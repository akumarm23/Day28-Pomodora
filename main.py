# Pomodora Application v0.1

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF0000"
RED = "#e7305b"
GREEN = "#00FF00"
YELLOW = "#f7f5dd"
PURPLE = '#800080'
WHITE = '#FFFFFF'
BLACK = '#000000'
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="TIMER")
    checkmark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long-Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short-Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="WORK", fg=BLACK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        session = math.floor(reps/2)
        for _ in range(session):
            mark += "✓"
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORA APP")
window.config(padx=20, pady=20, bg=YELLOW)


title_label = Label(text="TIMER", fg=RED, bg=YELLOW, font=(FONT_NAME, 55))
title_label.grid(column=1,row=0)


canvas = Canvas(width=300, height=450, bg=GREEN, highlightthickness=0)
tom = PhotoImage(file="tomato.png")
canvas.create_image(150, 225, image=tom)
timer_text = canvas.create_text(150,250, text="00:00", font=(FONT_NAME, 55, "bold"))
canvas.grid(column=1,row=1)

start = Button(text="START", command=start_timer, fg=PURPLE, font=(FONT_NAME, 25), highlightthickness=0, borderwidth=0)
start.grid(column=0,row=2)

reset = Button(text="RESET",command=reset_timer ,fg=PURPLE, font=(FONT_NAME, 25), highlightthickness=0, borderwidth=0 )
reset.grid(column=2,row=2)

checkmark = Label(text="",fg=GREEN,bg=BLACK, font=(FONT_NAME, 50))
checkmark.grid(column=1,row=3)

window.mainloop()

# END OF CODE