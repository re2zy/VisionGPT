# VisionGPT — Intelligent Object Interaction Agent

Go beyond detection — VisionGPT understands scenes. It identifies objects, infers their spatial relationships ("cup on table", "person near chair"), and answers natural-language questions about images using a VQA model.

## Models used

| Task | Model |
|---|---|
| Object detection | [facebook/detr-resnet-50](https://huggingface.co/facebook/detr-resnet-50) |
| Visual question answering | [Salesforce/blip2-opt-2.7b](https://huggingface.co/Salesforce/blip2-opt-2.7b) |

## Project structure

```
visiongpt/
├── models/detr.py          # loads DETR model
├── pipeline/
│   ├── detector.py         # image → detected objects
│   ├── scene_graph.py      # objects → spatial relationships
│   └── vqa.py              # image + question → answer
└── utils/visualizer.py     # draws bounding boxes, saves result

app.py                      # Streamlit web UI
main.py                     # CLI entry point
config.py                   # model names, thresholds, paths
test_images/                # sample images for testing
outputs/                    # saved visualizations
```

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Web UI

```bash
streamlit run app.py
```

Upload an image, click **Analyze** to see detected objects and scene relationships, then type a question to get a VQA answer.

### CLI

```bash
python main.py test_images/kitchen.jpg
python main.py test_images/desk.jpg --question "What is on the desk?"
```

Output: detected objects printed to terminal, annotated image saved to `outputs/result.jpg`.

## Example output

Given `test_images/kitchen.jpg`:

```
Found 4 object(s):
  cup (0.97)
  microwave (0.95)
  refrigerator (0.91)
  dining table (0.90)

Relationships:
  cup on dining table
  microwave near refrigerator

VQA: What is on the table?
Answer: a cup
```

## Applications

- Home automation — identify objects and their layout for smart home context
- Robotics — spatial reasoning for navigation and manipulation
- AR perception — scene understanding for augmented reality overlays
