######################### PROGRAMMER : S.MUKILAN ##############################

import difflib
import tkinter as tk
import random
import time
from PIL import Image,ImageTk
word_list = ["The fastest typing speed ever, 216 words per minute, was achieved by Stella Pajunas-Garnand\n from Chicago in 1946 in one minute on an IBM electric.\n As of 2005, writer Barbara Blackburn was the fastest English language typist\n in the world, according to The Guinness Book of World Records.\n Using the Dvorak Simplified Keyboard, she had maintained 150 wpm for 50 minutes,\n and 170 wpm for shorter periods, with a peak speed of 212 wpm.\n Blackburn, who failed her QWERTY typing class in high school, first encountered the Dvorak keyboard in 1938.\n quickly learned to achieve very high speeds, and occasionally toured giving speed-typing demonstrations during her secretarial career.\n She appeared on Late Night with David Letterman on January 24, 1985, but felt that Letterman made a spectacle of her.\n Blackburn died in April 2008."]
WINDOW =tk.Tk()
WINDOW.geometry('800x600')
WINDOW.title('TYPING SPEED TESTER')

tk.Label(WINDOW,fg='red',font=(None, 11),text='@creator by S.MUKILAN').place(x=10,y=575)
entry = tk.Entry(WINDOW, borderwidth=8)
entry.place(x=35,y=475,height=45,width=720)
tutorial = Image.open('h_t.jpg')
tutorial = ImageTk.PhotoImage(tutorial)
tutorial_s = tk.Button(WINDOW,image=tutorial)
tutorial_s.place(x=260,y=50)

def start():
    try:
        global entry
        tutorial_s.destroy()
        entry.destroy()
        entry = tk.Entry(WINDOW, borderwidth=8)
        entry.place(x=35,y=475,height=45,width=720)
    except():
        pass
    global time_s
    
    info = tk.Label(WINDOW,font=(None,14),text="Type Above Para In The Given Box And click Enter")
    info.place(x=175,y=540)
    time_s = time.time()
    try:
        global acc,skl,tm,wpm
        acc.destroy()
        tm.destroy()
        wpm.destroy()
        skl.destroy()
    except:
        pass
    try:
        global orgin,star,trya
        star.destroy()
        trya.destroy()
        orgin.destroy()  
    except:
        pass
    global orginal
    orginal = random.choice(word_list)
    orgin = tk.Button(WINDOW,font=(None,10),text=orginal)
    orgin.place(x=6,y=115)
    
title = tk.Label(WINDOW, fg="red",bg='black',font=(None,25), text="TYPING SPEED TESTER").place(x=200,y=30)
star = tk.Button(WINDOW, borderwidth=5, bg = 'black', fg='red',text='START', command=lambda:start())
star.place(x=175,y=540, height=30,width=450)
tk.Label(WINDOW,fg="black",font=(None,16),text="YOUR ACCURANCY: ").place(x=30,y=320)
tk.Label(WINDOW,fg="black",font=(None,16),text="YOUR TIME: ").place(x=30,y=400)
tk.Label(WINDOW,fg="black",font=(None,16),text="YOUR TYPING SKILL: ").place(x=400,y=400)
tk.Label(WINDOW,fg="black",font=(None,16),text="WORDS PER MINIUTE: ").place(x=400,y=320)

def result(Event):
    try:
        orgin.destroy()
    except:
        pass
    global orginal,trya,acc,skl,tm,wpm,time,time_s,tutorial_s
    tutorial_s.destroy()
    tutorial_s = tk.Button(WINDOW,image=tutorial)
    tutorial_s.place(x=260,y=50)
    title = tk.Label(WINDOW, fg="red",bg='black',font=(None,25), text="TYPING SPEED TESTER").place(x=200,y=30)
    typed = entry.get()
    typed_word = 1
    try:
        global acc,skl,tm,wpm
        acc.destroy()
        tm.destroy()
        wpm.destroy()
        skl.destroy()
    except:
        pass
    for i in typed:
        if (i==' '):
            typed_word += 1
    time_e = time.time()
    try:
        trya.destroy()
    except:
        pass
    try:
        accurency = difflib.SequenceMatcher(None,orginal,typed).ratio()*100
        trya = tk.Button(WINDOW, borderwidth=5, bg = 'black', fg='white',text='TRY AGAIN', command=lambda:start())
        trya.place(x=175,y=540, height=30,width=450)
        time_show = time_e - time_s - 1   
        tim_in_min = time_show/60
        word_per_min = int(typed_word/tim_in_min)
    
        if (word_per_min < 65 and word_per_min > 30) and (int(accurency) > 80) and int(accurency) <= 100:
            skill = "AVERAGE"
        if (word_per_min <= 30) or (int(accurency) <= 75):
            skill = "WEAK"
        if (word_per_min >= 65) and (int(accurency) >= 90):
            skill = "EXCELLENT"

        if (skill == "AVERAGE"):
            clr = 'orange'
        if (skill == "WEAK"):
            clr = 'red'
        if (skill == "EXCELLENT"):
            clr = 'green'

        accu = ("%.2f" % round(accurency, 2))
        acc = tk.Label(WINDOW,fg=clr,font=(None,16),text=str(accu)+"%")
        acc.place(x=250,y=320)
        tm = tk.Label(WINDOW,fg=clr,font=(None,16),text=str(int(time_show))+' Seconds')
        tm.place(x=170,y=400)
        wpm = tk.Label(WINDOW,fg=clr,font=(None,16),text=str(int(word_per_min)))
        wpm.place(x=640,y=320)
        skl = tk.Label(WINDOW,fg=clr,font=(None,16),text=str(skill))
        skl.place(x=625,y=400)
    except:
        pass
    
WINDOW.bind("<Return>", result)
WINDOW.mainloop()

######################### PROGRAMMER : S.MUKILAN ##############################
