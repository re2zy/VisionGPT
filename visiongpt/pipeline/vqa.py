from transformers import Blip2Processor, Blip2ForConditionalGeneration
from PIL import Image
import torch
import config

_processor = None
_model = None


def load_vqa_model():
    global _processor, _model
    if _model is None:
        dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        _processor = Blip2Processor.from_pretrained(config.BLIP2_MODEL_NAME)
        _model = Blip2ForConditionalGeneration.from_pretrained(
            config.BLIP2_MODEL_NAME, torch_dtype=dtype
        )
        _model.eval()
    return _processor, _model


def answer_question(image_path: str, question: str) -> str:
    processor, model = load_vqa_model()
    image = Image.open(image_path).convert("RGB")
    inputs = processor(image, question, return_tensors="pt")
    with torch.no_grad():
        generated = model.generate(**inputs, max_new_tokens=50)
    return processor.decode(generated[0], skip_special_tokens=True).strip()
