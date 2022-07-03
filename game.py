from tkinter import *
import random

root = Tk()
root.title("RPS")
width = 620
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#9b59b6")

player_rock = PhotoImage(file='C:/Users/hp/RPS/Project_1/rock-user.png')
player_paper = PhotoImage(file='C:/Users/hp/RPS/Project_1/paper-user.png')
player_scissors = PhotoImage(file='C:/Users/hp/RPS/Project_1/scissors-user.png')
comp_rock = PhotoImage(file='C:/Users/hp/RPS/Project_1/rock-comp.png')
comp_paper = PhotoImage(file='C:/Users/hp/RPS/Project_1/paper-comp.png')
comp_scissors = PhotoImage(file='C:/Users/hp/RPS/Project_1/scissors-comp.png')
start = PhotoImage(file='C:/Users/hp/RPS/Project_1/start.png').subsample(4)
win = PhotoImage(file='C:/Users/hp/RPS/Project_1/win.png').subsample(4)
draw = PhotoImage(file='C:/Users/hp/RPS/Project_1/draw.png').subsample(4)
lose = PhotoImage(file='C:/Users/hp/RPS/Project_1/lose.png').subsample(4)

player_img = Label(root, image=player_rock, bg='white')
player_img.grid(row=2, column=1, padx=30, pady=30)
comp_img = Label(root, image=comp_rock, bg='white')
comp_img.grid(row=2, column=3, padx=30, pady=30)

# lbl Player
lbl_player = Label(root, font=("Arial", 15), text='Player', bg='red', fg='yellow')
lbl_player.grid(row=1, column=1)

#lbl Computer
lbl_comp = Label(root, font=("Arial", 15), text='Computer', bg='red', fg='yellow')
lbl_comp.grid(row=1, column=3)

# Score
player_score = Label(root, text='0', font=('Arial', 30), bg='#9b59b6', fg='white')
breaklbl_score = Label(root, text='-', font=('Arial', 30), bg='#9b59b6', fg='white')
comp_score = Label(root, text='0', font=('Arial', 30), bg='#9b59b6', fg='white')
player_score.grid(row=3, column=1)
breaklbl_score.grid(row=3, column=2)
comp_score.grid(row=3, column=3)

# Message
msg = Label(root, font=('Arial', 30), bg='#9b59b6', fg='#CC9900')
msg.grid(row=2, column=2)
msg.configure(image=start)

# Update Player Score
def updatePlayerScore():
    score = int(player_score['text'])
    score += 1
    player_score['text'] = score

# Update Computer Score
def updateComputerScore():
    score = int(comp_score['text'])
    score += 1
    comp_score['text'] = score

# Logic
def Rock():
    global player_choice
    player_choice = 1
    player_img.configure(image=player_rock)
    MatchProcess()

def Paper():
    global player_choice
    player_choice = 2
    player_img.configure(image=player_paper)
    MatchProcess()

def Scissors():
    global player_choice
    player_choice = 3
    player_img.configure(image=player_scissors)
    MatchProcess()

def MatchProcess():
    comp_choice = random.randint(1, 3) 
    if comp_choice == 1:
        comp_img.configure(image=comp_rock)
        ComputerRock()
    elif comp_choice == 2:
        comp_img.configure(image=comp_paper)
        ComputerPaper()
    else:
        comp_img.configure(image=comp_scissors)
        ComputerScissors()

def ComputerRock():
    if player_choice == 1:
        msg.configure(image=draw)
    elif player_choice == 2:
        updatePlayerScore()
        msg.configure(image=win)
    else:
        msg.configure(image=lose)
        updateComputerScore()

def ComputerPaper():
    if player_choice == 1:
        msg.configure(image=lose)
        updateComputerScore()
    elif player_choice == 2:
        msg.configure(image=draw)
    else:
        msg.configure(image=win)
        updatePlayerScore()        

def ComputerScissors():
    if player_choice == 1:
        msg.configure(image=win)
        updateComputerScore()
    elif player_choice == 2:
        msg.configure(image=lose)
        updateComputerScore()
    else:
        msg.configure(image=draw)             

def ExitApp():
    root.destroy()
    exit()

sm_player_rock = player_rock.subsample(3, 3)
Rock = Button(root, image=sm_player_rock, command=Rock, bg='red')
Rock.grid(row=4, column=1)

sm_player_paper = player_paper.subsample(3, 3)
paper = Button(root, image=sm_player_paper, command=Paper, bg='blue')
paper.grid(row=4, column=2)

sm_player_scissors = player_scissors.subsample(3, 3)
scissors = Button(root, image=sm_player_scissors, command=Scissors, bg='yellow')
scissors.grid(row=4, column=3)

bnt_quit = Button(root, text="Quit", command=ExitApp)
bnt_quit.grid(row=5, column=2)

root.mainloop()
