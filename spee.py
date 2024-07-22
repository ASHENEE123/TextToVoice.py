from gtts import gTTS
import os
import cv2
print(cv2.__version__)
te="enter your text "
t1=gTTS(text=te, lang='hi',slow=True)
t1.save("first.mp3")
os.system("first.mp3")
