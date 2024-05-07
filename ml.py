import torch
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.train(data="data.yaml",source="Aerial-Airport.v1-v1.yolov5-obb/train",epochs=5)