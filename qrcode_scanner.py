import cv2
from pyzbar.pyzbar import decode
import webbrowser

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    cv2.imshow('QRcode scanner',frame)

    if any(decode(frame)):
        qr_code = decode(frame)[0].data.decode()

        webbrowser.open(qr_code)

        break
        

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

camera.release()
