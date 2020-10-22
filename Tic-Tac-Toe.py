#Tic tac toe let's gooo

board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter
    

def spaceIsFree(pos):
    return board[pos] == ' '
    

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
def isWinner(bo, le):
    #win wierszami (1,2,3) || (4,5,6) || (7,8,9) x
    #win kolumnami (1,4,7) || (2,5,8) || (3,6,9) 
    #win ukosami   (1,5,9) || (3,5,7)
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) 

def playerMove():
    run = True
    while run:
        move = input('Select position to place an X in 1-9: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('This place is occupied')
            else:
                print('insert correct number in range 1-9')
        except:
            print('please type a number!')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i 
                return move

    cornerOpen = []
    for i in possibleMoves:
        for i in [1,3,7,9]:
            cornerOpen.append(i)
    if len(cornerOpen) > 0:
        move = selectRandom(cornerOpen)
        return move
    if 5 in possibleMoves:
        move = 5
        return move
    
    edgesOpen = []
    for i in possibleMoves:
        for i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    return move
    
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True    

def main():
    print("Welcome in Tica-tac-toe game!")
    printBoard(board)

    while not isBoardFull(board):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O wins')
            break
        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie!')
            else:
                insertLetter('O', move)
                print('Computer placed \'O\' in position', move, ':')
                printBoard(board)
        else:
            print('X wins - you just won!')
            break
    
    if isBoardFull(board):
        print("Tie!")

main()
