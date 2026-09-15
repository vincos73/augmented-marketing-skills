#!/usr/bin/env python3
"""Validate deterministic Vincos SVG layout invariants without dependencies."""

import math
import re
import sys
import xml.etree.ElementTree as ET


NUM = r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?"


def nums(value):
    return [float(number) for number in re.findall(NUM, value or "")]


def points(element):
    tag = element.tag.rsplit("}", 1)[-1]
    values = nums(element.get("points"))
    if len(values) < 6 or len(values) % 2:
        raise ValueError(f"{tag} richiede almeno 3 coppie x,y")
    return list(zip(values[::2], values[1::2]))


def bbox(element):
    tag = element.tag.rsplit("}", 1)[-1]
    if tag == "rect":
        x, y, width, height = (
            float(element.get(key, "0"))
            for key in ("x", "y", "width", "height")
        )
        if width < 0 or height < 0:
            raise ValueError("rect con dimensione negativa")
        return x, y, x + width, y + height
    if tag in ("polygon", "polyline"):
        pairs = points(element)
        xs, ys = zip(*pairs)
        return min(xs), min(ys), max(xs), max(ys)
    if tag == "circle":
        cx, cy, radius = (
            float(element.get(key, "0")) for key in ("cx", "cy", "r")
        )
        if radius < 0:
            raise ValueError("circle con raggio negativo")
        return cx - radius, cy - radius, cx + radius, cy + radius
    if tag == "line":
        x1, y1, x2, y2 = (
            float(element.get(key, "0"))
            for key in ("x1", "y1", "x2", "y2")
        )
        return min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    return None


def has_chamfer_segment(element, cut):
    pairs = points(element)
    segments = zip(pairs, pairs[1:] + pairs[:1])
    return any(
        abs(x2 - x1) >= cut and abs(y2 - y1) >= cut
        for (x1, y1), (x2, y2) in segments
    )


def connector_segments(element):
    tag = element.tag.rsplit("}", 1)[-1]
    if tag == "line":
        return [
            (
                (float(element.get("x1", "0")), float(element.get("y1", "0"))),
                (float(element.get("x2", "0")), float(element.get("y2", "0"))),
            )
        ]
    if tag == "polyline":
        pairs = points(element)
        return list(zip(pairs, pairs[1:]))
    raise ValueError("connettore validabile solo su line o polyline")


def segment_crosses_box_interior(start, end, box):
    """Return true when an open segment enters a node's interior bbox."""
    x1, y1 = start
    x2, y2 = end
    xmin, ymin, xmax, ymax = box
    epsilon = 1e-6
    xmin += epsilon
    ymin += epsilon
    xmax -= epsilon
    ymax -= epsilon
    if xmin >= xmax or ymin >= ymax:
        return False

    dx = x2 - x1
    dy = y2 - y1
    lower = 0.0
    upper = 1.0
    for direction, distance in (
        (-dx, x1 - xmin),
        (dx, xmax - x1),
        (-dy, y1 - ymin),
        (dy, ymax - y1),
    ):
        if abs(direction) < epsilon:
            if distance < 0:
                return False
            continue
        ratio = distance / direction
        if direction < 0:
            lower = max(lower, ratio)
        else:
            upper = min(upper, ratio)
        if lower > upper:
            return False
    return upper - lower > epsilon


def report(errors):
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("OK: SVG Vincos valido")
    return 0


def main(path):
    errors = []
    try:
        root = ET.parse(path).getroot()
    except (OSError, ET.ParseError) as exc:
        print(f"ERROR: SVG non leggibile: {exc}")
        return 1

    view_box = nums(root.get("viewBox"))
    if len(view_box) != 4 or view_box[2] <= 0 or view_box[3] <= 0:
        errors.append("viewBox deve avere x, y, larghezza e altezza positive")
    if errors:
        return report(errors)

    vx, vy, width, height = view_box
    footer_y = vy + height * 0.88
    elements = list(root.iter())
    footer = [
        element
        for element in elements
        if element.get("data-vincos-footer") == "true"
    ]
    if not footer:
        errors.append('manca un elemento data-vincos-footer="true"')

    for element in elements:
        tag = element.tag.rsplit("}", 1)[-1]
        try:
            box = bbox(element)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        if element.get("data-vincos-footer") == "true":
            if not box:
                errors.append(f"footer marcato su geometria non supportata: {tag}")
            else:
                if box[1] < footer_y:
                    errors.append("footer fuori dalla fascia inferiore del 12%")
                if (
                    box[0] < vx
                    or box[1] < vy
                    or box[2] > vx + width
                    or box[3] > vy + height
                ):
                    errors.append("footer fuori dal canvas")

        if element.get("data-vincos-content") == "true" and not box:
            errors.append(f"contenuto marcato su geometria non supportata: {tag}")
        if element.get("data-vincos-content") == "true" and box:
            if box[3] > footer_y:
                errors.append("contenuto nella safe zone footer inferiore del 12%")
            elif footer_y - box[3] < 24:
                errors.append("contenuto con gap inferiore a 24 px dal footer")

        raw_cut = element.get("data-vincos-chamfer-cut")
        if raw_cut is None:
            continue
        try:
            cut = float(raw_cut)
        except ValueError:
            cut = None
        if cut is None or not math.isfinite(cut):
            errors.append("chamfer con cut non numerico o non finito")
            continue
        if cut < 16:
            errors.append("chamfer con cut inferiore a 16 px")
        if tag != "polygon":
            errors.append("chamfer validabile solo su polygon")
            continue
        if not box:
            errors.append("chamfer marcato senza geometria verificabile")
            continue
        if not has_chamfer_segment(element, cut):
            errors.append(
                "chamfer senza lato diagonale con Δx e Δy almeno pari al cut dichiarato"
            )
        if (
            box[0] < vx
            or box[1] < vy
            or box[2] > vx + width
            or box[3] > vy + height
        ):
            errors.append("chamfer fuori dal canvas")
        if box[3] > footer_y:
            errors.append("chamfer nella safe zone footer")

    nodes = [
        element for element in elements if element.get("data-vincos-node") == "true"
    ]
    connectors = [
        element
        for element in elements
        if element.get("data-vincos-connector") == "true"
    ]
    node_boxes = []
    for node in nodes:
        box = bbox(node)
        if not box:
            tag = node.tag.rsplit("}", 1)[-1]
            errors.append(f"nodo marcato su geometria non supportata: {tag}")
        else:
            node_boxes.append(box)

    for connector in connectors:
        try:
            segments = connector_segments(connector)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if any(
            segment_crosses_box_interior(start, end, node_box)
            for start, end in segments
            for node_box in node_boxes
        ):
            errors.append("connettore attraversa l'interno di un nodo")

    return report(errors)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: validate_svg.py FILE.svg")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
