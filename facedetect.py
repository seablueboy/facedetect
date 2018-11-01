import  cv2
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera=cv2.VideoCapture(0)


while True:
    (grabbed,frame)=camera.read()
    # frameclone=frame.copy()
    rect = detector.detectMultiScale(frame, scaleFactor=1.2)
    for (x, y, w, h) in rect:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('face',frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
camera.release()
cv2.destroyAllWindows()

