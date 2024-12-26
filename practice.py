from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

mixer.init()

mixer.music.load("images/kbc.mp3")
mixer.music.play(-1)

def select(event):
    callButton.place_forget()

    ProgressbarA.place_forget()
    ProgressbarB.place_forget()
    ProgressbarC.place_forget()
    ProgressbarD.place_forget()

    ProgressbarLabelA.place_forget()
    ProgressbarLabelB.place_forget()
    ProgressbarLabelC.place_forget()
    ProgressbarLabelD.place_forget()

    b=event.widget
    value=b["text"]

#================================== final win window =============================
    for i in range(15):
        if value==correct_answers[14]:
            winImage=PhotoImage(file="images/Picture15.png")
            winImageLabel=Label(rightframe,image=winImage,bg="black",height=750)
            winImageLabel.grid(row=0,column=0)

            def close():
                root2.destroy()
                root.destroy()
            
           
            def playagain():
                # wImage=PhotoImage(file="images/Picture0.png")
                # wImageLabel=Label(rightframe,image=wImage,bg="black",height=750)
                # wImageLabel.grid(row=0,column=0)
                # amountLabel.config(image=amountImage)   

                mixer.music.stop()
                mixer.music.load("images/kbc.mp3")
                mixer.music.play()           

                lifeline50Button.config(state=NORMAL,image=image50)
                audiencePoleButton.config(state=NORMAL,image=audiencePole)
                phoneLifelineButton.config(state=NORMAL,image=phoneImage)

                root2.destroy()
                questionArea.delete(1.0,END)
                questionArea.insert(END,questions[0])
 
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])  
    
                amountLabel.config(image=amountImage)   

            mixer.music.stop()
            mixer.music.load("images/kbcwon.mp3")
            mixer.music.play(-1) 
            
            root2=Toplevel()
            root2.overrideredirect(True)
            root2.config(bg="black")
            root2.geometry("500x400+190+150")
            root2.title("You Won")
            imgLabel=Label(root2,image=centerImage,bd=0)
            imgLabel.pack(pady=30)

            winlabel=Label(root2,text="You Won",font=("arial",40,"bold"),bg="black",fg="white")
            winlabel.pack()

            playagainButton=Button(root2,text="Play Again",font=("arial",20,"bold"),bg="black",fg="white",
                           bd=0,activebackground="black",activeforeground="white",command=playagain)
            playagainButton.pack()

            closeButton=Button(root2,text="Close",font=("arial",20,"bold"),bg="black",fg="white",
                           bd=0,activebackground="black",activeforeground="white",command=close)
            closeButton.pack()

            happyImage=PhotoImage(file="images/happy.png")
            happyLabel=Label(root2,image=happyImage,bg="black")
            happyLabel.place(x=30,y=280)
              
            happyLabel1=Label(root2,image=happyImage,bg="black")
            happyLabel1.place(x=400,y=280)

            root2.mainloop()
            break

#=========================Amount Images =======================================================
        if value==correct_answers[i]:
            questionArea.delete(1.0,END)
            questionArea.insert(END,questions[i+1])

            optionButton1.config(text=first_option[i+1])
            optionButton2.config(text=second_option[i+1])
            optionButton3.config(text=third_option[i+1])
            optionButton4.config(text=fourth_option[i+1])
            amountLabel.config(image=amountImages[i])

