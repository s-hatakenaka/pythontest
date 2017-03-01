from tkinter import *
def bAaction():
    print('ありがとう')
def bBaction():
    print('いたい')
window = Tk()
buttonA = Button(window, text='押して',command=bAaction)
buttonB = Button(window, text='押さないでよ',command=bBaction)
buttonA.pack()
buttonB.pack()
