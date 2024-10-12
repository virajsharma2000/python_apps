import cv2
import cvlib

camera = cv2.VideoCapture(2)

while True:
 ret, frame = camera.read()

 cv2.imshow('camera', frame)

 if cv2.waitKey(1) & 0xFF == ord('p'):
  faces, confidences = cvlib.detect_face(frame)
  
  number_of_faces = len(faces)

  print(number_of_faces)
  
  break

