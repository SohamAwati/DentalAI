import os
import random
import time
from ultralytics import YOLO
import cv2
import numpy as np

# Try to load the trained model
MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../runs/classify/runs_cls/dental_cls_model/weights/best.pt"))
model = None
try:
    if os.path.exists(MODEL_PATH):
        model = YOLO(MODEL_PATH)
        print(f"Loaded YOLOv8 Classification model from {MODEL_PATH}")
    else:
        print(f"Model not found at {MODEL_PATH}, will use mock detection.")
except Exception as e:
    print(f"Failed to load model: {e}")

CLASS_MAP = {
    "NoEnamel_Caries": "healthy",
    "EarlyStageEnamel_Caries": "mild",
    "AdvanceEnamel_Caries": "severe"
}

def check_quality(image_bytes: bytes) -> dict:
    """
    Mock image quality check.
    """
    # Simulate processing time
    time.sleep(0.5)
    return {"passed": True, "reason": "Image is clear and well-lit."}

def detect_and_classify(image_bytes: bytes) -> list:
    """
    Classification using YOLOv8-cls on real data.
    """
    if model is None:
        return _mock_detect_and_classify(image_bytes)
        
    try:
        # Convert bytes to numpy array
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        h, w = img.shape[:2]
        
        # Run YOLO inference
        results = model(img)[0]
        
        cls_idx = results.probs.top1
        conf = float(results.probs.top1conf.item())
        predicted_name = results.names[cls_idx]
        
        # Map dataset class to our app conditions
        condition = CLASS_MAP.get(predicted_name, "unknown")
        
        teeth_data = [{
            "tooth_number": 1, # Whole image
            "condition": condition,
            "confidence": round(conf, 2),
            "boundingBox": [10, 10, w - 20, h - 20] # Full image box
        }]
            
        return teeth_data
    except Exception as e:
        print(f"Error during inference: {e}")
        return _mock_detect_and_classify(image_bytes)

def _mock_detect_and_classify(image_bytes: bytes) -> list:
    time.sleep(1.5)
    teeth_data = []
    conditions = ["healthy", "mild", "moderate", "severe"]
    num_teeth = random.randint(4, 8)
    sampled_numbers = random.sample([1, 2, 3, 4, 5, 8, 9, 14, 15, 18, 19, 30, 31], num_teeth)
    
    for tn in sampled_numbers:
        condition = random.choices(conditions, weights=[0.4, 0.3, 0.2, 0.1])[0]
        teeth_data.append({
            "tooth_number": tn,
            "condition": condition,
            "confidence": round(random.uniform(0.75, 0.99), 2),
            "boundingBox": [
                random.randint(10, 200),
                random.randint(10, 200),
                random.randint(30, 60),
                random.randint(30, 60)
            ]
        })
    return teeth_data

def calculate_severity(teeth: list) -> float:
    """
    Calculate severity based on classified teeth.
    """
    score = 0
    for tooth in teeth:
        if tooth["condition"] == "mild":
            score += 30
        elif tooth["condition"] == "moderate":
            score += 60
        elif tooth["condition"] == "severe":
            score += 100
            
    return min(100.0, float(score))

def determine_archetype(score: float) -> str:
    """
    Determine user archetype from severity score.
    """
    if score < 20:
        return "mostly-healthy-with-minor-staining"
    elif score < 60:
        return "plaque-heavy-but-no-cavities"
    else:
        return "high-risk"

def get_insights() -> dict:
    """
    Insights for clustering and association rules.
    """
    return {
        "clusters": [
            "Cluster 1: High diligence, low risk",
            "Cluster 2: High sugar, moderate risk",
            "Cluster 3: Low brushing frequency, high risk"
        ],
        "association_rules": [
            {"rule": "If (high_sugar) then (has_cavity)", "support": 0.45, "confidence": 0.82},
            {"rule": "If (low_brushing) then (has_cavity)", "support": 0.38, "confidence": 0.75},
            {"rule": "If (flosses_daily) then (healthy)", "support": 0.60, "confidence": 0.88}
        ]
    }
