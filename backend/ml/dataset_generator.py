import os
import random
import cv2
import numpy as np

# Configuration
NUM_IMAGES = 100
IMG_SIZE = 416
DATASET_DIR = "dataset"
CLASSES = ["healthy", "mild", "moderate", "severe"]

def create_dirs():
    dirs = [
        f"{DATASET_DIR}/images/train",
        f"{DATASET_DIR}/images/val",
        f"{DATASET_DIR}/labels/train",
        f"{DATASET_DIR}/labels/val"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

def generate_image(filename_prefix, subset="train"):
    # Create a dark background (like X-ray)
    img = np.zeros((IMG_SIZE, IMG_SIZE, 3), dtype=np.uint8)
    # Add some noise
    noise = np.random.randint(0, 50, (IMG_SIZE, IMG_SIZE, 3), dtype=np.uint8)
    img = cv2.add(img, noise)
    
    num_teeth = random.randint(4, 10)
    labels = []
    
    for _ in range(num_teeth):
        # Tooth properties
        w = random.randint(40, 80)
        h = random.randint(60, 100)
        x = random.randint(w//2, IMG_SIZE - w//2)
        y = random.randint(h//2, IMG_SIZE - h//2)
        
        # Draw tooth (white-ish)
        tooth_color = (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
        cv2.ellipse(img, (x, y), (w//2, h//2), 0, 0, 360, tooth_color, -1)
        
        # Determine condition
        condition_idx = random.choices([0, 1, 2, 3], weights=[0.5, 0.2, 0.2, 0.1])[0]
        
        if condition_idx > 0:
            # Draw caries (dark spot)
            caries_size = condition_idx * random.randint(5, 10)
            cx = x + random.randint(-w//4, w//4)
            cy = y + random.randint(-h//4, h//4)
            cv2.circle(img, (cx, cy), caries_size, (30, 30, 30), -1)
            
        # YOLO format: class_id center_x center_y width height (normalized)
        labels.append(f"{condition_idx} {x/IMG_SIZE} {y/IMG_SIZE} {w/IMG_SIZE} {h/IMG_SIZE}")
    
    img_path = f"{DATASET_DIR}/images/{subset}/{filename_prefix}.jpg"
    label_path = f"{DATASET_DIR}/labels/{subset}/{filename_prefix}.txt"
    
    cv2.imwrite(img_path, img)
    with open(label_path, "w") as f:
        f.write("\n".join(labels))

def generate_yaml():
    yaml_content = f"""path: {os.path.abspath(DATASET_DIR)}
train: images/train
val: images/val

names:
  0: healthy
  1: mild
  2: moderate
  3: severe
"""
    with open(f"{DATASET_DIR}/dataset.yaml", "w") as f:
        f.write(yaml_content)

if __name__ == "__main__":
    print("Generating synthetic dataset...")
    create_dirs()
    for i in range(NUM_IMAGES):
        subset = "train" if i < int(NUM_IMAGES * 0.8) else "val"
        generate_image(f"img_{i}", subset)
    generate_yaml()
    print("Dataset generation complete!")
