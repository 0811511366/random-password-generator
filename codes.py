from tkinter import *

window = Tk()
window.title('Password Generator')
window.geometry('350x150')

greeting = Label(text="Hello User", fg='black', bg='white')
button = Button(text="Enter number below", bg='black', fg='white')
entry = Entry(fg="black", bg="white", width=50)
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text='thank you')
label.pack()

window.mainloop()