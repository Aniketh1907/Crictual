import tkinter
from tkinter import *
import tkinter.messagebox
import random
import tkinter.simpledialog as sm
import tkinter.messagebox as mb
import pyttsx3 # pip install pyttsx3

root=Tk()
score=0
newscore = 0
def batting():


    engine = pyttsx3.init()

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()




    def decide(num):
        
        comp_gen = random.randint(0,6)
        if comp_gen==num:
            speak("You are out,Better luck next time")
            print("Out")
            mylabelq=Label(btnrow1,text="You lost",font="Verdana 24", relief=GROOVE, bd=0,fg="white", bg="#333333")
            mylabelq.pack()
            tkinter.messagebox.showinfo("You lost", "You got out better luck next time")
            root.destroy()

        else:
            print("")
            global score 
            score = score+num
            
            
    def winner(comp_score,score):
        if comp_score<=score:
            speak("You Won the game!!")
            print("You won")
            mylabelw=Label(btnrow1,text="You won",font="Verdana 24", relief=GROOVE, bd=0,fg="white", bg="#333333")
            mylabelw.pack()
            tkinter.messagebox.showinfo("Champion", "Hurray!!!You won the mach")
            root.destroy()
        else:
            pass
    
        
    def btn1_clicked():
        disp.delete(0, END)
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        decide(1)
        global fnum
        fnum=score
        try:
            disp.insert(0, score)
        except:
            pass
        winner(comp_score,score)


    def btn2_clicked():
        disp.delete(0, END)
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        decide(2)
        try:
            disp.insert(0, score)
        except:
            pass
        winner(comp_score,score)

    def btn3_clicked():
        disp.delete(0, END)
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        decide(3)
        try:
            disp.insert(0, score)
        except:
            pass
        winner(comp_score,score)

    def btn4_clicked():
        disp.delete(0, END)
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        decide(4)
        try:
            disp.insert(0, score)
        except:
            pass
        winner(comp_score,score)

    def btn5_clicked():
        disp.delete(0, END)
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        decide(5)
        try:
            disp.insert(0, score)
        except:
            pass
        winner(comp_score,score)
    def btn6_clicked():
        disp.delete(0, END)
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        decide(6)
        try:
            disp.insert(0, score)
        except:
            pass
        winner(comp_score,score)
    def key_event(*args):
        if disp.get() == '0':
            disp.delete(0, END)       
        



    root=Tk()
    #size of the window 
    root.geometry("700x500+400+400")
    root.resizable(0,0)

    #root.configure(bg="#292929")
    root.configure(bg="#141414")
    btnrow1 =Frame(root,bg="#ffffff")
    btnrow1.pack(expand = True,fill ="both")

    btnrow3 =Frame(root,bg="#ff00ff")
    btnrow3.pack(expand = True,fill ="both")
    btnrow4 =Frame(root,bg="#ff00ff")
    btnrow4.pack(expand = True,fill ="both")
    root.title("Virtual Cricket")
    mylabel = Label(btnrow1,text="The Virtual Cricket 2.0",font="Verdana 24", relief=GROOVE, bd=0,fg="white", bg="#333333")
    mylabel.pack()
    comp_score = random.randint(1,100)

    mylabel = Label(btnrow1,font="Verdana 24", relief=GROOVE, bd=0,fg="white", bg="#333333")
    mylabel.pack()


    mylabel = Label(btnrow1,text="Target is:"+str(comp_score),font="Verdana 24", relief=GROOVE, bd=0,fg="white", bg="#333333")
    mylabel.pack()

    displ = Entry(btnrow1, font="Verdana 20", fg="black", bd=0, justify=LEFT,text="enter your name:")
    displ.pack(expand=TRUE, fill=BOTH)
    player = str(displ)
    player_name = ''.join([i for i in player if not i.isdigit()])
    mylabel_1 = Label(text="Welcome"+player_name)
    mylabel.pack()



    speak("Welcome back sir!")

    disp = Entry(root, font="Verdana 20", fg="black", bg="#ffffff", bd=0, justify=RIGHT, insertbackground="#abbab1")
    disp.bind("<Key-1>", key_event)
    disp.bind("<Key-2>", key_event)
    disp.bind("<Key-3>", key_event)
    disp.bind("<Key-4>", key_event)
    disp.bind("<Key-5>", key_event)
    disp.bind("<Key-6>", key_event)
    disp.insert(0, '0')
    disp.focus_set()
    disp.pack(expand=TRUE, fill=BOTH)








    btn1_clicked = Button(btnrow3, text="1", font="Segoe 20", relief=GROOVE, bd=0,fg="white", bg="#333333",command= btn1_clicked)
    btn1_clicked.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn2_clicked = Button(btnrow3, text="2", font="Segoe 20", relief=GROOVE, bd=0,fg="white", bg="#333333",command=btn2_clicked)
    btn2_clicked.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn3_clicked = Button(btnrow3, text="3", font="Segoe 20", relief=GROOVE, bd=0,fg="white", bg="#333333",command=btn3_clicked)
    btn3_clicked.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn4_clicked = Button(btnrow3, text="4", font="Segoe 20", relief=GROOVE, bd=0,fg="white", bg="#333333",command=btn4_clicked)
    btn4_clicked.pack(side=LEFT, expand=TRUE, fill=BOTH)
    btn5_clicked = Button(btnrow3, text="5", font="Segoe 20", relief=GROOVE, bd=0,fg="white", bg="#333333",command=btn5_clicked)
    btn5_clicked.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn6_clicked = Button(btnrow3, text="6", font="Segoe 20", relief=GROOVE, bd=0,fg="white", bg="#333333",command=btn6_clicked)
    btn6_clicked.pack(side=LEFT, expand=TRUE, fill=BOTH)

    pi_btn = Button(btnrow4, text="Batting", font="Segoe 20", relief=GROOVE, bd=0,fg="white", bg="#ff781f")
    pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)



    root.mainloop()

