import tkinter as tk
from strength_checker import check
import common_passwords

def run_app():
    window= tk.Tk()
    window.title("PASSWORD CHECKER")
    window.geometry("500x500")
 
    input_label=tk.Label(window,text="Enter Password",font=("areal",12),fg="green")
    input_label.pack(pady=10)
    password_entry=tk.Entry(window,font=("arial",12),show="*");
    password_entry.pack(pady=10)

    def strength():       
        
        output = check(password_entry.get())
        result_label.config(text=output,fg="teal",font="areal")

    button =tk.Button(
        window,text="Check Strength",command=strength,bg="pink"
    )
    button.pack(pady=10)

    result_label=tk.Label(window,text="",justify="left")
    result_label.pack(pady=15)
    window.mainloop()

