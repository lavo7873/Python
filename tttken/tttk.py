import tkinter as tk
from tkinter import ttk

man_hinh_chinh =tk.Tk()
man_hinh_chinh.title('Demo')
man_hinh_chinh.geometry('500x500')



label1 = ttk.Label(man_hinh_chinh, text='Label 1',bg='green')
label1.place(relx= 0.2, rely=0.1)

man_hinh_chinh.mainloop()