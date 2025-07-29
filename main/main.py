from player import Player
from board import Board
from menu import Menu

class Game:
    def __init__(self):
        self.players=[Player(),Player()]
        self.board=Board()
        self.menu=Menu()
        self.cur=0

    def start(self):
       choice=self.menu.main()
       if choice=='1':
          self.setup()
          self.play_game()
       else:
          print("Thank You For Playing ")

    def setup(self):
        for player in self.players:
           player.choose_name()
           player.choose_symbol()

    def play_game(self):
        while True :
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice=self.menu.display()
                if choice =='1':
                 self.restart()
                else :
                    print("Thank You For Playing ")
                    break
            else:
               self.switch()


    def play_turn(self):
        player=self.players[self.cur]
        self.board.display()
        print(f"{player.name}'s turn ")
        while True:
          try:
            cell=int(input("Enter a cell (1-9): "))
            if 1<= cell <=9 and self.board.update(cell,player.symbol):
             break
            else :
             print("Try a gain ")
          except ValueError:
             print("Enter a number between 1 anfd 9 ")


    def switch (self):
        self.cur=1-self.cur

    def check_win(self):
        com=[
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
            ]
        for combo in com:
            if (self.board.board[combo[0]]==self.board.board[combo[1]]==
                 self.board.board[combo[2]]):
                  return True
            return False

    def check_draw(self):
       return all(not cell.isdigit()for cell in self.board.board)

    def restart(self):
        self.board.reset()
        self.cur=0
        self.play_game()

game=Game()
game.start()




