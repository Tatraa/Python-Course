import tkinter as tk
from tkinter import StringVar, Button, Entry
import tkinter.font as font

okno = tk.Tk()
okno.title("Calculator")

myFont = font.Font(family='Arial', size=20, weight='bold')

ans_entry =  Entry(okno, bd=5, width=20, font=myFont, bg="gray", fg="white")
ans_entry.grid(row=0, column=0, columnspan=4)

equation = {
    'num_1': '',
    'num_2': '',
    'oper': ''
}

def mouse_button_release(event):
    widg = event.widget
    text = widg.cget("text")

    if text in "0123456789":
        ans_entry.insert(len(ans_entry.get()), text)
        if equation['oper'] == '':
            equation['num_1'] += text
        else:
            equation['num_2'] += text

    elif text in "+-*/":
        if equation['num_1'] != '':
            equation['oper'] = text
            ans_entry.insert(len(ans_entry.get()), text)

    elif text == "C":
        ans_entry.delete(0, tk.END)
        equation['num_1'] = ''
        equation['num_2'] = ''
        equation['oper'] = ''

    elif text == "=":
        if equation['num_1'] != '' and equation['num_2'] != '' and equation['oper'] != '':
            result = 0
            num1 = int(equation['num_1'])
            num2 = int(equation['num_2'])

            if equation['oper'] == '+':
                result = num1 + num2
            elif equation['oper'] == '-':
                result = num1 - num2
            elif equation['oper'] == '*':
                result = num1 * num2
            elif equation['oper'] == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    ans_entry.delete(0, tk.END)
                    ans_entry.insert(0, "Error")
                    return

            ans_entry.delete(0, tk.END)
            ans_entry.insert(0, str(result))
            equation['num_1'] = str(result)
            equation['num_2'] = ''
            equation['oper'] = ''

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    btn = Button(okno, text=button, padx=20, pady=10)
    btn['font'] = myFont
    btn.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

okno.bind("<ButtonRelease-1>", mouse_button_release)

okno.mainloop()
