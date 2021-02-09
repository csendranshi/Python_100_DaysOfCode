from tkinter import *

window = Tk()
window.title("I am Bored")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a funny Label", font=("Arial", 24))
my_label.pack(expand= True)

def  button_clicked():

    my_label["text"] = "Button Clicked"
    new_text = input.get()
    my_label.config(text=new_text)
    # my_label.config(text="")

button = Button(text="Click Me", command= button_clicked)
button.pack()

input = Entry(width=15)
input.pack()
answer = input.get()

window.mainloop()