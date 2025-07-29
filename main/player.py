class Player:
    def __init__(self):
        self.name=""
        self.symbol=""

    def choose_name(self):
      while True:
       name=input("Enter your Name ")
       if name.isalpha()==True:
         self.name=name
         break
         print("Enter a valid Name ")
    
    def choose_symbol(self):
     while True:
      symbol=input("Enter your Symbol ")
      if len(symbol)==1:
         self.symbol=symbol
         break
         print("Enter a one symbol")