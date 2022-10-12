import pygame 
from pygame import mixer
from tkinter import *
import time
pygame.init()
mixer.init()


window_=Tk()
window_.geometry("300x300")
window_.resizable(False, False)

val = 0

def temp_text(e):
    entry_.delete(0,"end")

def ringAlarm():
    mixer.music.play()
    window_.after(val * 1000 *60, ringAlarm)

def setAlarm(e=""):
    global val
    try:
        val = int(entry_.get())
        ringAlarm()
    except:
        pass


window_.config(bg="Black")
window_.title("Hatırlatıcı")
entry_=Entry(window_,width=30,font="sans 14 normal")
entry_.config(fg="Gray")
entry_.pack()
entry_.insert(0,"Hatırlatma aralığı giriniz.(Dakika)")
entry_.bind("<FocusIn>", temp_text)
buton=Button(window_,width=30,height=5,text="Hatırlatıcıyı çalıştırmak için basın.",command=setAlarm)
buton.pack()
#entry_.bind("<KeyRelease>", setAlarm)

sound = 1
mixer.music.load("mb.mp3")
mixer.music.set_volume(sound)


#time.sleep(60*val)




window_.mainloop()


