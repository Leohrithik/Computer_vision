import mediapipe as mp
import cv2

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hand = mpHands.Hands()

cap = cv2.VideoCapture(0)
while True:
    success, image = cap.read()
    image = cv2.flip(image, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hand.process(image)
    # print(results)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.rectangle(image, (20, 350), (90, 440), (0, 277, 33), cv2.FILLED)
    cv2.rectangle(image, (20, 350), (90, 440), (0, 0, 255), 4)

    lmlist = []
    tipids = [4, 8, 12, 16, 20]
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                # print(id,lm)
                cx = lm.x
                cy = lm.y
                lmlist.append([id, cx, cy])
                # print(lmlist)


    fingerlist = []

    if len(lmlist) != 0 and len(lmlist) == 21:
        for id in range(0,5):
            if lmlist[tipids[id]][2] > lmlist[tipids[id]-2][2]:
                fingerlist.append(0)
            else:
                fingerlist.append(1)    

    print(fingerlist)

            # mpDraw.draw_landmarks(image, hand_landmarks, mpHands.HAND_CONNECTIONS)

    cv2.imshow('Hand', image)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
