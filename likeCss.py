from tkinter import *

classLabel = lambda window: Label(window,
              text='Go ahead, Mr. Jostar',
              font=('Arial', 40, 'bold'),
              fg='#EEBC1D',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,)

classEntry = lambda window: Entry(window,
              font=('Arial', 30, 'bold'),
              fg='#EEBC1D',
              bg='black',)

menuClass = {'font':('Helvetica', 12), 
             'fg':'#EEBC1D', 
             'bg':'black', 
             'activeforeground':'#EEBC1D', 
             'activebackground':'#404040'}

buttonClass = lambda window, func, text: Button(window,
                text=text,
                command=func,
                font=('Comic Sans', 40),
                fg='#EEBC1D',
                bg='#0B0B45',
                activeforeground='#EEBC1D',
                activebackground='#253DA1',
                relief=RAISED,
                bd=10,
                padx=20,
                pady=20,)

warningLabel = lambda window: Label(window,
              text='Uncorrect input',
              font=('Arial', 20, 'bold'),
              fg='#8B0000',
              bg='#FF7F7F',
              relief=FLAT,
              bd=5,
              padx=5,
              pady=5,)