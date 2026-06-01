
from tkinter import *

window = Tk()


def submit():
    print("The temperature is "+str(scale.get())+" degrees Celsius.")


fire_image = PhotoImage(file='fire icon.png')
fire_label = Label(image=fire_image)
fire_label.pack()

scale = Scale(from_=100,
              to_=0,
              length=200,
              orient=VERTICAL,
              fg="#26b5bd",
              bg="black",
              troughcolor="#98f5fa",
              font=("Consolas",18),
              showvalue=0,
              resolution=1,
              tickinterval=20)
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

ice_image = PhotoImage(file='ice icon.png')
ice_label = Label(image=ice_image)
ice_label.pack()

submit_button = Button(text="submit",
                       command=submit)
submit_button.pack()
window.mainloop()
