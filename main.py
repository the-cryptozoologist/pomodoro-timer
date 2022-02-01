# ---------------------------- IMPORTS ------------------------------- #
import tkinter as tk
import math

# ---------------------------- GLOBAL ------------------------------- #
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
marks = ""
work_total = 0


# ---------------------------- TIMER SKIP ------------------------------- #

# skip current timer
def skip():
    window.after_cancel(timer)
    start_timer()


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    start.config(state="normal")
    global marks
    global reps
    global work_total
    work_total = 0
    reps = 0
    marks = ""
    check_marks.config(text=marks)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", font=(FONT_NAME, 35, "bold"), bg=GREEN, fg="white", pady=10, padx=10)
    canvas.itemconfig(pomodoro_counter, text="")


# ---------------------------- TIMER SETUP ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60

    short_break_sec = SHORT_BREAK_MIN * 60

    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        label.config(text="Break", font=(FONT_NAME, 35, "bold"), bg=GREEN, fg=YELLOW, pady=10, padx=10)
        global marks
        marks += "✓"
        check_marks.config(text=marks)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label.config(text="Break", font=(FONT_NAME, 35, "bold"), bg=GREEN, fg=PINK, pady=10, padx=10)
        marks += "✓"
        check_marks.config(text=marks)
    else:
        countdown(work_sec)
        label.config(text="Work", font=(FONT_NAME, 35, "bold"), bg=GREEN, fg=RED, pady=10, padx=10)

    if reps % 8 == 1:
        marks = ""
        check_marks.config(text=marks)
    elif reps % 8 == 0:
        global work_total
        work_total += 1
        canvas.itemconfig(pomodoro_counter, text=work_total)


# ---------------------------- COUNTDOWN SETUP ------------------------------- #

def countdown(count):
    start.config(state="disabled")
    count_min = math.floor(count // 60)
    count_sec = count % 60
    if count_sec < 1:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)
window.resizable(False, False)

label = tk.Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=GREEN, fg="white", pady=10, padx=10)
label.grid(row=0, column=1)

check_marks = tk.Label(text="", font=(FONT_NAME, 15, "bold"), bg=GREEN, fg="white", pady=10, padx=10)
check_marks.grid(row=2, column=1, padx=10)

canvas = tk.Canvas(width=210, height=250, background=GREEN, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)
pomodoro_counter = canvas.create_text(103, 170, text="", fill="white", font=(FONT_NAME, 20, "bold"))

start = tk.Button(text="Start", command=start_timer, bg=PINK, fg="white", font=(FONT_NAME, 20, "bold"))
start.grid(row=3, column=1, pady=10)

skip = tk.Button(text="Skip", command=skip, bg=PINK, fg="white", font=(FONT_NAME, 20, "bold"))
skip.grid(row=2, column=0, pady=10)

reset = tk.Button(text="Reset", command=reset_timer, bg=PINK, fg="white", font=(FONT_NAME, 20, "bold"))
reset.grid(row=2, column=2, pady=10)

window.mainloop()
