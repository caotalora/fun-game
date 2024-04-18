import turtle  as t 
from time import sleep
from sys import exit
import turtle as t


def Winner_Window():
    bob.clear()
    picasso.clear()
    diana.clear()
    sc.bgcolor(0.58, 0.482, 0.212)
    sc.setup(width = 600, height= 600)
    picasso.penup()
    picasso.goto(0,0)
    if z[0] % 2 != 0:
        picasso.color('red')
        picasso.write("Congrat's Red Win", True, align = "center", font = ('Verdana',50,"bold"))
    else:
        picasso.color('black')
        picasso.write("Congrat's Black Win", True, align= "Center", font = ('Verdana',50,"bold"))
    t.onscreenclick(None)
    ## may want to add an special function inside onscreenclick to do the restart

'''
bob = t.Turtle()
sc = t.Screen()
sc.title("Teeko")
sc.bgcolor(0.58, 0.482, 0.212) ## RGB selector 0-1
sc.setup(width = 600, height= 600)
bob.speed(500)
bob.hideturtle()
'''

###original game funcs
def quitcheck(string):
    '''so player can quit at any time'''
    if string.lower() == "quit":
        quit()
    else:
        return True
## we have to print the statements, we also have to see 

def displaymenu():
    '''Shows menu, and different options for player'''
    choice = input("""1. Display Instructions
2. Display Additional Information
3. Start Game

Enter a number: """)
    quitcheck(choice)
    if choice == "1":
        print("""
Teeko consists of a 5 by 5 board where players alternate placing tokens.
A player wins when they place 4 of their tokens in a line or sqaure.
Once both players have placed 4 tokens, they must move their existing tokens rather than place new ones.""")
        displaymenu()
    elif choice == "2":
        print("""
Type quit at any time to exit the game
Made by Cameron Barnaik, Leo Yang, Carlos Otalora, Jorge Valdivieso""")
        displaymenu()
    elif choice == "3":
        return
    else:
        displaymenu()

def check_horiz(row,col,piece):
    '''Checks if there is a horizontal line on the board anywhere for current player turn'''
    if col == 0 or col == 1:
        if board[row][col] == piece:
            for i in range(1,4):
                if board[row][col + i] == piece:
                    continue
                else:
                    return False
            return True
        
def check_vert(row,col,piece):
    '''checks for vertical line of whoever's turn it is'''
    if row == 0 or row == 1:
        if board[row][col] == piece:
            for i in range(1,4):
                if board[row + i][col] == piece:
                    continue
                else:
                    return False
            return True
        else:
            return False
    else:
        return False
        

def taketurn(board, turn,row,column):
    '''carries out player's moves'''
    if turn % 2 == 0:
        piece = "B"
    else:
        piece = "R"
    
#    while board[row][column]:
 #       print("There's already a piece there, choose another space")
  #      row, column = taketurn(board,turn,row,column)
    board[row][column] = piece
    '''    
    else:
        print('For the piece you want to move...')
        row0,column0 = get_player_input1(turn)
        if board[row0][column0] != piece:
            print("move YOUR piece")
            row0,column0 = get_player_input1(turn)
            while board[row0][column0] != piece:
                print("move YOUR piece")
                row0,column0 = get_player_input1(turn)
        board[row0][column0] = ''
        print("Where do you want to move the piece...")
        row,column = get_player_input1(turn)
        if board[row][column] != '':
            while board[row][column]:
                print("There's already a piece there, choose another space")
                row, column = get_player_input1(turn)
        board[row][column] = piece
        '''
    return row,column
    
        
def rightorleft(row,col,piece):
    '''checks if given point is top right or top left for checking if diagonal lines'''
    if piece != board[row][col]:
        return False
    elif row < 2 and col < 2:
        return 1
    elif row < 2 and col > 2:
        return -1
    else:
        return 0

def square_possible(row,col,piece):
    '''checking if a square is possible for a player'''
    #if there aren't 2 squares on the row or column, then 
    #square not possible because 4 pieces per player
    count = 0
    if row > 3 or col > 3:
        return False
    else:
        for i in range(5):
            if board[i][col] == piece:
                count += 1
        if count == 2:
            return True
        else:
            return False

def check_square(row,col,piece):
    '''Checks if whoever's turn it is made a square'''
    if square_possible(row,col,piece):
    #no point in checkinf if square if not possible
        if piece == board[row][col]:
            for i in range(2):
                for j in range(2):
                    if board[row + i][col + j] == piece:
                        continue
                    else:
                        return False
            return True
        else:
            return False
    else:
        return False
        

def check_diag(row,col,piece):
    '''checks if there is a diagonal line for whose turn it is'''
    n = rightorleft(row,col,piece)
    if n:
        if n > 0:
            piece = board[row][col]
            for i in range(1,4):
                if board[row + i][col + i] == piece:
                    continue
                else:
                    return False
            return True
        else:
            piece = board[row][col]
            for i in range(1,4):
                if board[row + i][col - i] == piece:
                    continue
                else:
                    return False
            return True
    else:
        return False

