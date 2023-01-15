import tkinter

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="images/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = tkinter.Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)

login_label = tkinter.Label(text="Email/Username:")
login_label.grid(row=2, column=0)

login_input = tkinter.Entry(width=35)
login_input.grid(row=2, column=1, columnspan=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = tkinter.Entry(width=21)
password_input.grid(row=3, column=1)

generate_password_btn = tkinter.Button(text="Generate Password", width=13)
generate_password_btn.grid(row=3, column=2)

add_password_btn = tkinter.Button(text="Add", width=36)
add_password_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
