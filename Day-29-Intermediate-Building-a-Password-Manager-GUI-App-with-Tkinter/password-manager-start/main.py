from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_letters = [random.choice(string.ascii_letters) for char in range(random.randint(8,10))]
    password_symbols = [random.choice(string.punctuation) for char in range(random.randint(2,4))]
    password_numbers = [random.choice(string.digits) for char in range(random.randint(2,4))]
    
    password_all = password_letters + password_numbers + password_symbols

    random.shuffle(password_all)
    final_password = "".join(password_all)
    pyperclip.copy(final_password)
    if entry_password:
        entry_password.delete(0, END)
    entry_password.insert(0, final_password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    password = entry_password.get()
    username = entry_username.get()
    website = entry_website.get()
    new_data = {
        website: {
            "email": username,
            "password": password, 
        }
    }

    if password and username and website:
        is_ok = messagebox.askokcancel(title=website, message=f"Continue to save this password to the file?\n"
                                                        f"Username: {username}\n"
                                                        f"Password: {password}\n")
        
        if is_ok:
            try:
                with open("data.json", "r") as f:
                    data = json.load(f)

            except FileNotFoundError:
                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent=4)

            else:
                data.update(new_data)
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)

            finally:
                entry_website.delete(0, END)
                entry_password.delete(0, END)
    
    else:
        messagebox.showwarning(title="Invalid entry", message=f"You should fill all the details to save the password!")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password(): 
    website = entry_website.get()
    if website:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                email = data[website]["email"]
                password = data[website]["password"]
        except FileNotFoundError:
            messagebox.showwarning(title="No Saved Password", message=f"You did not save any password!")
        except KeyError:
            messagebox.showwarning(title="Password Does Not Exist", message=f"There's no saved password for {website}")
        else:
            messagebox.showinfo(title=f"{website} Info", message=f"Website : {website}\n"
                                                                f"Username: {email}\n"
                                                                f"Password: {password}\n")
    
    else:
        messagebox.showwarning(title="Invalid entry", message=f"Enter the website to search password!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=620, height=400)
window.config(padx=20,pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.place(x=300, y=80, anchor="center")

label_website = Label(text="Website:  ", justify="center", width=15)
label_website.place(x=100, y=200, anchor="center")

label_username = Label(text="Email/Username:  ", justify="center", width=15)
label_username.place(x=100, y=250, anchor="center")

label_password = Label(text="Password:  ", justify="center", width=15)
label_password.place(x=100, y=300, anchor="center")

entry_website = Entry(width=20, justify="center")
entry_website.place(x=270, y=200, anchor="center")

entry_username = Entry(width=40, justify="center")
entry_username.insert(0, "aygunnvsnss@gmail.com")
entry_username.place(x=360, y=250, anchor="center")

entry_password = Entry(width=20, justify="center")
entry_password.place(x=270, y=300, anchor="center")

button_generate_password = Button(text="Generate Password", justify="center", command=generate_password)
button_generate_password.place(x=465, y=300, anchor="center", height=24, width=155)

button_save_password = Button(text="Save Password", justify="center", command=save_password)
button_save_password.place(x=300, y=350, anchor="center", width=200)

button_search = Button(text="Search", justify="center", command=search_password)
button_search.place(x=465, y=200, anchor="center", height=24, width=155)

window.mainloop()
