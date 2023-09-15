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
    #print(res)
    image=cv2.cvtColor(imgrgb,cv2.COLOR_RGB2BGR)
    cv2.rectangle(image,(20,350),(90,440),(0,255,0),cv2.FILLED)
    cv2.rectangle(image,(20,350),(90,440),(255,0,0),3)

    lmlist=[]
    tipids=[4,8,12,16,20]

    if res.multi_hand_landmarks:
        for handlms in res.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):
                #print(id,lm)
                cx=lm.x
                cy=lm.y
                lmlist.append([id,cx,cy])
                #print(lmlist)

    fingerlist=[]
    if len(lmlist)!=0 and len(lmlist)==21:
        if lmlist[12][1]<lmlist[20][1]:    # check right or left
            if lmlist[tipids[0]][1]>lmlist[tipids[0]-1][1]:    #X value of tip increases when finger closed
                fingerlist.append(0)       # append 0 when closed
            else:
                fingerlist.append(1)       # append 1 when opened
        else:
            if lmlist[tipids[0]][1]<lmlist[tipids[0]-1][1]:   # x value decreases when hand closed 
                fingerlist.append(0)
            else:
                fingerlist.append(1)
    



        for id in range(1,5):  #thumb is cosidered seperately
            if lmlist[tipids[id]][2]>lmlist[tipids[id]-2][2]:
                fingerlist.append(0)
            else:
                fingerlist.append(1)
    #print(fingerlist)
        if len(fingerlist)!=0:
            fingercount=fingerlist.count(1)
            print(fingercount)

        cv2.putText(image,str(fingercount),(30,420),cv2.FONT_HERSHEY_PLAIN,6,(0,0,0),5)
        
        





        draw.draw_landmarks(image,handlms,mphands.HAND_CONNECTIONS)


    cv2.imshow('hand gesture counting',image)
    

    
    if cv2.waitKey(1) & 0XFF==ord('k'):
        break
cap.release()
cv2.destroyAllWindows()
