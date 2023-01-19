from tkinter import *
from PIL import Image, ImageTk
from random import randint
import random
window = Tk()
window.title("Matrix Rock, Paper and Scissors")
window.configure(background="Black")
image_rock1 = ImageTk.PhotoImage(Image.open("rock1.png"))
image_paper1 = ImageTk.PhotoImage(Image.open("paper1.png"))
image_scissor1 = ImageTk.PhotoImage(Image.open("scissorscom.png"))
image_rock2 = ImageTk.PhotoImage(Image.open("rock1.png"))
image_paper2 = ImageTk.PhotoImage(Image.open("paper1.png"))
image_scissors2 = ImageTk.PhotoImage(Image.open("scissorshum.png"))
label_player= Label(window, image=image_scissors2)
label_computer=Label(window, image=image_scissor1)
label_computer.grid(row=1,column =0)
label_player.grid(row=1, column=4)
computer_score=Label(window,text=0,font=('century gothic',50,"bold"),bg="black",fg="green")
player_score=Label(window,text=0,font=('century gothic',50,"bold"),bg="black",fg="green")
player_score.grid(row=1,column=3)
computer_score.grid(row=1, column=1)
print("Choose \n1)To play as Neo\n2)To play as Trinity\n3)To play as Morpheus")
ch=input()
choice=float(ch)
if choice==1:
    player_indicator = Label(window, font=("century gothic", 38, "bold"), text="NEO", bg="black", fg="green")
elif choice==2:
    player_indicator = Label(window, font=("century gothic", 38, "bold"), text="TRINITY", bg="black", fg="green")
else:
    player_indicator = Label(window, font=("century gothic", 38, "bold"), text="MORPHEUS", bg="black", fg="green")

print("\nChoose\n1)To play against Sentinels\n2)To play against Agent Smith\n3)To play against The Analyst")
chh=input()
villain=float(chh)
if villain==1:
    computer_indicator=Label(window,font=("century gothic",38,"bold"),text="SENTINELS",bg="black",fg="green")
elif villain==2:
    computer_indicator = Label(window, font=("century gothic", 38, "bold"), text="AGENT SMITH", bg="black", fg="green")
else:
    computer_indicator = Label(window, font=("century gothic", 38, "bold"), text="THE ANALYST", bg="black", fg="green")
computer_indicator.grid(row=0,column=1)
player_indicator.grid(row=0, column=3)
def msg_updation(a):
    final_message['text']=a
def computer_update():
    final= int(computer_score['text'])
    final+=1
    computer_score["text"]= str(final)

def player_update():
    final= int(player_score['text'])
    final+=1
    player_score["text"]= str(final)
def winner_check(p,c):
    if p==c :
        msg_updation("It's a tie")
    elif p=="rock":
            if c=="paper":
                msg_updation("Villain Wins !")
                computer_update()
            else:
                msg_updation("Hero Wins !")
                player_update()

    elif p=="paper":
         if c=="scissor":
             msg_updation("Villain Wins !")
             computer_update()
         else:
             msg_updation("Hero Wins !")
             player_update()

    elif p=="scissors":
        if c=="rock":
            msg_updation("Villain Wins !")
            computer_update()
        else:
            msg_updation("Hero Wins !")
            player_update()

    else:
        pass
to_select=["rock","paper","scissors"]

def choice_update(a):
    choice_computer=random.randint(0,2)
    if choice_computer==to_select[0]:
        label_computer.configure(image=image_rock2)
    elif choice_computer==to_select[1]:
        label_computer.configure(image=image_paper2)

    else:
        label_computer.configure(image=image_scissor1)

        if a=="rock":
            label_player.configure(image=image_rock1)

        elif a=="paper":
            label_player.configure(image=image_paper2)
        else:
            label_player.configure(image=image_scissors2)

        winner_check(a, choice_computer)




final_message=Label(window,font=("century gothic",35,"bold"),bg="black",fg="green")
final_message.grid(row=3,column=2)



button_rock=Button(window,width=15,height=5,text="ROCK",font=("Century Gothic",20,"bold"),bg="black",fg="green",command=lambda:choice_update("rock")).grid(row=2,column=1)
button_paper=Button(window,width=15,height=5,text="PAPER",font=("Century Gothic",20,"bold"),bg="black",fg="green",command=lambda:choice_update("paper")).grid(row=2,column=2)
button_scissor=Button(window,width=15,height=5,text="SCISSORS",font=("Century Gothic",20,"bold"),bg="black",fg="green",command=lambda:choice_update("scissors")).grid(row=2,column=3)


window.mainloop()


