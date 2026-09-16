import os
import cv2
import numpy as np

SPLIT_DIR = "caries_cls_dataset"

def augment_and_save(img, cls, count=50):
    train_count = int(count * 0.8)
    for i in range(count):
        split = "train" if i < train_count else "val"
        aug_img = img.copy()
        
        if np.random.rand() > 0.5:
            aug_img = cv2.flip(aug_img, 1)
            
        value = np.random.randint(-30, 30)
        hsv = cv2.cvtColor(aug_img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        v = cv2.add(v, value)
        v = np.clip(v, 0, 255)
        final_hsv = cv2.merge((h, s, v))
        aug_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        
        aug_img = cv2.resize(aug_img, (224, 224))
        cv2.imwrite(f"{SPLIT_DIR}/{split}/{cls}/img_{np.random.randint(100000)}.jpg", aug_img)

def process_healthy_teeth():
    print("Generating healthy teeth...")
    img = np.zeros((224, 224, 3), dtype=np.uint8)
    # White teeth color
    cv2.rectangle(img, (0, 0), (224, 224), (240, 240, 240), -1)
    # Pink gums
    cv2.rectangle(img, (0, 0), (224, 80), (180, 190, 255), -1)
    
    # Add some noise for realism
    noise = np.random.randint(-10, 10, (224, 224, 3), dtype=np.int16)
    img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    
    augment_and_save(img, "NoEnamel_Caries", count=50)

if __name__ == "__main__":
    process_healthy_teeth()
