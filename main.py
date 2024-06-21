# import everything from tkinter
from tkinter import *
# ttk is a module that styles tkinter widgets
from tkinter import ttk

# pack() and grid() can't be used on the same parent window
# results in errors
# creating parent window with label
# child window with entry box

#============================ First Window =============================
root = Tk()
# set window parent window size
root.geometry("400x300")
# set window color
root.configure(bg='papaya whip')
root.title("Play Numbers")
# create label
label0 = Label(root, text="Play Numbers", pady=30, font="NuevaStdCond", bg='papaya whip')
label0.pack()
label1 = Label(root, text="1) Add pairs that equals to 10", pady=2, font="NuevaStdCond", bg='papaya whip')
label1.pack()
label2 = Label(root, text="2) Multiply pairs <= 80 ", pady=2, font="NuevaStdCond", bg='papaya whip')
label2.pack()
label3 = Label(root, text="3) Then enter 2 favorite numbers!", pady=2, font="NuevaStdCond", bg='papaya whip')
label3.pack()
label4 = Label(root, text="One will be doubled in coins!", pady=2, font="NuevaStdCond", bg='papaya whip')
label4.pack()


#============================= Second Window =================================
# A function to open new window
# Toplevel() makes it the last window
def open_win():
    child_win = Toplevel(root)
    child_win.title("Play Numbers")
    child_win.geometry("400x300")
    #content= entry.get()
    # hides the window without destroying it
    root.withdraw()

# create entry widget
#entry = ttk.Entry(root, width=35)
#entry.pack(ipady=4, pady=20)
# create button in main window
button_Main = ttk.Button(root, text="OK", command=open_win)
button_Main.pack(pady=20)
#e = Entry(root, width=35, borderwidth=5)
# grid() places the entry box in certain rows and columns
# columnspan will span the text field like a line
#e.pack()
#e.grid(row=2, column=2, columnspan=6, padx=4, pady=4)

def addNumb(num1, num2):
    return num1 + num2


# Define buttons
# command=... is where the function will go
    #button1 = Button(root, text="6", padx=40,pady=40, command=addNumb)
    #button2 = Button(root, text="15", padx=40,pady=40, command=addNumb)
    #button3 = Button(root, text="8", padx=40,pady=40, command=addNumb)
    #button4 = Button(root, text="2", padx=40,pady=40, command=addNumb)
    #button5 = Button(root, text="4", padx=40,pady=40, command=addNumb)
    #button6 = Button(root, text="1", padx=40,pady=40, command=addNumb)


# Place buttons on screen
    #button1.grid(row=2, column=0)
    #button2.grid(row=2, column=1)
    #button3.grid(row=2, column=2)

    #button4.grid(row=3, column=0)
    #button5.grid(row=3, column=1)
    #button6.grid(row=3, column=2)

root.mainloop()

# event loop