##### difference?
def wincheck(board,turn):
    '''Detects if one of the players won'''
    if turn < 6:
        return False
    elif turn % 2 == 0:
        piece = "B"
    else:
        piece ="R"
    states = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != '':
                states.append(checker(i,j,piece))
    if (True in states):
        print(f"Congrats, {piece} won")
        Winner_Window()
        return True
    else:
        return False  


def checker(row, col,piece):
    '''checks if any of the win conditions are met for one point'''
    if check_horiz(row,col,piece) or check_vert(row,col,piece) or check_diag(row,col,piece) or check_square(row,col,piece):
        return True
    else:
        return False

def makeboard():
    '''makes information container (list)'''
    rows = []
    columns = []
    for h in range(5):
        for j in range(5):
            columns += [""]
        rows += [columns]
        columns = []
    return rows
###

z = [0]

mylist = [1]

def rectangle(x):
    bob.pendown()
    bob.width(20)
    bob.forward(x)
    bob.right(90)
    bob.forward(x*2)
    bob.right(90)
    bob.forward(x*2)
    bob.right(90)
    bob.forward(x*2)
    bob.right(90)
    bob.forward(x)

Points = {"A1":(-145,115),"A2":(-72.5,115),"A3":(0,115),"A4":(72.5,115),"A5":(145,115)
          ,"B1":(-145,42.5),"B2":(-72.5,42.5),"B3":(0,42.5),"B4":(72.5,42.5),"B5":(145,42.5)
           ,"C1":(-145,-30),"C2":(-72.5,-30),"C3":(0,-30),"C4":(72.5,-30),"C5":(145,-30)
           ,"D1":(-145,-102.5),"D2":(-72.5,-102.5),"D3":(0,-102.5),"D4":(72.5,-102.5),"D5":(145,-102.5)
           ,"E1":(-145,-175),"E2":(-72.5,-175),"E3":(0,-175),"E4":(72.5,-175),"E5":(145,-175)}

def minisquares():
    for i in range(4):
        bob.pendown()
        bob.forward(12.5)
        bob.penup()
        bob.forward(30)
        bob.right(90)
        bob.forward(30)
    bob.penup()
    bob.forward(72.5)

    #bob.pendown()
    #bob.fd(12.5)

def DrawingRight2():
    ## create slla the circles
    for key, value in Points.items():
        bob.width(2)
        bob.penup()
        bob.goto(value[0],value[1])
        bob.pendown()
        bob.circle(30) 
    ## makes the big ectangle 
    bob.penup()
    bob.home()
    bob.goto(0,200)
    rectangle(200)
    bob.width(1)
    list = ["A1","B1","C1","D1"]
    for i in list:
        value = Points[i] 
        bob.penup()
        bob.goto(value[0]+30,value[1]+30)
        bob.pendown()
        for i in range(4):
            minisquares()
    

Translator_rows = {"A":0,"B":1, "C":2,"D":3,"E":4}


def filler3(final):
        Value = Points[final]
        if z[0] % 2 == 0:
            diana.fillcolor('black')
            #taketurn(board,z[0])
        else:
            diana.fillcolor('red')
            #taketurn(board,z[0])
        diana.penup()
        diana.goto(Value[0],Value[1]+5) # changed to + 5 for half filling
        diana.pendown()
        diana.begin_fill()
        diana.circle(25) ## changed to 25 for half filling 
        diana.end_fill()
        
def replacement(position):
    Value = Points[position]
    diana.color(0.58,0.482,0.212)
    diana.fillcolor(0.58, 0.482, 0.212)
    diana.penup()
    diana.goto(Value[0],Value[1]+5) # changed to + 5 for half filling
    diana.pendown()
    diana.begin_fill()
    diana.circle(26) ## changed to 25 for half filling 
    diana.end_fill()
    diana.color('black')



def Turn():
    picasso.penup()
    picasso.setposition(0,250)
    picasso.clear()
    picasso.pendown()
    if z[0] < 8:
        if z[0] % 2 != 0:
            picasso.color('red')
            picasso.write(" It's Red Turn", True, align = "center", font = ('Verdana',20,"bold"))
        else:
            picasso.color('black')
            picasso.write(" It's Black Turn", True, align= "Center", font = ('Verdana',20,"bold"))
    elif mylist[0] == 1:
        if z[0] % 2 != 0:
            picasso.color('red')
            picasso.write(" It's Red Turn, Please select a piece to remove", True, align = "center", font = ('Verdana',15,"bold"))
        else:
            picasso.color('black')
            picasso.write(" It's Black Turn, Please select a piece to remove", True, align= "Center", font = ('Verdana',15,"bold"))
    else:  
        if z[0] % 2 != 0:
            picasso.color('red')
            picasso.write(" It's Red Turn, Please select a position for the piece", True, align = "center", font = ('Verdana',15,"bold"))
        else:
            picasso.color('black')
            picasso.write(" It's Black Turn, Please select a position for the piece", True, align= "Center", font = ('Verdana',15,"bold"))
