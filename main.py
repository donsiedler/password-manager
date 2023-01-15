import tkinter

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="images/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()

window.mainloop()
