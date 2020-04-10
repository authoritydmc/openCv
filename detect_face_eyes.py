import cv2
import datetime
cap=cv2.VideoCapture(0)
wid=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
eye_cascade=cv2.CascadeClassifier('/home/beast/python_Codes/openCV/haarcascades/haarcascade_eye.xml')
face_cascade=cv2.CascadeClassifier('/home/beast/python_Codes/openCV/haarcascades/haarcascade_frontalface_default.xml')
writer=cv2.VideoWriter('detect_face_eye.mp4',cv2.VideoWriter_fourcc(*'XVID'),20,(wid,height))

def detect_eye(img):
    raw_img=img.copy()
    raw_img=cv2.cvtColor(raw_img,cv2.COLOR_BGR2GRAY)
    eye_rects=eye_cascade.detectMultiScale(raw_img,scaleFactor=1.2,minNeighbors=5)
    for (x,y,w,h) in eye_rects:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5)
    return 
def detect_face(img):
    raw_img=img.copy()
    raw_img=cv2.cvtColor(raw_img,cv2.COLOR_BGR2GRAY)
    face_rects=face_cascade.detectMultiScale(raw_img,scaleFactor=1.2,minNeighbors=5)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),10)
    return 


while True:
    ret,fr=cap.read()

    if cv2.waitKey(1) & 0xFF==27:
        break
    ff=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    detect_eye(fr)
    detect_face(fr)
    cv2.putText(fr,f"{datetime.datetime.now().strftime('%H:%M:%S')} {datetime.date.today()}",( 20,height-20),ff,1,(255,255,255))
    cv2.imshow("Detect Face and Eye",fr)
    writer.write(fr)
cv2.destroyAllWindows()
cap.release()
writer.release()