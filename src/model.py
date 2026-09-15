from PIL import Image


def analyze_image(image: Image.Image) -> dict:
    """
    Placeholder AI analysis interface.

    The actual trained AI model can be connected here.
    """
    return {
        "condition": "Normal PCB",
        "confidence": 0.50,
        "severity": "Low",
        "location": "No suspicious region identified",
    }
