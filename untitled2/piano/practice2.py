import pygame
import sys
from tkinter import *
from msvcrt import getch

pygame.init()


#검정건반 음 설정
def piano_Cs():
    num1.set("C#3")
    pygame.mixer.init()
    sound = pygame.mixer.Sound(r"C#3.wav")
    sound.play()
    return
def piano_Ds():
    num1.set("D#3")
    pygame.mixer.init()
    sound = pygame.mixer.Sound(r"D#3.wav")
    sound.play()
    return
def piano_Fs():
    num1.set("F#3")
    pygame.mixer.init()
    sound = pygame.mixer.Sound(r"F#3.wav")
    sound.play()
    return
def piano_Gs():
    num1.set("G#3")
    pygame.mixer.init()
    sound = pygame.mixer.Sound(r"G#3.wav")
    sound.play()
    return
def piano_As():
    num1.set("A#3")
    pygame.mixer.init()
    sound = pygame.mixer.Sound(r"A#3.wav")
    sound.play()
    return
def piano_Cs1():
    num1.set("C#4")
    pygame.mixer.init()
    sound = pygame.mixer.Sound(r"C#4.wav")
    sound.play()
    return
def piano_Ds1():
    num1.set("D#4")
    pygame.mixer.init()
    sound = pygame.mixer.Sound(r"D#4.wav")
    sound.play()
    return


#흰건반 음 설정
def piano_C():
    num1.set("C3")
    pygame.mixer.init()
    sound = pygame.mixer.Sound(r"C3.wav")
    sound.play()
def piano_D():
    num1.set("D3")
    sound = pygame.mixer.Sound(r"D3.wav")
    sound.play()
    return
def piano_E():
    num1.set("E3")
    sound = pygame.mixer.Sound(r"E3.wav")
    sound.play()
    return
def piano_F():
    num1.set("F3")
    sound = pygame.mixer.Sound(r"F3.wav")
    sound.play()
    return
def piano_G():
    num1.set("G3")
    sound = pygame.mixer.Sound(r"G3.wav")
    sound.play()
    return
def piano_A():
    num1.set("A3")
    sound = pygame.mixer.Sound(r"A3.wav")
    sound.play()
    return
def piano_B():
    num1.set("B3")
    sound = pygame.mixer.Sound(r"B3.wav")
    sound.play()
    return
def piano_C1():
    num1.set("C4")
    sound = pygame.mixer.Sound(r"C4.wav")
    sound.play()
    return
def piano_D1():
    num1.set("D4")
    pygame.mixer.init()
    sound = pygame.mixer.Sound(r"D4.wav")
    sound.play()
    return
def piano_E1():
    num1.set("E4")
    pygame.mixer.init()
    sound = pygame.mixer.Sound(r"E4.wav")
    sound.play()
    return

root = Tk()
frame = Frame(root)

root.title("룰루♬")

num1=StringVar()

topframe = Frame(root)
topframe.pack(side = TOP)
txtDisplay=Entry(frame,textvariable = num1,bd=20,insertwidth =1,font=30,justify='center',width=4,)
txtDisplay.pack(side = TOP)

