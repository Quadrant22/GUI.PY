# import everything from tkinter
from tkinter import *
import tkinter as tk
# ttk is a module that styles tkinter widgets
from tkinter import ttk

# pack() and grid() can't be used on the same parent window
# results in error
# creating parent window with label
# child window with entry box

#============================ First Window =============================
root = tk.Tk()
# set window parent window size
root.geometry("400x300")
# set window color
root.configure(bg='snow')
root.title("Play Numbers")
# create label        #font="NuevaStdCond"
label0 = tk.Label(root, text="Play Numbers", height=5, pady=10, bg='misty rose2', font=('Times New Roman', 15, 'bold'))
label0.pack()
label1 = tk.Label(root, text="Select a number to raise to the power of 4", pady=0, font=('Times New Roman', 10, 'bold'), bg='snow')
label1.pack()



#============================= Second Window =================================
# A function to open new window
# Toplevel() makes it the last window
def open_win():
    child_win = tk.Toplevel(root)
    child_win.title("Play Numbers")
    child_win.geometry("300x300")
    #entry1 = tk.Entry(child_win, width=40, borderwidth=1)
    #entry1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    #my_str1 = tk.StringVar()
    b2 = tk.Button(child_win, text="8", padx=30, pady=30, bg='misty rose2', command=lambda:my_function(8))
    b2.grid(row=1, column=0)
    #-----------------------------------------------------------------------
    b3 = tk.Button(child_win, text="12", padx=30, pady=30, command=lambda:my_function(12))
    b3.grid(row=1, column=1)
    # -----------------------------------------------------------------------
    b4 = tk.Button(child_win, text="6", padx=30, pady=30, bg='misty rose2', command=lambda:my_function(6))
    b4.grid(row=1, column=2)
    # -----------------------------------------------------------------------
    b5 = tk.Button(child_win, text="4", padx=30, pady=30, command=lambda:my_function(4))
    b5.grid(row=2, column=0)
    # -----------------------------------------------------------------------
    b6 = tk.Button(child_win, text="2", padx=30, pady=30, bg='misty rose2', command=lambda:my_function(2))
    b6.grid(row=2, column=1)
    # -----------------------------------------------------------------------
    b7 = tk.Button(child_win, text="5", padx=30, pady=30, command=lambda:my_function(5))
    b7.grid(row=2, column=2)
    # -----------------------------------------------------------------------

    def my_function(number):
        x = int(number) ** 4
        print(str(number) + str(" To the power of 4 is: " + str(x)))

    my_function(8)
    # hides the main window without destroying it
    root.withdraw()


# create button in main window
button_Main = ttk.Button(root, text="OK", command=open_win)
button_Main.pack(pady=20)



root.mainloop()

