import cv2
from gtts import gTTS
import pyglet
import os
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width/2)
    cy = int(height/2)

    pixel_center = frame[cy, cx]
    hue_value = pixel_center[0]
    sat_value = pixel_center[1]
    val_value = pixel_center[2]

    color = "Undefined"
    if (val_value == 0) and (sat_value <= 255) and (hue_value <=255):
        color = "BLACK"
        s = gTTS(text="Black", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 255) and (sat_value <= 50) and (val_value >= 210 and val_value <= 255):
        color = "WHITE"
        s = gTTS(text="White", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 5) and (sat_value <= 100) and (val_value >= 180 and val_value <= 255):
        color = "RED"
        s = gTTS(text="Red", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value > 5 and hue_value <= 17) and (sat_value >=150 and sat_value <= 255) and (val_value >= 200 and val_value <= 255):
        color = "ORANGE"
        s = gTTS(text="Orange", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value > 17 and hue_value <= 37) and (sat_value >= 110 and sat_value <= 180) and (val_value >= 220 and val_value <= 255):
        color = "YELLOW"
        s = gTTS(text="Yellow", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value > 38 and hue_value <= 48) and (sat_value >= 140 and sat_value <= 190) and (val_value >= 230 and val_value <= 255):
        color = "LIME GREEN"
        s = gTTS(text="Lime Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value > 48 and hue_value < 70) and (sat_value >= 225 and sat_value <= 255) and (val_value >= 220 and val_value <= 255) :
        color = "GREEN"
        s = gTTS(text="Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif hue_value > 77 and hue_value < 98:
        color = "SKY BLUE"
        s = gTTS(text="Sky Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value > 80 and hue_value < 100) and (sat_value >= 70 and sat_value <= 200) and (val_value >= 245 and val_value <= 255):
        color = "LIGHT BLUE"
        s = gTTS(text="Light Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value > 102 and hue_value < 126) and (sat_value >= 225 and sat_value <= 255) and (val_value >= 35 and val_value <= 255):
        color = "DARK BLUE"
        s = gTTS(text="Dark Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value > 140 and hue_value < 150) and (sat_value >= 80 and sat_value <= 255) and (val_value >= 150 and val_value >= 210):
        color = "VIOLET"
        s = gTTS(text="Violet", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value > 155 and hue_value < 172) and (sat_value >= 100 and sat_value <= 255) and (val_value >= 220 and val_value <= 255):
        color = "PINK"
        s = gTTS(text="Pink", lang='en')
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
