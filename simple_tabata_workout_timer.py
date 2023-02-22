"""
Simple Timer (Interval) for Tabata Workout

-> 8 Rounds
-> 6 Repetitions
-> 30 Seconds Workout
-> 20 Seconds Rest

Author: @calvinagas
Date: 02/21/2023

"""

import tkinter as tk
import os
import sys


def updateLabel(i):
    labelCounter['text'] = str(i)
    window.update()


def updateLableRound(j):
    labelRound['text'] = f'Round {j}'
    window.update()


def updateLableRepetition(j):
    labelRepetition['text'] = f'Round {j}'
    window.update()


def finish():
    labelInstruction['text'] = ''
    labelInstruction['bg'] = 'green'
    labelInstruction.pack_forget()

    labelRepetition['text'] = ''
    labelRepetition['bg'] = 'green'
    labelRepetition.pack_forget()

    labelRound['text'] = ''
    labelRound['bg'] = 'green'
    labelRound.pack_forget()

    labelCounter['text'] = ''
    labelCounter['bg'] = 'green'
    labelCounter.pack_forget()

    window.configure(bg='green')
    labelKey['text'] = 'Congratulations! You"ve made it!'
    labelKey['bg'] = 'green'
    window.after(5000, restart_program)


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def pre_workout():
    i = 6
    for _ in range(5):  # ready counter
        i = i - 1
        window.after(1000, updateLabel(i))


def start(event=None):
    k = 0
    j = 0
    pre_workout()
    for _ in range(6):
        k = k + 1
        for _ in range(8):  # round counter
            j = j + 1
            updateLableRound(j)
            workout()
            rest()
        updateLableRepetition(k)
    finish()


def workout():
    labelInstruction['text'] = 'Workout!'
    labelInstruction['bg'] = 'blue'
    window.configure(bg='blue')
    labelRound['bg'] = 'blue'
    labelRepetition['bg'] = 'blue'
    labelKey['bg'] = 'blue'
    labelCounter['bg'] = 'blue'

    i = 31
    for _ in range(30):
        i = i - 1
        window.after(1000, updateLabel(i))


def rest():
    labelInstruction['text'] = 'Rest!'
    labelInstruction['bg'] = 'red'
    window.configure(bg='red')
    labelRound['bg'] = 'red'
    labelRepetition['bg'] = 'red'
    labelKey['bg'] = 'red'
    labelCounter['bg'] = 'red'
    i = 21
    for _ in range(20):
        i = i - 1
        window.after(1000, updateLabel(i))


def reset(event=None):
    labelCounter['text'] = '0'
    window.mainloop()


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("1000x600")
    window.title("Simple Time Interval for Tabata Cardio Workout")
    window.iconbitmap("timer_ico.ico")
    window.resizable(False, False)

    labelRepetition = tk.Label(window, text='Repetition', font=('arial 30 bold', 30), bg='yellow')
    labelRepetition.place(anchor="center")
    labelRepetition.pack(padx=10, pady=15)

    labelRound = tk.Label(window, text='Round', font=('arial 30 bold', 30), bg='yellow')
    labelRound.place(anchor="center")
    labelRound.pack(padx=10, pady=15)

    labelInstruction = tk.Label(window, text='Get Ready', font=('arial 30 bold', 80), bg='yellow')
    labelInstruction.place(anchor="center")
    labelInstruction.pack(padx=30, pady=25)

    labelCounter = tk.Label(window, text='0', font=('arial 30 bold', 80), bg='yellow')
    labelCounter.place(anchor="center")
    labelCounter.pack(padx=30, pady=20)

    labelKey = tk.Label(window, text="Press [Spacebar] to start workout!, Press[Enter] to reset", font=('Arial', 18),
                        bg='yellow')
    labelKey.pack(padx=30, pady=25)

    window.bind("<space>", start)
    window.configure(bg='yellow')

    window.bind("<Return>", reset)

    window.mainloop()
