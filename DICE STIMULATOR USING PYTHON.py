from tkinter import*
import random


#window creation and configuration
window = Tk()

window.configure(bg = "white")
window.geometry("650x550")
window.title("DICE STIMULATOR")
window.resizable(0,0)

#defining the rolling function
def rolling_of_dice():
    dots = ['\u2680', '\u2681', '\u2682', '\u2683','\u2684', '\u2685']
    label.configure(
        text = f'{random.choice(dots)}{random.choice(dots)}')
    label.pack()

#adding buttons and position   
roll_button = Button(window,text = "ROLL", width = 15,height =3,font = 16 ,bg = "violet" ,bd=2,command = rolling_of_dice)
roll_button.pack(padx=12,pady=17)
label=Label(window,font=("times",270),bg="black",fg="violet")


window.mainloop()
