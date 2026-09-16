import os
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models
from torch.utils.data import DataLoader, TensorDataset

def create_dummy_dataset(num_samples=100, img_size=224):
    X = torch.randn(num_samples, 3, img_size, img_size)
    y = torch.randint(0, 4, (num_samples,))
    return TensorDataset(X, y)

def train_mobilenet():
    print("Initializing MobileNetV2...")
    model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
    num_ftrs = model.classifier[1].in_features
    model.classifier[1] = nn.Linear(num_ftrs, 4)
    
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    train_data = create_dummy_dataset(100)
    train_loader = DataLoader(train_data, batch_size=16, shuffle=True)
    
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
            
    os.makedirs("models", exist_ok=True)
    torch.save(model.state_dict(), "models/mobilenet_v2_dental.pth")
    print("Model saved to models/mobilenet_v2_dental.pth")

if __name__ == "__main__":
    train_mobilenet()
