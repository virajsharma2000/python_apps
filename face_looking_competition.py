import cv2
import cvlib
import os
import easygui

image_file_name = easygui.fileopenbox('choose image file of people')

image = cv2.imread(image_file_name)

faces, confidences = cvlib.detect_face(image)

if len(faces) > 0:
  bounding_box = faces[confidences.index(max(confidences))]
  
  x1, y1, x2, y2 = bounding_box[0], bounding_box[1], bounding_box[2], bounding_box[3]

  cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

  cv2.imshow('competition result', image)

  cv2.waitKey(0)

else:
  print('Error - no face found')
