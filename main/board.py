class Board:
    def __init__(self):
        self.board=[str(i) for i in range(1,10)]


    def display(self):
        for i in range(0,9):
            print( ' | ',end="")
            print(self.board[i],end="")
            if (i%3==2):
                print(' | ',end="")
                print('\n'+' -'*7)

    def update(self,choice,symbol):
        if self.board[choice-1].isdigit():
            self.board[choice-1]=symbol
            return True
        return False




    def reset(self):
       self.board=[str(i) for i in range(1,10)]
        


