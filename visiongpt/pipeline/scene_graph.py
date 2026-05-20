def _center(box):
    x1, y1, x2, y2 = box
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def _is_on(box_a, box_b):
    """True if box_a is resting on top of box_b (overlapping horizontally, a's bottom near b's top)."""
    ax1, ay1, ax2, ay2 = box_a
    bx1, by1, bx2, by2 = box_b
    horiz_overlap = ax1 < bx2 and ax2 > bx1
    near_top = abs(ay2 - by1) < (by2 - by1) * 0.5
    return horiz_overlap and near_top and ay2 <= by2


def _distance(box_a, box_b):
    cx_a, cy_a = _center(box_a)
    cx_b, cy_b = _center(box_b)
    return ((cx_a - cx_b) ** 2 + (cy_a - cy_b) ** 2) ** 0.5


def build_scene_graph(detections: list[dict]) -> list[str]:
    relationships = []
    for i, obj_a in enumerate(detections):
        for j, obj_b in enumerate(detections):
            if i >= j:
                continue
            label_a = obj_a["label"]
            label_b = obj_b["label"]
            box_a = obj_a["box"]
            box_b = obj_b["box"]

            if _is_on(box_a, box_b):
                relationships.append(f"{label_a} on {label_b}")
            elif _is_on(box_b, box_a):
                relationships.append(f"{label_b} on {label_a}")
            elif _distance(box_a, box_b) < 150:
                relationships.append(f"{label_a} near {label_b}")

    return relationships
