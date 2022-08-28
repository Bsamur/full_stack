from gtts import gTTS
import os
from os import path

dosya=open("C:\Users\LENOVO\Desktop\azranınhikayesi.txt",encoding="utf-8")
yazi=dosya.read()
cikti=gTTS(text=yazi,lang='tr',slow=False)
cikti.save("azranınhikayesi.mp3")
os.system("azranınhikayesi.mp3")
dosya.close()


