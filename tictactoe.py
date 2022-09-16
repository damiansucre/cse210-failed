board =[' ','1','2','3','4','5','6','7','8','9']
Win = 1
Running = 0
Game = Running
Draw = -1  
Running = 0    
Stop = 1  
Mark = 'X'

#The program must have a function called main.
def main():    
    player =1
    print("\nTic-Tac-Toe is a game in which two players seek in alternate turns to complete a row,\n"
        "a column, or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.\n" 
        "Designed by Damian Escalante\n")

    #The program must have at least one while loop.
    while (Game == Running):

        DrawBoard(board) 
        #The program must have at least one if/then block.   
        if(player % 2 != 0):    
            print("X's turn to choose a square (1-9)")    
            Mark = 'x'    
        else:    
            print("O's turn to choose a square (1-9)")    
            Mark = 'O'    
        choice = int(input("Enter the position between [1-9] where you want to mark : "))    
        if(CheckPosition(choice)):    
            board[choice] = Mark    
            player+=1    
            CheckWin(board)
    
    #The program must have at least one if/then block.
    if(Game==Draw):    
        print("Good game. Thanks for playing!")    
    elif(Game==Win):    
        player-=1    
        if(player%2!=0):    
            print("Good game. Thanks for playing!\nPlayer X Won")    
        else:    
            print("Good game. Thanks for playing!\nPlayer O Won")

#The program must have more than one function.
#The game is played on a grid that is three squares by three squares.    
def DrawBoard(board):    
    print("%c|%c|%c" % (board[1],board[2],board[3]))    
    print("-+-+-")    
    print("%c|%c|%c" % (board[4],board[5],board[6]))    
    print("-+-+-") 
    print("%c|%c|%c" % (board[7],board[8],board[9]))    
    

#This Function Checks position is empty or not    
def CheckPosition(x):    
    if((board[x] == '1')or(board[x] == '2')or(board[x] == '3')or(board[x] == '4')or(board[x] == '5')or(board[x] == '6')or(board[x] == '7')or(board[x] == '8')or(board[x] == '9')):    
        return True    
    else:    
        return False

#This Function Checks player has won or not    
def CheckWin(board):    
    global Game    
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[1] != '1'):    
        Game = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != '4'):    
        Game = Win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != '7'):    
        Game = Win    
    #Vertical Winning Condition    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != '1'):    
        Game = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != '2'):    
        Game = Win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != '3'):    
        Game=Win    
    #Diagonal Winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != '5'):    
        Game = Win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != '5'):    
        Game=Win    
    #Match Tie or Draw Condition    
    elif(board[1]!='1' and board[2]!='2' and board[3]!='3' and board[4]!='4' and board[5]!='5' and board[6]!='6' and board[7]!='7' and board[8]!='8' and board[9]!='9'):    
        Game=Draw    
    else:            
        Game=Running

if __name__ == "__main__":
    main()