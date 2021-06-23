import pyautogui
import time
from tkinter import *


def show_frame(frame):
    frame.tkraise()


# Making the window
win = Tk()
win.title("Spam bot 9000")
win.geometry("450x220")
win.iconbitmap("C:\\Users\\Max\\Documents\\Python programs\\Spammer\\spammericon.ico")
win.wm_attributes("-topmost", 1)
win.resizable(False, False)

win.rowconfigure(0, weight=1)
win.columnconfigure(0, weight=1)

main = Frame(win)
sett = Frame(win)
hel = Frame(win)

settbtnimg = PhotoImage(file=r"settbtn.png")
settbtnimgs = settbtnimg.subsample(25, 25)

helpbtnimg = PhotoImage(file=r"helpbtn.png")
helpbtnimgs = helpbtnimg.subsample(15, 15)

for frame in (main, sett, hel):
    frame.grid(row=0, column=0, sticky="nsew")


def settings():
    print("'open settings'")


# ======================================================================================================== main =================================================================================
main_title = Label(main, text="Main", bg="dodger blue")
main_title.pack(fill="x")

# options button
optionsbtn = Button(main, image=settbtnimgs, command=lambda: show_frame(sett))
optionsbtn.place(relx=0, rely=0.1)

howtobtn = Button(main, image=helpbtnimgs, width=7, command=lambda: show_frame(hel))
howtobtn.place(relx=0.949, rely=0.1, width=23, height=23)

var2 = StringVar()
var2.set("Delay")
slidert = Entry(main, textvar=var2)
slidert.place(relx=0.5, rely=0.22, anchor="center")

# Number of spams
value = DoubleVar()
slider = Scale(main, orient="horizontal", from_="1", to="250", variable=value)
slider.place(relx=0.5, rely=0.35, anchor="center", width=285)

# Spam text
var = StringVar()
var.set("Message")
textbox = Entry(main, textvar=var)
textbox.place(relx=0.33, rely=0.6, anchor="center", height=25)

warninglbl = Label(main, text="Wait for the spaming to stop before you click off the dm's", fg="red")
warninglbl.place(relx=0.5, rely=0.8, anchor="center")


def spam():
    global sleep
    slidert.get()
    if isinstance(slidert, str):
        slidert.delete(0, END)
    else:
        sleep = False
        time.sleep(5)
        selection = value.get()
        spamno = 0
        stme = int(var2.get())
        if stme > 1:
            sleep = True
        while spamno < selection:
            if sleep:
                sleep = False
            else:
                if chkValue.get() == 1 and chkValue1.get() == 1:
                    word = textbox.get()
                    pyautogui.typewrite("/" + word)
                    pyautogui.press("enter")
                    spamno = spamno + 1
                    time.sleep(stme)
                elif chkValue.get() == 1:
                    word = textbox.get()
                    pyautogui.typewrite(word)
                    pyautogui.press("enter")
                    spamno = spamno+1
                    time.sleep(stme)
                elif chkValue.get() != 1 and chkValue1.get() == 1:
                    word = textbox.get()
                    pyautogui.typewrite("/" + word)
                    spamno = spamno + 1
                    time.sleep(stme)
                else:
                    word = textbox.get()
                    pyautogui.typewrite(word)
                    spamno = spamno+1
                    time.sleep(stme)
            if var.get() == "BEE":
                f = open("supersecret.txt", 'r')
                win.update()
                for word in f:
                    var.set(f)
                    pyautogui.typewrite(word)
            else:
                if chkValue.get() == 1 and chkValue1.get() == 1:
                    word = textbox.get()
                    pyautogui.typewrite("/" + word)
                    pyautogui.press("enter")
                    spamno = spamno + 1
                elif chkValue.get() == 1:
                    word = textbox.get()
                    pyautogui.typewrite(word)
                    pyautogui.press("enter")
                    spamno = spamno+1
                elif chkValue.get() != 1 and chkValue1.get() == 1:
                    word = textbox.get()
                    pyautogui.typewrite("/" + word)
                    spamno = spamno + 1
                else:
                    word = textbox.get()
                    pyautogui.typewrite(word)
                    spamno = spamno+1


# Spam button
spam = Button(main, text="Spam!", command=spam, width=17, bg="green")
spam.place(relx=0.665, rely=0.6, anchor="center")

# ======================================================================================================== settings =============================================================================
main_title = Label(sett, text="Settings", bg="dodger blue")
main_title.pack(fill="x")

backbtn = Button(sett, text="Back", width=6, command=lambda: show_frame(main))
backbtn.place(relx=0.06, rely=0.16, anchor="center")

chkValue = IntVar()
chkValue.set(True)
ntrcb = Checkbutton(sett, text="Press enter after word", variable=chkValue)
ntrcb.place(relx=0, rely=0.25)

chkValue1 = IntVar()
rblxcb = Checkbutton(sett, text="Roblox mode (types '/' before message)", variable=chkValue1)
rblxcb.place(relx=0, rely=0.35)

minlbl = Label(sett, text="Mins Between Messages")
minlbl.place(relx=0, rely=0.45)

mslbl = Label(sett, text="More coming soon!")
mslbl.place(relx=0.5, rely=0.7, anchor="center")

# ======================================================================================================== help =================================================================================
main_title = Label(hel, text="Help", bg="dodger blue")
main_title.pack(fill="x")

backbtn2 = Button(hel, text="Back", width=6, command=lambda: show_frame(main))
backbtn2.place(relx=0.06, rely=0.16, anchor="center")

# Text
point1 = Label(hel, text=u'\u2022 Open your targets instagram dms')
point1.place(relx=0.05, rely=0.3)
point2 = Label(hel, text=u'\u2022 Type the message you want to spam them with in to the box')
point2.place(relx=0.05, rely=0.4)
point3 = Label(hel, text=u'\u2022 Select how many times you want to send the message using the slider')
point3.place(relx=0.05, rely=0.5)
point4 = Label(hel, text=u'\u2022 Press the spam button')
point4.place(relx=0.05, rely=0.6)
point5 = Label(hel, text=" Note: you will have a few seconds until the spam starts")
point5.place(relx=0.5, rely=0.8, anchor="center")

show_frame(main)

win.mainloop()
