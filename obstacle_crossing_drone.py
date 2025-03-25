import cv2
from ultralytics import YOLO, settings
import json
import logging
import playsound

logging.getLogger("ultralytics").setLevel(logging.ERROR)

camera = cv2.VideoCapture(2)
yolo_model = YOLO('yolov8n.pt')

while True:
 ret, frame = camera.read()

 cv2.imshow('drone view', frame)
 
 objects = json.loads(yolo_model(frame)[0].to_json())

 confidences = []

 for object_ in objects:
  confidences.append(object_['confidence'])
 
 if confidences and max(confidences) > 0.7:
  playsound.playsound('/home/viraj/Downloads/mixkit-shop-scanner-beeps-1073-[AudioTrimmer.com].wav')

 if cv2.waitKey(1) & 0xFF == ord('q'):
  break
