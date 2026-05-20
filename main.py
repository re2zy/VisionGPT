import argparse
from visiongpt.pipeline.detector import detect
from visiongpt.pipeline.scene_graph import build_scene_graph
from visiongpt.pipeline.vqa import load_vqa_model, answer_question
from visiongpt.utils.visualizer import visualize


def main():
    parser = argparse.ArgumentParser(description="VisionGPT CLI")
    parser.add_argument("image", help="Path to input image")
    parser.add_argument("--question", "-q", default="What objects are in the image?")
    args = parser.parse_args()

    print("Detecting objects...")
    detections = detect(args.image)
    print(f"Found {len(detections)} object(s):")
    for d in detections:
        print(f"  {d['label']} ({d['score']:.2f})")

    print("\nBuilding scene graph...")
    relationships = build_scene_graph(detections)
    if relationships:
        print("Relationships:")
        for r in relationships:
            print(f"  {r}")
    else:
        print("No spatial relationships detected.")

    print(f"\nVQA: {args.question}")
    load_vqa_model()
    answer = answer_question(args.image, args.question)
    print(f"Answer: {answer}")

    output_path = visualize(args.image, detections)
    print(f"\nVisualization saved to: {output_path}")


if __name__ == "__main__":
    main()