#=================================Try again and close area ========================================================
        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()

            def tryagain():
                mixer.music.stop()
                mixer.music.load("images/kbc.mp3")
                mixer.music.play()

                lifeline50Button.config(state=NORMAL,image=image50)
                audiencePoleButton.config(state=NORMAL,image=audiencePole)
                phoneLifelineButton.config(state=NORMAL,image=phoneImage)

                root1.destroy()
                questionArea.delete(1.0,END)
                questionArea.insert(END,questions[0])
 
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])  

                amountLabel.config(image=amountImage)             

            root1=Toplevel()
            root1.overrideredirect(True)
            root1.config(bg="black")
            root1.geometry("500x400+190+150")
            root1.title("You won 0 pounds")
            imgLabel=Label(root1,image=centerImage,bd=0)
            imgLabel.pack(pady=30)

            loselabel=Label(root1,text="You Lose",font=("arial",40,"bold"),bg="black",fg="white")
            loselabel.pack()

            tryagainButton=Button(root1,text="Try Again",font=("arial",20,"bold"),bg="black",fg="white",
                           bd=0,activebackground="black",activeforeground="white",command=tryagain)
            tryagainButton.pack()

            closeButton=Button(root1,text="Close",font=("arial",20,"bold"),bg="black",fg="white",
                           bd=0,activebackground="black",activeforeground="white",command=close)
            closeButton.pack()

            sadImage=PhotoImage(file="images/sad.png")
            sadLabel=Label(root1,image=sadImage,bg="black")
            sadLabel.place(x=30,y=280)
              
            sadLabel1=Label(root1,image=sadImage,bg="black")
            sadLabel1.place(x=400,y=280)

            root1.mainloop()
            break

#==============================life line 50 button =============================================
def lifeline50():
    mixer.music.pause()
    mixer.music.play(-1)
   
    lifeline50Button.config(image=image50X,state=DISABLED)

    if questionArea.get(1.0,'end-1c')==questions[0]:
        optionButton2.config(text="")
        optionButton4.config(text="")

    if questionArea.get(1.0,'end-1c')==questions[1]:
        optionButton1.config(text="")
        optionButton4.config(text="")

    if questionArea.get(1.0,'end-1c')==questions[2]:
        optionButton4.config(text="")
        optionButton3.config(text="")

    if questionArea.get(1.0,'end-1c')==questions[3]:
        optionButton1.config(text="")
        optionButton4.config(text="")

    if questionArea.get(1.0,'end-1c')==questions[4]:
        optionButton2.config(text="")
        optionButton4.config(text="")

    if questionArea.get(1.0,'end-1c')==questions[5]:
        optionButton1.config(text="")
        optionButton4.config(text="")

    if questionArea.get(1.0,'end-1c')==questions[6]:
        optionButton2.config(text="")
        optionButton3.config(text="")

    if questionArea.get(1.0,'end-1c')==questions[7]:
        optionButton1.config(text="")
        optionButton4.config(text="")

    if questionArea.get(1.0,'end-1c')==questions[8]:
        optionButton3.config(text="")
        optionButton4.config(text="")

    if questionArea.get(1.0,'end-1c')==questions[9]:
        optionButton2.config(text="")
        optionButton4.config(text="")

    if questionArea.get(1.0,'end-1c')==questions[10]:
        optionButton1.config(text="")
        optionButton4.config(text="")

    if questionArea.get(1.0,'end-1c')==questions[11]:
        optionButton2.config(text="")
        optionButton4.config(text="")

    if questionArea.get(1.0,'end-1c')==questions[12]:
        optionButton3.config(text="")
        optionButton4.config(text="")

    if questionArea.get(1.0,'end-1c')==questions[13]:
        optionButton2.config(text="")
        optionButton4.config(text="")

    if questionArea.get(1.0,'end-1c')==questions[14]:
        optionButton3.config(text="")
        optionButton4.config(text="")

