import tkinter as tk

from zmq import Frame

win = tk.Tk()
win.title("John And The Miraculous Adventures Of Python")
win.geometry("1500x750")
win.resizable(False,False)
win.config(bg="black")
def startgame():
    def destruction():
        ttlshad1.destroy()
        titlelab.destroy()
        helplab.destroy()
        menushad.destroy()
        startbutt.destroy()
        optionbutt.destroy()
        exitbutt.destroy()
        aboutbutt.destroy()
    def click_to_start():
        destruction()
        chappage()
    
    def go_to_about():
        destruction()
        about()

    ttlshad1 = tk.Label(win, text="John And The Miraculous Adventures Of Python", font=("Arial", 30), fg="grey", bg= "grey")
    titlelab = tk.Label(win,text="John And The Miraculous Adventures Of Python",font=("Arial", 30), bg= "black", fg= "white")
    helplab = tk.Label(win, text="If you find yourself stuck, click on the 'About' section !!", font=("Arial", 20), fg="white", bg="black")
    ttlshad1.place(x=200, y=15)
    titlelab.place(x=190, y=10)
    helplab.place(x=350, y=700)

#Start menu: Has buttons for start menu including start, options, exit, and something else if i feel like adding more --------> COMPLETE
    menushad = tk.Label(win, text="START", font=("Arial", 30), width=13, height=9, bg="grey", fg="grey")
    startbutt = tk.Button(win, text="START", font=("Arial", 30), fg="white", bg="black", width=10, height=1,command=click_to_start)
    optionbutt = tk.Button(win, text="OPTIONS", font=("Arial", 30), fg="white", bg="black", width=10, height=1)
    aboutbutt = tk.Button(win, text="ABOUT", font=("Arial", 30), fg="white", bg="black", width=10, height=1, command=go_to_about)
    exitbutt = tk.Button(win, text="EXIT", font=("Arial", 30), fg="white", bg="black", width=10, height=1, command=win.destroy)
    menushad.place(x=550, y=100)
    startbutt.place(x=591, y=135)
    optionbutt.place(x=591, y=240)
    aboutbutt.place(x=591, y=345)
    exitbutt.place(x=591, y=450)

#Chapters: Player can access all the chapters. To play the next chapter he has to complete the previous chapter.

def chappage():
    headershad = tk.Label(win, text="Chapters", font=("Arial", 30), fg="grey", bg="grey")
    chapheader = tk.Label(win, text="Chapters", font=("Arial", 30), fg="white", bg="black")
    headershad.place(x=635, y=15)
    chapheader.place(x=630, y=10)
    def back_to_start():
        back.destroy()
    def back_click():
        back_to_start()
        chapheader.destroy()
        startgame()

    back = tk.Button(win, text = "<", font=("Arial", 30), width=3, height=1, fg="white", bg="black", borderwidth=0, command=back_click)
    back.place(x=10, y=10)

    chap_array = tk.Frame(win, bg="black")
    chap_array.place(x=20, y=200)

    chapter_1 = tk.Button(chap_array, text="CHAPTER 1: The Adventure Starts !", font=("Arial", 20), fg="white", bg="black", borderwidth=0)
    chapter_2 = tk.Button(chap_array, text="CHAPTER 2: Magic called programming !", font=("Arial", 20), fg="white", bg="black", borderwidth=0)
    chapter_1.pack()
    chapter_2.pack()

#About section: Gives a gist of the game, and also about the team.   ---------> INCOMPLETE
def about():
    headershad = tk.Label(win, text="About", font=("Arial", 30), fg="grey", bg="grey")
    aboutheader = tk.Label(win, text = "About", font=("Arial", 30), fg="white", bg="black")
    headershad.place(x=675, y=15)
    aboutheader.place(x=665, y=10)
    def back_to_start():
        back.destroy()
    def back_click():
        back_to_start()
        headershad.destroy()
        aboutheader.destroy()
        startgame()
    back = tk.Button(win, text ="<", font=("Arial", 30), width=3, height=1, fg="white", bg="black", borderwidth=0, command=back_click)
    back.place(x=10, y=10)

startgame()
win.mainloop()