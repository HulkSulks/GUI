## ========== FIRST TRY SUCCESS TIC TAC TOE BY Aayush Yanamandra 2:53PM 7 June, 2020 ========== ##

#IMPORTING TKINTER AND MESSAGE BOX
from tkinter import *
import tkinter.messagebox
#DEFINING THE GUI
tk = Tk()
tk.title("TIC TAC TOE @AAYUSH.Y@")

#DEFINING PLAYER INPUTS AS STRINGS FOR THE TIME BEING
pa = StringVar()
player_b = StringVar()
p1 = StringVar()
p2 = StringVar()

#DEFINING PLAYER 1 & PLAYER 2 BOTH TOGETHER
#GIVING PLAYER 1 A GRID TO PLAY ON AND DEFINING THE GRID
player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
#SAME APPLIES TO PLAYER 2
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

#bclick OR  b_click IS ENABLED FOR BOTH PLAYERS "B STANDS FOR BOARD"
bclick = True
flag = 0
#DISABLING THE CONFIG BUTTON SO THAT PLAYERS CANNOT CHANGE ANY BUTTON
def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


#DEFINING THE BUTTON CLICK
def btnClick(buttons):
    #GLOBALISING THE bclick, flag, player2_name, player1_name, playerb, pa
    global bclick, flag, player2_name, player1_name, playerb, pa
    #IF THE BUTTON IS EMPTY THEN WE CAN CLICK ON THE BOARD
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        #THEN WE DISABLE CLICK FOR THE TILE/ BUTTON eg. B1 IS DISABLED WHEN PLAYER TYPES OR CLICKS ON B1
        bclick = False
        #THEN WE CHECK FOR WINS
        playerb = p2.get() + " TIE!"
        pa = p1.get() + " WIN!"
        checkForWin()
        flag += 1

    #IF BUTTON IS NOT PRESSED THE USER CAN PRESS THE PARTICULAR BUTTON UNTIL ITS TRUE
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    #IF YOU TRY TO PRESS A FILLED BOX YOU WILL GET AN ERROR
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

#NOW MY PYTHON PROJECT WILL SEARCH FOR ANY POSSIBLE WINS
def checkForWin():
       #WIN FOR HORIZONTAL PLACEMENT ROW-1
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        #WIN FOR HORIZONTAL PLACEMENT ROW-2
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        #WIN FOR HORIZONTAL PLACEMENT ROW-3
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or

        #WIN FOR DIAGONAL PLACEMENT DIAGONAL-1
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        #WIN FOR DIAGONAL PLACEMENT DIAGONAL-1 REVERSE
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or

        #WIN FOR VERTICAL PLACEMENT C-1
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        #WIN FOR VERTICAL PACEMENT C-2
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        #WIN FOR B'S 7, 6, 9
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        #THEN DISABLE BUTTON
        disableButton()
        #DISPLAY THE WINNER NAME
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

    #MOMENT FOR TIE IF ALL 8 BLANKS ARE FILLED
    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    #WIN FOR 'O'
    #WIN FOR HORIZONTAL
    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          #WIN FOR DIAGONAL
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
         #WIN FOR VERTICAL
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        #DISABLE BUTTONS
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)

#BUTTONS I DEFINED PREVIOUSLY
buttons = StringVar()
#DEFINING FONTS AND SIZES, WIDTH AND HEIGHT OF EACH CHARACTER
label = Label( tk, text="Player 1:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)

label = Label( tk, text="Player 2:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)

button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

#DEFINING MAINLOOP
tk.mainloop()
