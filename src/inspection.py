from defect_categories import DEFECT_CATEGORIES


def inspect_pcb(image_name: str) -> dict:
    return {
        "image": image_name,
        "detected_condition": "Normal PCB",
        "confidence": 0.50,
        "severity": "Low",
        "approximate_location": "No suspicious region identified",
        "probable_cause": "No visible defect detected",
        "recommended_action": "Continue with visual and electrical inspection.",
        "supported_categories": DEFECT_CATEGORIES,
    }
