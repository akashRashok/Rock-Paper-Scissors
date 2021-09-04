from tkinter import *
import random

def play():
    user_pick=user_take.get()
    if user_pick==pick:
        Result.set('tie you both selected the same')
    elif user_pick=='rock' and pick=='scissor':
        Result.set('You won')
    elif user_pick=='paper' and pick=='rock':
        Result.set('You won')
    elif user_pick=='scissor' and pick=='paper':
        Result.set('You won')
    elif user_pick=='rock' and pick=='paper':
        Result.set('Computer won')
    elif user_pick=='paper' and pick=='scissors':
        Result.set('Computer won')
    elif user_pick=='scissors' and pick=='rock':
        Result.set('Computer won')
    else:
        Result.set('Invalid Input: choose rock, paper,or scissors')

def Reset():
    Result.set("")
    user_take.set("")

def Exit():
    root.destroy()

root=Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock, Paper, Scissors')
root.config(bg='seashell2')

Label(root,text='Rock, Paper, Scissors' ,font='arial 20 bold' ,bg='grey').pack()

user_take= StringVar()
Label(root,text='Choose one: Rock, Paper, Scissors' ,font='arial 15 bold' ,bg='grey').place(x=20,y=70)
Entry(root,font='arial 15', textvariable=user_take, bg='grey').place(x=85, y=140)

pick=random.randint(1,3)
if pick==1:
    pick='rock'
elif pick==2:
    pick='paper'
elif pick==3:
    pick='scissors'

Result=StringVar()

Entry(root,font='arial 10 bold', textvariable=Result, bg='grey',width = 50,).place(x=25, y = 250)
Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)
Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)
Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)
root.mainloop()
