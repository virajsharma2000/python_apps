import cv2
import cvlib

samosa_per_person = int(input('Enter how many samosa one person should get: '))

camera = cv2.VideoCapture(0)

while True:
 if camera.isOpened():
  ret, frame = camera.read()

  cv2.imshow('camera',frame)

  if cv2.waitKey(1) & 0xFF == ord('s'):
   faces, confidences = cvlib.detect_face(frame)
  
   number_of_faces = len(faces)

   if number_of_faces > 0:
    number_of_samosas = number_of_faces * samosa_per_person

    print(number_of_samosas)

    break

   else:
    print('no person found')
    break

 else:
  print('failed to open camera')

camera.release()
cv2.destroyAllWindows()
