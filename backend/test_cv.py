import cv2
import numpy as np
import os

img_path = "/Users/soham/.gemini/antigravity-ide/brain/8973671f-d860-4b5f-857c-7ea1224bfa73/.user_uploaded/media_1789492127579.png"
if not os.path.exists(img_path):
    print("Image not found")
else:
    img = cv2.imread(img_path)
    h, w = img.shape[:2]
    # Crop to just the image part (assuming it's a screenshot)
    # The image in the screenshot is roughly in the center-left
    # Let's just run it on the whole thing and filter by size
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    boxes = []
    for cnt in contours:
        x, y, bw, bh = cv2.boundingRect(cnt)
        area = bw * bh
        # Filter for teeth-like sizes
        if 500 < area < 20000 and 0.5 < (bh/bw) < 3.0:
            boxes.append((x, y, bw, bh))
            
    print(f"Found {len(boxes)} potential teeth")
