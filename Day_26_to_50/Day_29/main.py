from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCHING WEBSITE ------------------------------- #
def find_password():
    try:
        with open("passwords.json") as file:
            data = json.load(file)
            try:
                messagebox.showinfo(title="Credentials",message=f"Email : {data[website_input.get()]['email']}\n Password : {data[website_input.get()]['password']}")
            except:
                messagebox.showinfo(title="Error",message="No details for the website exists")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data file found")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def gen_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_to_file():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open('passwords.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                # file.write(f"{website} | {email} | {password}\n")
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            print(website, email, password)

            with open("passwords.json", "w") as file:
                # file.write(f"{website} | {email} | {password}\n")
                json.dump(data, file, indent=4)
        finally:
            password_input.delete(0, END)
            website_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Anshika's Password Manager")
window.config(padx=15, pady=15)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website :")
website_label.grid(column=0, row=1)

website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=1, row=1)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2,row=1)

email_label = Label(text="Email/ Username :")
email_label.grid(column=0, row=2)

email_input = Entry(width=40)
email_input.insert(0, "csendranshi@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password :")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

gen_pw_button = Button(text="Generate Password", width=15, command=gen_password)
gen_pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_to_file)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
