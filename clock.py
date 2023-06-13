from tkinter import *
from tkinter.ttk import *
from time import strftime

# Creating tkinter window
root = Tk()
root.title('Clock')

# Display time on the label
def time():
    string = strftime('%H:%M:%S')
    lbl.config(text=string)
    lbl.after(1000, time)

# Appearance of the clock
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='white',
            foreground='black')

# Place clock at the center of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()
