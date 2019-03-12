from tkinter import *
import random
import time

root=Tk()
root.geometry("800x800+0+0")
root.title("calculator")
#text_Input=float()
text_Input= StringVar()
operator=""


Tops=Frame(root,width=1600,height=50,bg="grey",relief=SUNKEN)
Tops.pack(side=TOP)

frame=Frame(root,width=300,height=700,relief=SUNKEN)
frame.pack(side=TOP)

lblInfo=Label(Tops,font=('arial',50,'bold'),text="CALCULATOR",fg="steel blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

txtDisplay=Entry(frame,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="grey", justify="right")
txtDisplay.grid(columnspan=4)

def btnclick(numbers):
    global operator
    operator=operator+ str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""


btn7=Button(frame,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="grey",command=lambda:btnclick(7)).grid(row=2,column=0)

btn8=Button(frame,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="grey",command=lambda:btnclick(8)).grid(row=2,column=1)

btn9=Button(frame,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="grey",command=lambda:btnclick(9)).grid(row=2,column=2)

Addition=Button(frame,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="grey",command=lambda:btnclick("+")).grid(row=2,column=3)
#========================================================================================================================================================
btn4=Button(frame,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="grey",command=lambda:btnclick(4)).grid(row=3,column=0)

btn5=Button(frame,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="grey",command=lambda:btnclick(5)).grid(row=3,column=1)

btn6=Button(frame,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="grey",command=lambda:btnclick(6)).grid(row=3,column=2)

Subtraction=Button(frame,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="grey",command=lambda:btnclick("-")).grid(row=3,column=3)
#==============================================================================================================================================================
btn1=Button(frame,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="grey",command=lambda:btnclick(1)).grid(row=4,column=0)

btn2=Button(frame,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="grey",command=lambda:btnclick(2)).grid(row=4,column=1)

btn3=Button(frame,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="grey",command=lambda:btnclick(3)).grid(row=4,column=2)

Multiply=Button(frame,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="grey",command=lambda:btnclick("*")).grid(row=4,column=3)
#==============================================================================================================================================================
btn0=Button(frame,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="grey",command=lambda:btnclick(0)).grid(row=5,column=0)

btnClear=Button(frame,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="C",bg="grey",command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(frame,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="grey",command=btnEqualsInput).grid(row=5,column=2)

Division=Button(frame,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="grey",command=lambda:btnclick("/")).grid(row=5,column=3)

root.mainloop()
