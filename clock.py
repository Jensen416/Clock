import tkinter as tk
import time as t

# Creating tkinter window
root = tk.Tk()
root.title('Clock')

# Add timezone info
timezone_info = t.tzname[t.daylight]
timezone = tk.Label(root, text=timezone_info, font=('calibri', 30))
timezone.pack(anchor='center')

# Configure the clock
def time():
    now = datetime.datetime.now()
    time_12hr = now.strftime('%I:%M:%S %p')
    clock.config(text=time_12hr)
    clock.after(1000, time)

# Appearance of the clock
clock = tk.Label(root, font=('calibri', 40, 'bold'),
            background='white',
            foreground='black')
clock.pack(anchor='center')
time()

root.mainloop()
