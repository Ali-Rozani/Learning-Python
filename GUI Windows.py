from tkinter import *
Window = Tk()
Window.geometry("420x350")
Window.title("Vast Reason")
def click():
    print("You clicked the button!")
Button =  Button(Window, text="Click Me!", command=click, font=('Arial',25))
Label = Label(Window, text="Hello!", font=('Arial',70, ' bold'), fg='#00FF00', bg='black', relief=RAISED, bd=50, padx=100, pady=100)
Label.place(x=100, y=100)
Button.pack()
Window.mainloop()