def bowling():
    
    
    engine = pyttsx3.init()

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()




    def decide(num):
        
        comp_gen = random.randint(1,6)
        if comp_gen==num:
            speak("Its out you won the match")
            print("Out")
            mylabelq=Label(btnrow1,text="You won",font="Verdana 24", relief=GROOVE, bd=0,fg="white", bg="#333333")
            mylabelq.pack()
            tkinter.messagebox.showinfo("You won", "Biryani time")
            root.destroy()

        else:
            print("")
            global score 
            score = score+comp_gen
            
    def winner(comp_score,score):
        if comp_score<=score:
            speak("You Won the game!!")
            print("You won")
            mylabelw=Label(btnrow1,text="You won",font="Verdana 24", relief=GROOVE, bd=0,fg="white", bg="#333333")
            mylabelw.pack()
            tkinter.messagebox.showinfo("Champion", "Hurray!!!You won the mach")
            root.destroy()
        else:
            pass
    
        
    def btn1_clicked():
        disp.delete(0, END)
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        decide(1)
        global fnum
        fnum=score
        try:
            disp.insert(0, score)
        except:
            pass
        winner(comp_score,score)


    def btn2_clicked():
        disp.delete(0, END)
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        decide(2)
        try:
            disp.insert(0, score)
        except:
            pass
        winner(comp_score,score)

    def btn3_clicked():
        disp.delete(0, END)
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        decide(3)
        try:
            disp.insert(0, score)
        except:
            pass
        winner(comp_score,score)

    def btn4_clicked():
        disp.delete(0, END)
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        decide(4)
        try:
            disp.insert(0, score)
        except:
            pass
        winner(comp_score,score)

    def btn5_clicked():
        disp.delete(0, END)
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        decide(5)
        try:
            disp.insert(0, score)
        except:
            pass
        winner(comp_score,score)
    def btn6_clicked():
        disp.delete(0, END)
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        decide(6)
        try:
            disp.insert(0, score)
        except:
            pass
        winner(comp_score,score)
    def key_event(*args):
        if disp.get() == '0':
            disp.delete(0, END)       
        



    root=Tk()
    #size of the window 
    root.geometry("700x500+400+400")
    root.resizable(0,0)

    #root.configure(bg="#292929")
    root.configure(bg="#141414")
    btnrow1 =Frame(root,bg="#ffffff")
    btnrow1.pack(expand = True,fill ="both")

    btnrow3 =Frame(root,bg="#ff00ff")
    btnrow3.pack(expand = True,fill ="both")
    btnrow4 =Frame(root,bg="#ff00ff")
    btnrow4.pack(expand = True,fill ="both")
    root.title("Virtual Cricket")
    mylabel = Label(btnrow1,text="The Virtual Cricket 2.0",font="Verdana 24", relief=GROOVE, bd=0,fg="white", bg="#333333")
    mylabel.pack()
    comp_score = random.randint(1,100)

    mylabel = Label(btnrow1,font="Verdana 24", relief=GROOVE, bd=0,fg="white", bg="#333333")
    mylabel.pack()


    mylabel = Label(btnrow1,text="Target is:"+str(comp_score),font="Verdana 24", relief=GROOVE, bd=0,fg="white", bg="#333333")
    mylabel.pack()

    displ = Entry(btnrow1, font="Verdana 20", fg="black", bd=0, justify=LEFT,text="enter your name:")
    displ.pack(expand=TRUE, fill=BOTH)
    player = str(displ)
    player_name = ''.join([i for i in player if not i.isdigit()])
    mylabel_1 = Label(text="Welcome"+player_name)
    mylabel.pack()



    speak("Welcome back sir!")

    disp = Entry(root, font="Verdana 20", fg="black", bg="#ffffff", bd=0, justify=RIGHT, insertbackground="#abbab1")
    disp.bind("<Key-1>", key_event)
    disp.bind("<Key-2>", key_event)
    disp.bind("<Key-3>", key_event)
    disp.bind("<Key-4>", key_event)
    disp.bind("<Key-5>", key_event)
    disp.bind("<Key-6>", key_event)
    disp.insert(0, '0')
    disp.focus_set()
    disp.pack(expand=TRUE, fill=BOTH)








    btn1_clicked = Button(btnrow3, text="1", font="Segoe 20", relief=GROOVE, bd=0,fg="white", bg="#333333",command= btn1_clicked)
    btn1_clicked.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn2_clicked = Button(btnrow3, text="2", font="Segoe 20", relief=GROOVE, bd=0,fg="white", bg="#333333",command=btn2_clicked)
    btn2_clicked.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn3_clicked = Button(btnrow3, text="3", font="Segoe 20", relief=GROOVE, bd=0,fg="white", bg="#333333",command=btn3_clicked)
    btn3_clicked.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn4_clicked = Button(btnrow3, text="4", font="Segoe 20", relief=GROOVE, bd=0,fg="white", bg="#333333",command=btn4_clicked)
    btn4_clicked.pack(side=LEFT, expand=TRUE, fill=BOTH)
    btn5_clicked = Button(btnrow3, text="5", font="Segoe 20", relief=GROOVE, bd=0,fg="white", bg="#333333",command=btn5_clicked)
    btn5_clicked.pack(side=LEFT, expand=TRUE, fill=BOTH)

    btn6_clicked = Button(btnrow3, text="6", font="Segoe 20", relief=GROOVE, bd=0,fg="white", bg="#333333",command=btn6_clicked)
    btn6_clicked.pack(side=LEFT, expand=TRUE, fill=BOTH)

    pi_btn = Button(btnrow4, text="Bowling", font="Segoe 20", relief=GROOVE, bd=0,fg="white", bg="#ff781f")
    pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)



    root.mainloop()


