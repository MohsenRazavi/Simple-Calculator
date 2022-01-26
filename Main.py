from tkinter import *
import tkinter.messagebox

#  ============================ base settings =========================

root = Tk()

root.title('My proffesional calculator!')
root.geometry('400x200')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

# ======================= functions and variables ===================================
num1 = StringVar()
num2 = StringVar()
res_num = StringVar()

def errorMsg(message):
    if message == 'error':
        tkinter.messagebox.showerror('Error', 'Something went wrong')
    elif message == 'zd error':
        tkinter.messagebox.showerror('Error', 'devision by ziro impossible')


def plus():
    try:
        result = int(num1.get()) + int(num2.get())
        res_num.set(result)
    except:
        errorMsg('error')


def min():
    try:
        result = int(num1.get()) - int(num2.get())
        res_num.set(result)
    except:
        errorMsg('error')


def mul():
    try:
        result = int(num1.get()) * int(num2.get())
        res_num.set(result)
    except:
        errorMsg('error')


def div():
    if num2.get() == '0':
        errorMsg('zd error')
    else:
        try:
            result = int(int(num1.get()) / int(num2.get()))
            res_num.set(result)
        except:
            errorMsg('error')


#  =========================== frames =================================
top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)

# ============================ buttons ======================

btn_plus = Button(top_third, text='+', width=10, highlightbackground=color, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=10, pady=10)

btn_min = Button(top_third, text='-', width=10, highlightbackground=color, command=lambda: min())
btn_min.pack(side=LEFT, padx=10, pady=10)

btn_mul = Button(top_third, text='*', width=10, highlightbackground=color, command=lambda: mul())
btn_mul.pack(side=LEFT, padx=10, pady=10)

btn_div = Button(top_third, text='/', width=10, highlightbackground=color, command=lambda: div())
btn_div.pack(side=LEFT, padx=10, pady=10)

# ============================ labels and entries ============================

input1_txt = Label(top_first, text='Enter first num :', bg=color)
input1_txt.pack(side=LEFT, padx=10, pady=10)
first_num_get = Entry(top_first, textvariable=num1)
first_num_get.pack(side=LEFT, padx=10, pady=10)

input2_txt = Label(top_second, text='Enter second num :', bg=color)
input2_txt.pack(side=LEFT, padx=10, pady=10)
second_num_get = Entry(top_second, textvariable=num2)
second_num_get.pack(side=LEFT, padx=10, pady=10)

res = Label(top_forth, text='Result :', bg=color)
res.pack(side=LEFT, padx=10, pady=10)
res_show = Entry(top_forth, textvariable=res_num)
res_show.pack(side=LEFT, padx=10, pady=10)





tkinter.mainloop()
