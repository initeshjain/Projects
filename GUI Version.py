import tkinter
import random
from functools import partial

window = tkinter.Tk()

#..................Operation Area..................
def choices(u_choice):
    chances = 10
    i = 0
    computer_points = 0
    player_points = 0
    global p, op, er
    list=["paper","stone","scissor","paper","stone","scissor","paper","stone","scissor"]

    p['text'] = u_choice
    
    computer_guess = (random.choice(list))
    op['text'] = computer_guess

    if u_choice == 'stone' and  computer_guess == 'paper':
         er['text'] = "Computer Wins"

    elif u_choice == 'paper' and  computer_guess == 'stone':
            er['text'] = "You Wins"
            
    elif u_choice == 'scissor' and  computer_guess == 'paper':
            er['text'] = "You Wins"

    elif u_choice == 'paper' and  computer_guess == 'scissor':
            er['text'] = "Computer Wins"

    elif u_choice == 'stone' and  computer_guess == 'scissor':
            er['text'] = "You Wins"

    elif u_choice == 'scissor' and  computer_guess == 'stone':
            er['text'] = "Computer Wins"

    elif u_choice == computer_guess:
            er['text'] = "DRAW"

    else:
            er['text'] = "Oops Something Went Wrong."

#...................Design Area....................

window.title("The Stone, Paper, Scissor Game")
heading = tkinter.Label(window, text = "The Stone, Paper, Scissor Game",font=('arial',28,"bold"))
heading.grid(row=2, column=1, columnspan="6")

line = tkinter.Label(window, text = "-----------------------------------------------------------------------------",font=('arial',28,"bold"))
line.grid(row=3, column=1, columnspan="6")

# Opponent side design START.
opstatic = tkinter.Label(window, text = "Opponent selected:     ",font=('arial',20,"italic"))
op = tkinter.Label(window, text = "",font=('arial',20,"italic"))
op.grid(row=9, column=3, columnspan="4")
opstatic.grid(row=9, column=2, columnspan="4")
# Opponent side design END.

# WIN OR LOOSE SHOWING CODE HERE...........
er = tkinter.Label(window, text = "",font=('arial',14,"bold"))
er.grid(row=17, column=2, columnspan="8")

# Player side design START.
pstatic = tkinter.Label(window, text = "YOU selected:    ",font=('arial',14,"italic"))
pstatic.grid(row=23, column=2, columnspan="4")
p = tkinter.Label(window, text = "",font=('arial',14,"italic"))
p.grid(row=23, column=3, columnspan="4")
# Player side design END.

# Buttons for Stone Paper and Scissor.......

btn = tkinter.Button(window, text="Stone", width=20, command=partial(choices, "stone"))
btn.grid(row=40, column=2)

btn = tkinter.Button(window, text="Paper", width=20, command=partial(choices, "paper"))
btn.grid(row=40, column=3)

btn = tkinter.Button(window, text="Scissor", width=20, command=partial(choices, "scissor"))
btn.grid(row=40, column=4)


window.mainloop()