#검정건반 버튼설정 button0=여백공간
button1 = Button(topframe, padx=6, height=6, pady=6, bd=8, text="도# ", bg="black", fg="white", command=piano_Cs)
button1.pack(side =LEFT)
button0 = Button(topframe, state=DISABLED, height = 7, width=1, padx=0, pady=0, relief=RIDGE)
button0.pack(side=LEFT)
button2 = Button(topframe, padx=6, pady=6, height=6, bd=8, text="레# ", bg="black", fg="white", command=piano_Ds)
button2.pack(side =LEFT)
button0 = Button(topframe, state=DISABLED, height = 7, width=8, padx=0, pady=0, relief=RIDGE)
button0.pack(side = LEFT)
button3 = Button(topframe,padx=6, pady=6, height=6, bd = 8, text="파# ", bg="black", fg="white", command=piano_Fs)
button3.pack(side = LEFT)
button0 = Button(topframe, state=DISABLED, height = 7, width=1, padx=0, pady=0, relief=RIDGE)
button0.pack(side = LEFT)
button4 = Button(topframe, padx=6, pady=6, height=6, bd=8, text="솔# ", bg="black", fg="white", command=piano_Gs)
button4.pack(side = LEFT)
button0 = Button(topframe, state=DISABLED, height = 7, width=1, padx=0, pady=0, relief=RIDGE)
button0.pack(side=LEFT)
button2 = Button(topframe, padx=6, pady=6, height=6, bd=8, text="라# ", bg="black", fg="white", command=piano_As)
button2.pack(side = LEFT)
button0 = Button(topframe, state=DISABLED, height = 7, width=8, padx=0, pady=0, relief=RIDGE)
button0.pack(side = LEFT)
button3 = Button(topframe, padx=6, pady=6, height=6, bd=8, text="도#1", bg="black", fg="white", command=piano_Cs1)
button3.pack(side = LEFT)
button0 = Button(topframe, state=DISABLED, height=7, width=1, padx=0, pady=0, relief=RIDGE)
button0.pack(side = LEFT)
button4 = Button(topframe, padx=6, pady=6, height=6, bd=8, text="레#1", bg="black", fg="white", command=piano_Ds1)
button4.pack(side = LEFT)

frame1 = Frame(root)
frame1.pack( side = TOP )

#흰건반 버튼설정
button100 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="도", fg="black", command=piano_C)
button100.pack( side = LEFT )
button200 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="레", fg="black", command=piano_D)
button200.pack( side = LEFT )
button300 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="미", fg="black", command=piano_E)
button300.pack( side = LEFT )
button400 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="파", fg="black", command=piano_F)
button400.pack( side = LEFT )
button500 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="솔", fg="black", command=piano_G)
button500.pack( side = LEFT )
button600 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="라", fg="black", command=piano_A)
button600.pack( side = LEFT )
button700 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="시", fg="black", command=piano_B)
button700.pack( side = LEFT )
button800 = Button(frame1, padx=14, pady=16, bd=8, height=8, text="도1", fg="black", command=piano_C1)
button800.pack( side = LEFT )
button900 = Button(frame1, padx=14, pady=16, bd=8, height=8, text="레1", fg="black", command=piano_D1)
button900.pack( side = LEFT )
button1000 = Button(frame1, padx=14, pady=16, bd=8, height=8, text="미1", fg="black", command=piano_E1)
button1000.pack( side = LEFT )


frame.focus_set() #키보드, 마우스 이벤트를 동시에 처리
frame.pack()

#키보드 건반 함수 정의
def a(event) :
    piano_C()
def s(event) :
    piano_D()
def d(event) :
    piano_E()
def f(event) :
    piano_F()
def g(event) :
    piano_G()
def h(event) :
    piano_A()
def j(event) :
    piano_B()
def k(event) :
    piano_C1()
def l(event) :
    piano_D1()
def d2(event) :
    piano_E1()

#검정건반!
def w(event) :
    piano_Cs()
def e(event) :
    piano_Ds()
def t(event) :
    piano_Fs()
def y(event) :
    piano_Gs()
def u(event) :
    piano_As()
def o(event) :
    piano_Cs1()
def p(event) :
    piano_Ds1()




#키보드 인식 설정
frame.bind("<a>", a)
frame.bind("<s>", s)
frame.bind("<d>", d)
frame.bind("<f>", f)
frame.bind("<g>", g)
frame.bind("<h>", h)
frame.bind("<j>", j)
frame.bind("<k>", k)
frame.bind("<l>",l)
frame.bind("<;>", d2)

frame.bind("<w>", w)
frame.bind("<e>", e)
frame.bind("<t>", t)
frame.bind("<y>", y)
frame.bind("<u>", u)
frame.bind("<o>", o)
frame.bind("<p>", p)

root.mainloop()
