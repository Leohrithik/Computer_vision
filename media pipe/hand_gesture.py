import cv2
import mediapipe as mp
mphands=mp.solutions.hands
draw=mp.solutions.drawing_utils
hands=mphands.Hands()


cap=cv2.VideoCapture(0)
while True:
    suc,image=cap.read()
    image=cv2.flip(image,1)
    imgrgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    res=hands.process(imgrgb) 
    image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    if res.multi_hand_landmarks:
         for handlms in res.multi_hand_landmarks:
             draw.draw_landmarks(image,handlms,mphands.HAND_CONNECTIONS)       



    cv2.imshow('Hand Gesture Detection',image)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
