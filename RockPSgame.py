from tkinter import *
import random

root = Tk()
root.title('RPS Game')
root.geometry('245x270')

choices = ['rock', 'paper', 'scissors']
wins = 0
loses = 0
def rules(string):
    player.delete(0, END)
    choice_p = player.insert(0,string)
    choice_m = random.choice(choices)
    choice_p = player.get()
    global wins
    global loses
    if choice_p == choice_m:
        result = "Nope\nIt's a Tie "
    elif choice_p == 'rock' and choice_m == 'scissors':
        result = f'you win\n{choice_p}\n beat\n {choice_m}'
        wins +=1
    elif choice_p == 'scissors' and choice_m == 'paper':
        result = f'you win\n{choice_p}\n beat\n {choice_m}'
        wins += 1
    elif choice_p == 'paper' and choice_m == 'rock':
        result = f'you win\n{choice_p}\n beat\n {choice_m}'
        wins += 1
    else:
        result = f'you loose\n{choice_m}\n beat\n {choice_p}'
        loses +=1
    answer = Label(root, text=result + '\n' + 'You = ' + str(wins) + '\nDino = ' + str(loses), font=('Times', 12))
    answer.grid(row=3, column=1)




welcome_msg = Label(root, text='Welcome! \n I am Dino, Lets play Rock Paper Scissors')
welcome_msg.grid(row=0, column=0, padx=10,columnspan=3)

player = Entry(root, width=38 )
player.grid(row=1, column=0, padx=3, pady=5, columnspan=3)


rock_btn = Button(root, text='Rock', width=10, height=2, command= lambda: rules('rock'))
rock_btn.grid(row=2, column=0, sticky=W)

paper_btn = Button(root, text='Paper', width=10, height=2,command= lambda: rules('paper'))
paper_btn.grid(row=2, column=1, sticky=W)

scis_btn = Button(root, text='Scissors', width=10, height=2, command= lambda: rules('scissors'))
scis_btn.grid(row=2, column=2, sticky=W)
root.mainloop()