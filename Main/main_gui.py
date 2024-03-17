from tkinter import *

window = Tk()
window.geometry("800x600")
window.title("Alex's GUI")

icon = PhotoImage(file='1.png')
window.iconphoto(True, icon)
window.config(background="#4ecce6")

label1 = Label(window,
               text="do you even code?",
               font=('Arial', 40, 'bold'),
               fg='#00FF00',
               bg='black',
               relief=RAISED,
               bd=10,
               padx=20,
               pady=20,
               image=icon,
               compound='bottom')
label1.pack()

window.mainloop()