#===================Audience pole function====================================
def audiencePoleLifeline():
    mixer.music.pause()
    mixer.music.play(-1)

    audiencePoleButton.config(image=audiencePoleX,state=DISABLED)

    ProgressbarA.place(x=660,y=260)
    ProgressbarB.place(x=700,y=260)
    ProgressbarC.place(x=740,y=260)
    ProgressbarD.place(x=780,y=260)

    ProgressbarLabelA.place(x=660,y=380)
    ProgressbarLabelB.place(x=700,y=380)
    ProgressbarLabelC.place(x=740,y=380)
    ProgressbarLabelD.place(x=780,y=380)
    
    if questionArea.get(1.0,"end-1c")==questions[0]:
        ProgressbarA.config(value=70)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=5)
        ProgressbarD.config(value=5)

    if questionArea.get(1.0,"end-1c")==questions[1]:
        ProgressbarA.config(value=30)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=10)

    if questionArea.get(1.0,"end-1c")==questions[2]:
        ProgressbarA.config(value=50)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=20)

    if questionArea.get(1.0,"end-1c")==questions[3]:
        ProgressbarA.config(value=10)
        ProgressbarB.config(value=80)
        ProgressbarC.config(value=3)
        ProgressbarD.config(value=7)

    if questionArea.get(1.0,"end-1c")==questions[4]:
        ProgressbarA.config(value=50)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=20)

    if questionArea.get(1.0,"end-1c")==questions[5]:
        ProgressbarA.config(value=10)
        ProgressbarB.config(value=70)
        ProgressbarC.config(value=5)
        ProgressbarD.config(value=15)

    if questionArea.get(1.0,"end-1c")==questions[6]:
        ProgressbarA.config(value=70)
        ProgressbarB.config(value=10)
        ProgressbarC.config(value=5)
        ProgressbarD.config(value=15)

    if questionArea.get(1.0,"end-1c")==questions[7]:
        ProgressbarA.config(value=10)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=35)
        ProgressbarD.config(value=5)

    if questionArea.get(1.0,"end-1c")==questions[8]:
        ProgressbarA.config(value=50)
        ProgressbarB.config(value=5)
        ProgressbarC.config(value=15)
        ProgressbarD.config(value=30)

    if questionArea.get(1.0,"end-1c")==questions[9]:
        ProgressbarA.config(value=50)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=20)

    if questionArea.get(1.0,"end-1c")==questions[10]:
        ProgressbarA.config(value=5)
        ProgressbarB.config(value=10)
        ProgressbarC.config(value=80)
        ProgressbarD.config(value=5)

    if questionArea.get(1.0,"end-1c")==questions[11]:
        ProgressbarA.config(value=65)
        ProgressbarB.config(value=5)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=20)

    if questionArea.get(1.0,"end-1c")==questions[12]:
        ProgressbarA.config(value=5)
        ProgressbarB.config(value=80)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=5)

    if questionArea.get(1.0,"end-1c")==questions[13]:
        ProgressbarA.config(value=50)
        ProgressbarB.config(value=10)
        ProgressbarC.config(value=30)
        ProgressbarD.config(value=10)

    if questionArea.get(1.0,"end-1c")==questions[14]:
        ProgressbarA.config(value=75)
        ProgressbarB.config(value=5)
        ProgressbarC.config(value=15)
        ProgressbarD.config(value=5)

#====================Phone life line ===============================
def phoneLifeline():
    mixer.music.pause()
    mixer.music.load("images/calling.mp3")
    mixer.music.play()

    callButton.place(x=70,y=260)
    phoneLifelineButton.config(image=phoneImageX,state=DISABLED)

def phoneclick():
    for i in range(15):
        if questionArea.get(1.0,"end-1c")==questions[i]:
            engine.say(f"The answer is {correct_answers[i]}")
            engine.runAndWait()

    mixer.music.load("images/kbc.mp3")
    mixer.music.play(-1)

correct_answers = [
    "Paris", "Mars", "H2O", "Japan", "Shakespeare",
    "Nile", "Avocado", "Two", "Africa", "DaVinci",
    "Nitrogen", "Everest", "BlueWhale", "Heart", "Hockey"
]

questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is the chemical symbol for water?",
    "Which country is known as the Land of the Rising Sun?",
    "Who wrote the play 'Romeo and Juliet'?",
    "Which is the longest river in the world?",
    "What is the main ingredient in guacamole?",
    "What is the smallest prime number?",
    "Which continent is known as the 'Dark Continent'?",
    "Who painted the Mona Lisa?",
    "What is the most abundant gas in Earth's atmosphere?",
    "Which is the tallest mountain in the world?",
    "What is the largest mammal in the world?",
    "Which organ is responsible for pumping blood in the human body?",
    "What is the national sport of Canada?"
]

