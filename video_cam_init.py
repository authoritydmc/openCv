import cv2
import datetime
cap=cv2.VideoCapture(0)
wid=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#for windows use : *'DIVX'
#for linux use : *'XVID'
#some falana demkana

writer=cv2.VideoWriter('initVideoOpenCV.mp4',cv2.VideoWriter_fourcc(*'XVID'),20,(wid,height))
while True:
    ret,fr=cap.read()
    if cv2.waitKey(1) & 0xFF==27:
        break
    ff=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.putText(fr,f"{datetime.datetime.now().strftime('%H:%M:%S')} {datetime.date.today()}",( 20,height-20),ff,1,(255,255,255))
    writer.write(fr)
    cv2.imshow("Hello",fr)
cv2.destroyAllWindows()
cap.release()
writer.release()