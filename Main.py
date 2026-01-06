import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Controller, Key
import time
import winsound

# Keyboard controller
keyboard = Controller()

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# -------------------------------
# Keyboard Layout
# -------------------------------
keys = [
    ["Q","W","E","R","T","Y","U","I","O","P"],
    ["A","S","D","F","G","H","J","K","L","<<"],
    ["Z","X","C","V","B","N","M","SPACE"]
]

finalText = ""

# Timing control
pressDelay = 2  # delay between key presses
lastPressTime = 0

# -------------------------------
# Button Class
# -------------------------------
class Button:
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.text = text
        self.size = size

# -------------------------------
# Create Buttons
# -------------------------------
buttonList = []
for i, row in enumerate(keys):
    for j, key in enumerate(row):
        if key == "SPACE":
            buttonList.append(Button([100*j + 50, 100*i + 50], key, [350, 85]))
        else:
            buttonList.append(Button([100*j + 50, 100*i + 50], key))

# -------------------------------
# Draw Keyboard
# -------------------------------
def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), cv2.FILLED)

        text_x = x + 20 if button.text != "SPACE" else x + 120
        cv2.putText(img, button.text, (text_x, y+60),
                    cv2.FONT_HERSHEY_PLAIN, 2.5, (255, 0, 0), 3)
    return img

# -------------------------------
# Main Loop
# -------------------------------
while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)
    img = drawAll(img, buttonList)

    if hands:
        lmList = hands[0]["lmList"]
        ix, iy = lmList[8][0], lmList[8][1]   # Index finger tip

        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < ix < x+w and y < iy < y+h:
                # Highlight hover
                cv2.rectangle(img, (x, y), (x+w, y+h),
                              (175, 0, 175), cv2.FILLED)

                text_x = x + 20 if button.text != "SPACE" else x + 120
                cv2.putText(img, button.text, (text_x, y+60),
                            cv2.FONT_HERSHEY_PLAIN, 2.5, (255, 255, 255), 3)

                # Single touch logic with delay
                if time.time() - lastPressTime > pressDelay:
                    lastPressTime = time.time()

                    if button.text == "<<":
                        keyboard.press(Key.backspace)
                        keyboard.release(Key.backspace)
                        finalText = finalText[:-1]
                        winsound.Beep(400, 120)

                    elif button.text == "SPACE":
                        keyboard.press(Key.space)
                        keyboard.release(Key.space)
                        finalText += " "
                        winsound.Beep(600, 120)

                    else:
                        keyboard.press(button.text)
                        keyboard.release(button.text)
                        finalText += button.text
                        winsound.Beep(800, 60)

                    # Press effect
                    cv2.rectangle(img, (x, y), (x+w, y+h),
                                  (0, 0, 255), cv2.FILLED)

    # -------------------------------
    # Display Typed Text
    # -------------------------------
    cv2.rectangle(img, (50, 380), (1150, 480), (0, 0, 0), cv2.FILLED)
    cv2.putText(img, finalText, (60, 450),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

    cv2.imshow("Virtual Keyboard - Single Touch", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
