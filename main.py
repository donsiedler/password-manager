from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, messagebox
from tkinter.constants import END

DEFAULT_EMAIL = "default_email@example.com"


# ---------------------------- SAVE DATA ------------------------------ #
def save():
    website = website_input.get()
    login = login_input.get()
    password = password_input.get()

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields emtpy!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                          f"Login: {login} \n"
                                                          f"Password: {password} \n"
                                                          f"Is it ok to save?")
    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {login} | {password}\n")

        website_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="images/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
login_label = Label(text="Email/Username:")
login_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="EW")
website_input.focus()
login_input = Entry(width=35)
login_input.grid(row=2, column=1, columnspan=2, sticky="EW")
login_input.insert(0, DEFAULT_EMAIL)
password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="EW")

# Buttons
generate_password_btn = Button(text="Generate Password")
generate_password_btn.grid(row=3, column=2, sticky="EW")
add_password_btn = Button(text="Add", width=36, command=save)
add_password_btn.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
