from tkinter import *
count = 0


def click():
    global count
    count += 1
    print(f"You clicked {count} times")


window = Tk()
window.geometry("800x600")
window.title("Buttons usage")
window.config(bg='green')

button1 = Button(window,
                 command=click,
                 text="Hello, User!",
                 fg="#00FF00",
                 bg="#000000",
                 activebackground="#000000",
                 activeforeground="#00FF00",
                 padx=20,
                 pady=20,
                 )
button1.pack()

window.mainloop()
