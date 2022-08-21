import pygame
from pygame import mixer
from tkinter import *
import os

def play():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pause():
    songstatus.set("Paused")
    mixer.music.pause()

def stop():
    songstatus.set("Stopped")
    mixer.music.unpause()

def resume():
    songstatus.set("Resuming")
    mixer.music.unpause()

root=Tk()
root.title('Music Player')
root.geometry("425x602")
root.config(bg='light blue')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#add the playlist

playlist=Listbox(root,selectmode=SINGLE,bg="#330033",fg="Yellow",font=('Kunstler Script',19),width=40,height=21)
playlist.grid(columnspan=15)

os.chdir(r'F:\YouTube\Music Player\Songs List')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="PLAY",command=play)
playbtn.config(font=('Arial Black',15),bg="purple",fg="white",padx=8,pady=7)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="PAUSE",command=pause)
pausebtn.config(font=('Arial Black',15),bg="purple",fg="white",padx=8,pady=7)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="STOP",command=stop)
stopbtn.config(font=('Arial Black',15),bg="purple",fg="white",padx=8,pady=7)
stopbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="RESUME",command=resume)
Resumebtn.config(font=('Arial Black',15),bg="purple",fg="white",padx=8,pady=7)
Resumebtn.grid(row=1,column=3)

mainloop()