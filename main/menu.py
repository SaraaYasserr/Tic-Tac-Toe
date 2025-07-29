class Menu:
  def main(self):
      print("Welcome to Tic Tac Toe")
      print('1/Start game')
      print('2/End game')
      choice=input("Enter a number ")
      return choice


  def endgame():
      txt="""
      Game Over 
      1- Restart Game 
      2-Quit Game
      Enter your choice
      """
      choice=input(txt)
      return choice

