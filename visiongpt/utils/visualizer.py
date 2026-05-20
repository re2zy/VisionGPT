from PIL import Image, ImageDraw
import os
import config

COLORS = [
    "#e6194b", "#3cb44b", "#ffe119", "#4363d8", "#f58231",
    "#911eb4", "#42d4f4", "#f032e6", "#bfef45", "#fabebe",
]


def visualize(image_path: str, detections: list[dict], output_path: str = None) -> str:
    if output_path is None:
        output_path = os.path.join(config.OUTPUT_DIR, "result.jpg")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(image)

    for i, det in enumerate(detections):
        color = COLORS[i % len(COLORS)]
        x1, y1, x2, y2 = det["box"]
        draw.rectangle([x1, y1, x2, y2], outline=color, width=3)
        draw.text((x1 + 4, y1 + 4), f"{det['label']} {det['score']:.2f}", fill=color)

    image.save(output_path)
    return output_path