first_option = [
    "Paris", "Earth", "H2O", "China", "Shakespeare",
    "Amazon", "Avocado", "Zero", "Africa", "DaVinci",
    "Oxygen", "Everest", "Elephant", "Heart", "Hockey"
]

second_option = [
    "London", "Mars", "O2", "Japan", "Dickens",
    "Nile", "Potato", "Two", "Asia", "VanGogh",
    "Helium", "K2", "BlueWhale", "Brain", "Cricket"
]

third_option= [
    "Berlin", "Jupiter", "CO2", "India", "Hemingway",
    "Yangtze", "Tomato", "Three", "Australia", "Picasso",
    "Nitrogen", "Denali", "Shark", "Lungs", "Soccer"
]

fourth_option = [
    "Madrid", "Saturn", "NaCl", "Thailand", "Tolkien",
    "Mississippi", "Cucumber", "One", "Europe", "Rembrandt",
    "Neon", "Kilimanjaro", "Giraffe", "Liver", "Baseball"
]


root = Tk()

root.geometry("2000x1000+0+0")
root.title("Who wants to be a millionaire")
root.config(bg="black")

#=====================Frames==============================
leftframe = Frame(root,bg="black",padx=140)
leftframe.grid(row=0, column=0)

topframe = Frame(leftframe,bg="black",pady=15)
topframe.grid(row=0, column=0)

centerframe = Frame(leftframe,bg="black",pady=15)
centerframe.grid(row=1, column=0)

bottomframe = Frame(leftframe)
bottomframe.grid(row=2, column=0)

rightframe = Frame(root,bg="black",pady=25,padx=100)
rightframe.grid(row=0, column=1)

#==============================50-50 life line===============================================================
image50 = PhotoImage(file="images/50-50.png")
image50X = PhotoImage(file="images/50-50-X.png")


lifeline50Button = Button(topframe,image=image50,bg="black",activebackground="black",width=180,height=80,bd=0,
                   command=lifeline50)
lifeline50Button.grid(row=0,column=0)

#==============================audience pole life line==============================================
audiencePole = PhotoImage(file="images/audiencePole.png")
audiencePoleX = PhotoImage(file="images/audiencePoleX.png")

audiencePoleButton=Button(topframe,image=audiencePole,bg="black",activebackground="black",width=180,height=80,bd=0,
                   command=audiencePoleLifeline)
audiencePoleButton.grid(row=0,column=1)

#===========================phone a friend life line ============================================
phoneImage = PhotoImage(file="images/phoneAFriend.png")
phoneImageX = PhotoImage(file="images/phoneAFriendX.png")

phoneLifelineButton=Button(topframe,image=phoneImage,bg="black",activebackground="black",width=180,height=80,bd=0
                 ,command=phoneLifeline)
phoneLifelineButton.grid(row=0,column=2)

#===================================calling====================================================
callimage=PhotoImage(file="images/phone.png")

callButton=Button(root,image=callimage,bd=0,bg="black",activebackground="black",cursor="hand2"
           ,command=phoneclick)

#=============================center image logo ============================================
centerImage = PhotoImage(file="images/center.png")
LogoLabel=Label(centerframe,image=centerImage,bg="black",width=300,height=200)
LogoLabel.grid(row=0,column=0)

