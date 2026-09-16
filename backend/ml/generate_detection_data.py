import os
import shutil
import cv2
import numpy as np

DATASET_DIR = "dental_detect_dataset"

# YOLO classes
CLASSES = {
    0: "healthy",
    1: "mild",
    2: "moderate",
    3: "severe"
}

def create_dirs():
    if os.path.exists(DATASET_DIR):
        shutil.rmtree(DATASET_DIR)
    
    for split in ["train", "val"]:
        os.makedirs(f"{DATASET_DIR}/images/{split}", exist_ok=True)
        os.makedirs(f"{DATASET_DIR}/labels/{split}", exist_ok=True)
        
    with open(f"{DATASET_DIR}/data.yaml", "w") as f:
        f.write(f"train: images/train\n")
        f.write(f"val: images/val\n\n")
        f.write(f"nc: 4\n")
        f.write(f"names: ['healthy', 'mild', 'moderate', 'severe']\n")

def generate_image(img_id, split):
    # 640x640 image
    img = np.zeros((640, 640, 3), dtype=np.uint8)
    
    # Background (gums/mouth interior)
    cv2.rectangle(img, (0, 0), (640, 640), (100, 100, 200), -1) # dark red
    
    num_teeth = np.random.randint(4, 12)
    labels = []
    
    # Grid placement for teeth
    cols = 4
    rows = 3
    cell_w = 640 // cols
    cell_h = 640 // rows
    
    positions = np.random.choice(cols * rows, num_teeth, replace=False)
    
    for pos in positions:
        r = pos // cols
        c = pos % cols
        
        # Base tooth coords
        x1 = c * cell_w + np.random.randint(10, 30)
        y1 = r * cell_h + np.random.randint(10, 30)
        w = np.random.randint(70, 120)
        h = np.random.randint(90, 150)
        
        x2 = min(x1 + w, 639)
        y2 = min(y1 + h, 639)
        
        # Decide condition
        # Weights: 40% healthy, 30% mild, 20% moderate, 10% severe
        cls = np.random.choice([0, 1, 2, 3], p=[0.4, 0.3, 0.2, 0.1])
        
        # Draw tooth base (white/yellowish)
        cv2.rectangle(img, (x1, y1), (x2, y2), (220, 230, 240), -1)
        
        if cls == 1: # mild
            # draw small brown spot
            cv2.circle(img, (x1 + w//2, y1 + h//2), 10, (50, 100, 150), -1)
        elif cls == 2: # moderate
            # draw larger brown spots
            cv2.circle(img, (x1 + w//3, y1 + h//3), 20, (30, 70, 110), -1)
            cv2.circle(img, (x1 + int(w*0.7), y1 + int(h*0.7)), 15, (40, 80, 120), -1)
        elif cls == 3: # severe
            # draw huge black/dark brown area
            cv2.rectangle(img, (x1 + 10, y1 + h//2 - 20), (x2 - 10, y2 - 10), (10, 20, 30), -1)
            
        # Convert to YOLO format
        # YOLO needs normalized center x, center y, width, height
        x_center = (x1 + (x2 - x1) / 2) / 640.0
        y_center = (y1 + (y2 - y1) / 2) / 640.0
        norm_w = (x2 - x1) / 640.0
        norm_h = (y2 - y1) / 640.0
        
        labels.append(f"{cls} {x_center} {y_center} {norm_w} {norm_h}")
        
    # Add noise
    noise = np.random.randint(-15, 15, (640, 640, 3), dtype=np.int16)
    img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    
    cv2.imwrite(f"{DATASET_DIR}/images/{split}/img_{img_id}.jpg", img)
    with open(f"{DATASET_DIR}/labels/{split}/img_{img_id}.txt", "w") as f:
        f.write("\n".join(labels))

if __name__ == "__main__":
    create_dirs()
    # Generate 150 train, 30 val
    print("Generating train images...")
    for i in range(150):
        generate_image(i, "train")
    print("Generating val images...")
    for i in range(150, 180):
        generate_image(i, "val")
    print("Detection dataset generated successfully!")
