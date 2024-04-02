import msvcrt
import os


def main():
    
    cols = 3
    rows = 3
    table = [["-" for i in range(cols)] for j in range(rows)]
    playerRow = 0
    playerCol = 0
    turn = 0
    winX = False
    winO = False

    while True:

        os.system('cls')
        move(arr=table, r=rows, c=cols, pRow=playerRow, pCol=playerCol, t=turn)
        
        if winX:
            print("\nPLayer X wins!")
            break
        elif winO:
            print("\nPlayer O wins!")
            break
        
        print("\nControls:\nW : Move Up\nA : Move Left\nS : Move Down\nD : Move Right\nQ : Move Up-Left\nE : Move Up-Right\nZ : Move Down-Left\nX : Move Down-Right")
        print("\nEnter Move > ", end = "")
        
        c = msvcrt.getch().decode('utf-8')

        if c == "\r":
            if turn % 2 == 0:
                table[playerRow][playerCol] = "X"
            else:
                table[playerRow][playerCol] = "O"
            turn += 1
            
        elif c == "w":
            if playerRow - 1 < 0:
                playerRow = playerRow
            elif table[playerRow - 1][playerCol] == "-":
                playerRow -= 1
            elif table[playerRow - 1][playerCol] != "-":
                if playerRow - 2 < 0:
                    playerRow = playerRow
                elif table[playerRow - 2][playerCol] == "-":
                    playerRow -= 2
                
        elif c == "a":
            if playerCol - 1 < 0:
                playerCol = playerCol
            elif table[playerRow][playerCol - 1] == "-":
                playerCol -= 1
            elif table[playerRow][playerCol - 1] != "-":
                if playerCol - 2 < 0:
                    playerCol = playerCol
                elif table[playerRow][playerCol - 2] == "-":
                    playerCol -= 2
                    
        elif c == "s":
            if playerRow + 1 >= rows:
                playerRow = playerRow
            elif table[playerRow + 1][playerCol] == "-":
                playerRow += 1
            elif table[playerRow + 1][playerCol] != "-":
                if playerRow + 2 >= rows:
                    playerRow = playerRow
                elif table[playerRow + 2][playerCol] == "-":
                    playerRow += 2
                    
        elif c == "d":
            if playerCol + 1 >= cols:
                playerCol = playerCol
            elif table[playerRow][playerCol + 1] == "-":
                playerCol += 1
            elif table[playerRow][playerCol + 1] != "-":
                if playerCol + 2 >= cols:
                    playerCol = playerCol
                elif table[playerRow][playerCol + 2] == "-":
                    playerCol += 2
        
        elif c == "q":
            if playerCol - 1 < 0 or playerRow - 1 < 0:
                playerCol = playerCol
                playerRow = playerRow
            elif table[playerRow - 1][playerCol - 1] == "-":
                playerCol -= 1
                playerRow -= 1
            elif table[playerRow - 1][playerCol - 1] != "-":
                if playerRow - 2 < 0 or playerCol - 2 < 0:
                    playerCol = playerCol
                    playerRow = playerRow
                elif table[playerRow - 2][playerCol - 2] == "-":
                    playerCol -= 2
                    playerRow -= 2
                    
        elif c == "e":
            if playerCol + 1 >= cols or playerRow - 1 < 0:
                playerCol = playerCol
                playerRow = playerRow
            elif table[playerRow - 1][playerCol + 1] == "-":
                playerCol += 1
                playerRow -= 1
            elif table[playerRow - 1][playerCol + 1] != "-":
                if playerRow - 2 < 0 or playerCol + 2 >= cols:
                    playerCol = playerCol
                    playerRow = playerRow
                elif table[playerRow - 2][playerCol + 2] == "-":
                    playerCol += 2
                    playerRow -= 2
                    
        elif c == "z":
            if playerCol - 1 < 0 or playerRow + 1 >= rows:
                playerCol = playerCol
                playerRow = playerRow
            elif table[playerRow + 1][playerCol - 1] == "-":
                playerCol -= 1
                playerRow += 1
            elif table[playerRow + 1][playerCol - 1] != "-":
                if playerRow + 2 >= rows or playerCol - 2 < 0:
                    playerCol = playerCol
                    playerRow = playerRow
                elif table[playerRow + 2][playerCol - 2] == "-":
                    playerCol -= 2
                    playerRow += 2

        elif c == "x":
            if playerCol + 1 >= cols or playerRow + 1 >= rows:
                playerCol = playerCol
                playerRow = playerRow
            elif table[playerRow + 1][playerCol + 1] == "-":
                playerCol += 1
                playerRow += 1
            elif table[playerRow + 1][playerCol + 1] != "-":
                if playerRow + 2 >= rows or playerCol + 2 >= cols:
                    playerCol = playerCol
                    playerRow = playerRow
                elif table[playerRow + 2][playerCol + 2] == "-":
                    playerCol += 2
                    playerRow += 2
                    
        winX, winO = checkCombination(table)
                    
def checkCombination(arr):
    
    playerX = False
    playerO = False
    
    for i in range(3):
        if arr[i][0] == arr[i][1] and arr[i][1] == arr[i][2]:
            if arr[i][1] == "X":
                playerX = True
            elif arr[i][1] == "O":
                playerO = True
                
        elif arr[0][i] == arr[1][i] and arr[1][i] == arr[2][i]:
            if arr[1][i] == "X":
                playerX = True
            elif arr[1][i] == "O":
                playerO = True
                
    if arr[0][0] == arr[1][1] and arr[1][1] == arr[2][2]:
        if arr[0][0] == "X":
            playerX = True
        elif arr[0][0] == "O":
            playerO = True
    elif arr[2][0] == arr[1][1] and arr[1][1] == arr[0][2]:
        if arr[1][1] == "X":
                playerX = True
        elif arr[1][1] == "O":
                playerO = True
                
    return playerX, playerO
    
    
def move(arr, r, c, pRow, pCol, t):
    for i in range(r):
        for j in range(c):

            if i == pRow and j == pCol:
                if t % 2 == 0:
                    print("X" + " ", end="")
                else:
                    print("O" + " ", end="")
            else:
                print(arr[i][j] + " ", end="")

        print()


if __name__ == "__main__":
    main()
