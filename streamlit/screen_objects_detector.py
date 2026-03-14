from ultralytics import YOLO
import pyautogui
import numpy as np
import json

yolo_model = YOLO('yolov8n.pt')

while True:
 array = np.asarray(pyautogui.screenshot())

 objects = json.loads(yolo_model(array)[0].to_json())

 for object_ in objects:
  print(object_)