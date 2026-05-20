from transformers import DetrImageProcessor, DetrForObjectDetection
import config

_processor = None
_model = None


def load_model():
    global _processor, _model
    if _model is None:
        _processor = DetrImageProcessor.from_pretrained(config.DETR_MODEL_NAME)
        _model = DetrForObjectDetection.from_pretrained(config.DETR_MODEL_NAME)
        _model.eval()
    return _processor, _model
