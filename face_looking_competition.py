import cv2
import cvlib
import os
import easygui

camera = cv2.VideoCapture(2)

while True:
 ret, frame = camera.read()

 cv2.imshow('camera', frame)

 if cv2.waitKey(1) & 0xFF == ord('j'):
  faces, confidences = cvlib.detect_face(frame)

  if len(faces) > 0:
   bounding_box = faces[confidences.index(max(confidences))]
   
   x1, y1, x2, y2 = bounding_box[0], bounding_box[1], bounding_box[2], bounding_box[3]

   cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

   cv2.imshow('competition result', frame)