#===============================money chart ===============================================
amountImage=PhotoImage(file="images/Picture0.png")
amountImage1=PhotoImage(file="images/Picture1.png")
amountImage2=PhotoImage(file="images/Picture2.png")
amountImage3=PhotoImage(file="images/Picture3.png")
amountImage4=PhotoImage(file="images/Picture4.png")
amountImage5=PhotoImage(file="images/Picture5.png")
amountImage6=PhotoImage(file="images/Picture6.png")
amountImage7=PhotoImage(file="images/Picture7.png")
amountImage8=PhotoImage(file="images/Picture8.png")
amountImage9=PhotoImage(file="images/Picture9.png")
amountImage10=PhotoImage(file="images/Picture10.png")
amountImage11=PhotoImage(file="images/Picture11.png")
amountImage12=PhotoImage(file="images/Picture12.png")
amountImage13=PhotoImage(file="images/Picture13.png")
amountImage14=PhotoImage(file="images/Picture14.png")
amountImage15=PhotoImage(file="images/Picture15.png")

amountImages = [amountImage1,amountImage2,amountImage3,amountImage4,amountImage5,amountImage6,amountImage7,amountImage8,amountImage9,
amountImage10,amountImage11,amountImage12,amountImage13,amountImage14,amountImage15]

amountLabel=Label(rightframe,image=amountImage,bg="black",height=750)
amountLabel.grid(row=0,column=0)

#====================================layout image =======================================
layoutImage=PhotoImage(file="images/lay.png")
layoutLabel=Label(bottomframe,image=layoutImage,bg="black")
layoutLabel.grid(row=0,column=0)

#===================================question area =====================================
questionArea=Text(bottomframe,font=("arial",18,"bold"),width=34,height=2,wrap="word",bg="black",fg="white",bd=0)
questionArea.place(x=70,y=10)
questionArea.insert(END,questions[0])

LabelA=Label(bottomframe,text="A:",bg="black",fg="white",font=("arial",16,"bold"))
LabelA.place(x=60,y=110)

#=====================================Option Buttons =================================
optionButton1=Button(bottomframe,text=first_option[0],bg="black",fg="white",font=("arial",18,"bold"),bd=0,activebackground="black",activeforeground="white",cursor="hand2")
optionButton1.place(x=100,y=100)

LabelB=Label(bottomframe,text="B:",bg="black",fg="white",font=("arial",16,"bold"))
LabelB.place(x=340,y=110)

optionButton2=Button(bottomframe,text=second_option[0],bg="black",fg="white",font=("arial",18,"bold"),bd=0,activebackground="black",activeforeground="white",cursor="hand2")
optionButton2.place(x=380,y=100)

LabelC=Label(bottomframe,text="C:",bg="black",fg="white",font=("arial",16,"bold"))
LabelC.place(x=60,y=190)

optionButton3=Button(bottomframe,text=third_option[0],bg="black",fg="white",font=("arial",18,"bold"),bd=0,activebackground="black",activeforeground="white",cursor="hand2")
optionButton3.place(x=100,y=180)

LabelD=Label(bottomframe,text="D:",bg="black",fg="white",font=("arial",16,"bold"))
LabelD.place(x=340,y=190)

optionButton4=Button(bottomframe,text=fourth_option[0],bg="black",fg="white",font=("arial",18,"bold"),bd=0,activebackground="black",activeforeground="white",cursor="hand2")
optionButton4.place(x=380,y=180)

#========================Graphs========================================
ProgressbarA= Progressbar(root,orient=VERTICAL,length=120)
ProgressbarB= Progressbar(root,orient=VERTICAL,length=120)
ProgressbarC= Progressbar(root,orient=VERTICAL,length=120)
ProgressbarD= Progressbar(root,orient=VERTICAL,length=120)

ProgressbarLabelA=Label(root,text="A",font=("arial",20,"bold"),bg="black",fg="white")
ProgressbarLabelB=Label(root,text="B",font=("arial",20,"bold"),bg="black",fg="white")
ProgressbarLabelC=Label(root,text="C",font=("arial",20,"bold"),bg="black",fg="white")
ProgressbarLabelD=Label(root,text="D",font=("arial",20,"bold"),bg="black",fg="white")

optionButton1.bind("<Button-1>",select)
optionButton2.bind("<Button-1>",select)
optionButton3.bind("<Button-1>",select)
optionButton4.bind("<Button-1>",select)

root.mainloop()