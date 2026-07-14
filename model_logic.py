import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

def get_resnet_model(num_classes):
    # Load ResNet18 with pre-trained weights
    model = models.resnet18(weights='DEFAULT')
    # Modify the last fully connected layer (fc)
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, num_classes)
    return model

# Define the Image Transformations
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])