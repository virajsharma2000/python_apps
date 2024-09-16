import cv2
import cvlib
import playsound
import easygui

path_to_doorbell_sound = easygui.fileopenbox('open doorbell sound file')

camera = cv2.VideoCapture(0)

photo = []

while True:
  ret, frame = camera.read()
 
  faces, confidence = cvlib.detect_face(frame)

  if faces:
   playsound.playsound(path_to_doorbell_sound)

   if not photo:
    photo.append(frame)

  else:
   photo.clear()

  if photo:
   cv2.imshow('picture of person', photo[0])

   

  
