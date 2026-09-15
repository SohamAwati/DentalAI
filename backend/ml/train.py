import os
from ultralytics import YOLO

def main():
    # Load a pretrained classification model
    model = YOLO("yolov8n-cls.pt")

    # Train the model
    print("Starting YOLOv8 Classification training on Caries-Spectra dataset...")
    
    results = model.train(
        data=os.path.abspath("caries_cls_dataset"), 
        epochs=3, 
        imgsz=224, 
        project="runs_cls", 
        name="dental_cls_model"
    )
    
    print("Training complete! Model saved to runs_cls/dental_cls_model/weights/best.pt")

if __name__ == "__main__":
    main()
