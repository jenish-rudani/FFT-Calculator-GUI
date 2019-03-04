from tkinter import *
from scipy import fftpack
import numpy as np


def get_varibles(num):
    global i
    display.insert(i, num)
    i += 1


def clear_all():
    display.delete(0, END)
    display2.delete(0, END)


def get_undo():
    string = display.get()
    if len(string):
        new_string = string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")


def Calculate():
    new_string = int(display.get())
    y = [int(x) for x in str(new_string)]
    result = fftpack.fft(y)
    np.set_printoptions(precision=2)
    clear_all()
    display.insert(0, "Real:  ")
    display2.insert(0, "Imag: ")
    print(result.real)
    display.insert(6, result.real)
    display2.insert(5, result.imag)
    print(result.imag)
    return


# Defining Buttons
def Mybutton(newroot):
    Button(newroot, text='1', command=lambda: get_varibles(1), height=1, width=7).grid(row=3, column=0)
    Button(newroot, text='2', command=lambda: get_varibles(2), height=1, width=7).grid(row=3, column=1)
    Button(newroot, text='3', command=lambda: get_varibles(3), height=1, width=7).grid(row=3, column=2)

    Button(newroot, text='4', command=lambda: get_varibles(4), height=1, width=7).grid(row=4, column=0)
    Button(newroot, text='5', command=lambda: get_varibles(5), height=1, width=7).grid(row=4, column=1)
    Button(newroot, text='6', command=lambda: get_varibles(6), height=1, width=7).grid(row=4, column=2)

    Button(newroot, text='7', command=lambda: get_varibles(7), height=1, width=7).grid(row=5, column=0)
    Button(newroot, text='8', command=lambda: get_varibles(8), height=1, width=7).grid(row=5, column=1)
    Button(newroot, text='9', command=lambda: get_varibles(9), height=1, width=7).grid(row=5, column=2)

    Button(newroot, text='AC', command=lambda: clear_all(), height=1, width=7).grid(row=6, column=0)
    Button(newroot, text='0', command=lambda: get_varibles(0), height=1, width=7).grid(row=6, column=1)
    Button(newroot, text='FFT', command=lambda: Calculate(), height=1, width=7).grid(row=6, column=2)

    Button(newroot, text='<-', command=lambda: get_undo(), height=1, width=7).grid(row=3, column=3)
    Button(newroot, text='', height=1, width=7).grid(row=4, column=3)
    Button(newroot, text='', height=1, width=7).grid(row=5, column=3)
    Button(newroot, text='', height=1, width=7).grid(row=6, column=3)


if __name__ == '__main__':
    root = Tk()
    root.configure(bg='LightBlue')
    root.geometry("800x200")
    root.title("FFT Calculator")
    i = 0
    display = Entry(root, font="Helvetica 14", width=100)

    display2 = Entry(root, font="Helvetica 14", width=100)

    # label.config(font=("Courier", 44))
    display.grid(row=1, columnspan=60, sticky=W + E)
    display2.grid(row=2, columnspan=60, sticky=W + E)
    Mybutton(root)
    root.mainloop()
