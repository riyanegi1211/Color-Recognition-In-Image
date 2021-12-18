import cv2
from gtts import gTTS
import pyglet
import os
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# To take a series of frame
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

# To find the center of the frame
    cx = int(width/2)
    cy = int(height/2)

    pixel_center = frame[cy, cx]
    print(pixel_center)
    hue_value = pixel_center[0]
    sat_value = pixel_center[1]
    val_value = pixel_center[2]

    color = "Undefined"
    if (val_value == 0) and (sat_value <= 255) and (hue_value <= 255):
        color = "BLACK"
        s = gTTS(text="Black", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value >= 240 and hue_value <= 255) and (sat_value >= 242 and sat_value<= 255) and (val_value >= 225 and val_value <= 255):
        color = "WHITE"
        s = gTTS(text="White", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 18) :
        color = "RED"
        s = gTTS(text="Red", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value >= 80 and hue_value <= 90) and (sat_value >= 205 and sat_value <= 235) and (val_value ==255) :
        color = "ORANGE"
        s = gTTS(text="Orange", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value >= 17 and hue_value <= 40) :
        color = "YELLOW"
        s = gTTS(text="Yellow", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value > 40 and hue_value <= 50):
        color = "LIME GREEN"
        s = gTTS(text="Lime Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value > 50 and hue_value < 77) :
        color = "GREEN"
        s = gTTS(text="Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value > 77 and hue_value < 103) :
        color = "LIGHT BLUE"
        s = gTTS(text="Light Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value > 103 and hue_value < 125):
        color = "DARK BLUE"
        s = gTTS(text="Dark Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value > 125 and hue_value < 150):
        color = "PURPLE"
        s = gTTS(text="Purple", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value > 150 and hue_value < 174) :
        color = "PINK"
        s = gTTS(text="Pink", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    else:
        color = "RED"
        s = gTTS(text="Red", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)


    pixel_center_bgr = frame[cy, cx]
    cv2.putText(frame, color, (10,50), 0, 1, (255, 0, 0), 2)
    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
