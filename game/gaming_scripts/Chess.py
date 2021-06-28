ndef playercolor():
    while True:
        color = input("If you want to play black, type b. Otherwise type w: ")
        color = color.lower()
        if color == "b":
            break
        elif color == "w":
            break
        else:
            print("You must input either w or b. try again.")

def displayboard():
    global boardPositions = [["wr1", "wk1", "wi1", "wq", "wn", "wi2", "wk2", "wr2"], ["wp1", "wp2", "wp3", "wp4", "wp5", "wp6", "wp7", "wp8"], ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], ["bp1", "bp2", "bp3", "bp4", "bp5", "bp6", "bp7", "bp8"], ["br1", "bk1", "bi1", "bq", "bn", "bi2", "bk2", "br2"]]
    colorChoice = playercolor()
    if colorChoice == "w":
        print(boardPositions[0])
        print(boardPositions[1])
        print(boardPositions[2])
        print(boardPositions[3])
        print(boardPositions[4])
        print(boardPositions[5])
        print(boardPositions[6])
        print(boardPositions[7])
    else:
        print(boardPositions[7])
        print(boardPositions[6])
        print(boardPositions[5])
        print(boardPositions[4])
        print(boardPositions[3])
        print(boardPositions[2])
        print(boardPositions[1])
        print(boardPositions[0])

displayboard()

class Piece:
    def __init____(self,peace,color):
        self.Piece = peace
        self.color = color
    def move(self):
        pass


#def handleturn():
    #originalPos = int(input("Enter the position of the boardpiece that you want to move:"))
    #originalPos = originalPos-1
    #targetPos = int(input("Enter the value at which you want your board peace to move:"))
    #targetPos = targetPos-1
    #removedGamePiece = del(boardPositions,originalPos)
    #boardPositions.add
    #(removedGamePiece)

#handleturn()