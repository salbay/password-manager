# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import tkinter.messagebox
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Pasword Manager")
#window.geometry("500x300")
window.config(padx=20,pady=20)
window.maxsize(550,400)
window.minsize(550,400)

canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,95,image=logo_image)
canvas.grid(row=0,column=1,columnspan=2)

def onClick():
    pass


def getting_info():
    website = website_entry.get()
    email = email_entry.get()
    pasw = password_entry.get()
    datas = {"website":website,"email":email,"pasword":pasw}
    dataa = [website, " | ",email, " | ",pasw,"\n"]

    if website=="" or pasw=="":
        messagebox.showinfo(message="Please dont leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=email,
                                       message=f"These are the details entered:\nEmail: {email}\nPassword: {pasw}\nIs it ok to save?")
        if is_ok:
            messagebox.showinfo(title="Warning!", message="Your datas has been saved successfully.")
            with open("database","r") as file:
                old_data = file.read()

            with open("database","w") as file:
                file.write(old_data)
                for data in dataa:
                    file.write(data)

        website_entry.delete(0,END)
        password_entry.delete(0,END)
        website_entry.focus()

import random
import pyperclip
def generate_pasw():
    password_entry.delete(0,END)
    all = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "v",
           "y", "z", "A", "B", "C",
           "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "W", "V", "Y", "Z",
           "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
           "@", "£", "!", "'", "^", "+", "%", "&", "/", "(", ")", "=", "?", "-", ";", ":", ">"]
    new_pasword = ""
    for i in range(15):
        a = random.choice(all)
        new_pasword += a
    password_entry.insert(0,new_pasword)
    pyperclip.copy(new_pasword)


website_label = Label(text="Website:",fg="black")
website_label.grid(row=1,column=0)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=2)

email_label = Label(text="Email/Username:",fg="black")
email_label.grid(row=2,column=0)
email_entry = Entry(width=35)
email_entry.insert(0,"salim@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)

password_label = Label(text="Password:",fg="black")
password_label.grid(row=3,column=0)
password_entry = Entry(width=18)
password_entry.grid(row=3,column=1)

generate_pasw_buton = Button(text="Generate Password",width=12,command=generate_pasw)
generate_pasw_buton.grid(row=3,column=2)

add_buton = Button(text="Add",width=33,command=getting_info)
add_buton.grid(row=4,column=1,columnspan=2)



window.mainloop()