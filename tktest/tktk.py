import tkinter as tk
from tkinter import ttk


window= tk.Tk()
window.geometry("400x250")
window.title("Fill Color")


frame2 = tk.Frame(master=window, height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=window, height=270, bg="blue")
frame3.pack(fill=tk.X)

window.mainloop()