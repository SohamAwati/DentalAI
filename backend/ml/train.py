import os
from ultralytics import YOLO

def main():
    print("Initializing YOLOv8 Object Detection training...")
    
    # We use the detection base model
    model = YOLO("yolov8n.pt") 
    
    data_yaml = os.path.abspath(os.path.join(os.path.dirname(__file__), "dental_detect_dataset/data.yaml"))
    
    # Train the model
    results = model.train(
        data=data_yaml,
        epochs=3, # Low epochs for quick demonstration
        imgsz=640,
        name="dental_detect_model"
    )
    
    print("Training complete! Model saved to runs/detect/dental_detect_model/weights/best.pt")

if __name__ == "__main__":
    main()