Bmoves = []
Rmoves = []

moves = []

def Printer(string):
    picasso.clear()
    picasso.penup()
    picasso.goto(0,250)
    picasso.write (string, font = ('Verdana',20,"bold"), align = 'center')

def game_play(row,column,final,Bmoves,Rmoves):
    if z[0] % 2 == 0:
        piece = 'B'
    else:
        piece = 'R'
    
    if piece == 'B' and z[0] >= 8 and mylist[0] != 1:
        dx = abs(Bmoves[-2]) - abs(int(row))
        dy = abs(Bmoves[-1]) - abs(int(column - 1))
      #  print(f'{Bmoves}, ({row},{column - 1})')
        if dx == 0 and dy == 0:
           Printer("There is already a piece there, please try again")
           return
        elif dx > 1 or dy > 1:
            Printer("You can move one space. Try again")
            return
        else:
            pass
    
    elif piece == 'R' and z[0] >= 8 and mylist[0] != 1:
        dx = abs(Rmoves[-1][0]) - abs(int(row))
        dy = abs(Rmoves[-1][1]) - abs(int(column) - 1)
      #  print(f'{Rmoves}, ({row},{column - 1})')
        if dx == 0 and dy == 0:
           Printer("There is already a piece there, please try again")
           return
        elif dx > 1 or dy > 1:
            Printer("You move in any direction\nbut only by one space\nTry again")
            return
        else:
            pass
    
        

    if board[row][int(column) - 1] and z[0] < 8:
        Printer("There is already a piece there, please try again")
    elif z[0] < 8:
        filler3(final)
        taketurn(board,z[0],row,column - 1)
        x = wincheck(board,z[0])
        z[0] += 1
        if x == False: ## slves a problem in the win window
            Turn() 
    elif board[row][int(column) - 1] != piece and mylist[0] == 1:
        Printer("Move YOUR piece")
    elif board[row][int(column) - 1] and mylist[0] != 1:
        Printer("There is already a piece there, try again")
    else:
        if mylist[0] == 1:
            replacement(final)
            if z[0] % 2 == 0:
                Bmoves.append(row)
                Bmoves.append(column - 1)
               # print(row,column - 1)
                #print('jello')
            else:
                Rmoves += [(row,int(column) - 1)]
            board[row][int(column)-1] = ""                    ### replcaes piece from the board()
            mylist[0] = 0
            Turn()
        else:   
            filler3(final)
            taketurn(board,z[0],row,column - 1)
            x = wincheck(board,z[0])
            z[0] += 1
            if x == False:
                Turn()
            mylist[0] = 1
    

  #  for i in board:
   #     print(i)


def get_player_input1(x,y):
    picasso.clear()
    bob.width(1)
    string = ''
    x = float(x)
    y = float(y)
    ## function to decide whose turn is it 
    if x > -200 and x < -121.75:
        string += '1'

    elif x > -121.75 and x < -36.25:
        string += '2'
    elif x > -36.25 and x < 36.75:
        string += '3'
    elif x > 36.25 and x < 121.75:
        string += '4'
    elif x > 121.75 and x < 200:
        string += '5'

    if y > 108.75 and y < 200:
        string2 = "A"
    elif y > 36.25 and y < 108.75:
        string2 = "B"
    elif y > -42.5  and y < 36.25:
        string2 = "C"
    elif y > -108.75 and y < -42.5:
        string2 = "D"
    elif y > -200 and y < -108.75:
        string2 = "E"
    
    row = Translator_rows[string2]
    column = int(string)
    final = string2 + string
    game_play(row,column,final,Bmoves,Rmoves)


displaymenu()
board = makeboard()


bob = t.Turtle()
sc = t.Screen()
sc.title("Teeko")
sc.bgcolor(0.58, 0.482, 0.212) ## RGB selector 0-1
sc.setup(width = 600, height= 600)
bob.speed(5000)
bob.hideturtle()
picasso = t.Turtle()
picasso.hideturtle()
diana = t.Turtle()
diana.speed(500)
diana.hideturtle()


DrawingRight2()
Turn()
t.onscreenclick(get_player_input1, btn = 1, add = True)
t.done()


leaderboard = open("leaderboard.txt", "a+")
name = input("Enter your initials for the leaderboard: ")
leaderboard.write(f"{name} won in {z[0]+1} turns\n")
leaderboard.close()
myfile = open('leaderboard.txt','r')
print("You've been added to the leaderboard!")
myfile.close()
## probme: there is no adjacent statemenrt, moreover, the board does not remove the piece after replacement happens()