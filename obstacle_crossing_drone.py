import cv2
from ultralytics import YOLO, settings
import json
import logging

logging.getLogger("ultralytics").setLevel(logging.ERROR)

camera = cv2.VideoCapture(0)
yolo_model = YOLO('yolov8n.pt')

while True:
 ret, frame = camera.read()

 objects = json.loads(yolo_model(frame)[0].to_json())

 confidences = []

 for object_ in objects:
  confidences.append(object_['confidence'])
 
 if confidences and max(confidences) >= 0.6 and max(confidences) <= 0.7:
  print('go up, obstacle detected')

 if cv2.waitKey(1) & 0xFF == ord('q'):
  break
