import tkinter as tk
from tkinter import ttk

login_window = tk.Tk()  
login_window.geometry("400x250")
login_window.title("Login")

username = ttk.Label(login_window, text = "Username:").place(x = 30,y = 50)  
email = ttk.Label(login_window, text = "Email:").place(x = 30, y = 90)  
password = ttk.Label(login_window, text = "Password:").place(x = 30, y = 130)

entry1 = ttk.Entry(login_window).place(x = 100, y = 50)  
entry2 = ttk.Entry(login_window).place(x = 100, y = 90)  
entry3 = ttk.Entry(login_window).place(x = 100, y = 130)

login_window.mainloop() 
