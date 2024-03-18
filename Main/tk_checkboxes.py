from tkinter import *

def display():
    if(x.get() == 1):
        print("You agree with our terms")
    else:
        print("You dont agree with our terms :(")


window = Tk()
window.geometry("800x600")
window.config(bg='wheat')

x = IntVar()
photo = PhotoImage(file='1.png')
check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           bg='black',
                           fg='#00FF00',
                           activeforeground='#00FF00',
                           activebackground='black',
                           font=('Arial', 20),
                           padx=25,
                           pady=10,
                           image=photo,
                           compound=LEFT)
check_button.pack()
window.mainloop()