#Welcome the User
mb.showinfo("Welcome", "We are very delighted to welcome you")
#Get user info
name = sm.askstring("Name:","Enter username:")
select = sm.askstring("odd or even","type odd or Even: ")
if(select=="odd" or select=="Odd"):
    num = sm.askinteger("0-6","Enter a number between 0 to 6: ")
    comp = random.randint(0,6)
    print(num)
    print(comp)
    if ((num+comp)%2==1):
        selecting = sm.askstring("bat or ball","What would you like to do: ")
        if(selecting=="bat" or selecting=="Bat"):
            batting()
        elif(selecting=="bowl" or selecting=="Bowl"):
            bowling()
    else:
        comp_selecting= random.randint(1,2)
        if(comp_selecting==1):
            batting()
        else:
            bowling()
  
     
elif(select=="even" or select=="Even"):
    num = sm.askinteger("0-6","Enter a number between 0 to 6: ")
    comp = random.randint(0,6)
    if ((num+comp)%2==0):
        selecting = sm.askstring("bat or bowl","What would you like to do: ")
        if(selecting=="bat" or selecting=="Bat"):
            batting()
        elif(selecting=="bowl" or selecting=="Bowl"):
            bowling()
    else:
        comp_selecting= random.randint(1,2)
        if(comp_selecting==1):
            batting()
            
        else:
            bowling()
           
  
root.mainloop()