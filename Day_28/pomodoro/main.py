from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    tick.config(text="")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps%8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    elif reps%2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
import math

def count_down(count):
    global timer

    print(count)
    mins=count//60
    if len(str(count//60))<2:
        mins="0"+str(count//60)

    secs=count%60
    if len(str(count%60))<2:
        secs="0"+str(count%60)
    canvas.itemconfig(timer_text, text =f"{mins}:{secs}")
    if count > 0:
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps%2==0:
            marks = ""
            for _ in range(0,math.floor(reps/2)):
                marks += "✔"
            tick.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro - by Anshika")
window.config(padx=150,pady=65, bg=YELLOW)


timer_label = Label(text="Timer",font=("Courier",48),fg=GREEN,bg=YELLOW)
timer_label.grid(column=1,row=0)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,32,"bold"))
canvas.grid(column=1,row=1)

# count_down(5)

start_button = Button(text="Start", font=(FONT_NAME,12),command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", font=(FONT_NAME,12), command=reset_timer)
reset_button.grid(column=2,row=2)

tick = Label(font=(FONT_NAME,20),fg=GREEN,bg=YELLOW)
tick.grid(column=1,row=3)

window.mainloop()