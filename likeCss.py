from tkinter import *
from tkinter import ttk

classLabel = lambda window, text: Label(window,
              text=text,
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
              bg='black',
              disabledbackground='#A9A9A9',
              disabledforeground='#A9A9A9')

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
              fg='#404040',
              bg='#404040',
              relief=FLAT,
              bd=5,
              padx=5,
              pady=5,
              disabledforeground='#404040',)
              

progressbarClass = lambda window: ttk.Progressbar(window, 
                    orient ="horizontal", 
                    length = 200,
                    mode ="determinate",
                    takefocus=2)