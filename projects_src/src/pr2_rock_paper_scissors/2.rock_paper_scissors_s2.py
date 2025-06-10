import random

class Game_rock_paper_scissors:

  def __init__(self,):

    self.items = ["rock", "paper", "scissors"]

  def get_user_choice(self,):
    user_act = input("chooce one of the items : rock, paper or scissors : ")


    if user_act.lower() not in self.items:
      print("wrong choice, you should choose rock, paper or scissors")
      return self.get_user_choice()  ## return function, you can use while loop as well.

    return user_act.lower()

  def get_computer_choice(self,):
    computer_choice = random.choice(self.items)
    return computer_choice

  def select_winner(self,user_choice, computer_choice):

    if user_choice == computer_choice:
      return "equal"

    winner_options = {"paper": "rock", "rock": "scissors", "scissors": "paper"}
    if winner_options[user_choice] == computer_choice:
      return "you win"

    return "you lose the game"

  def play(self):
    user_choice = self.get_user_choice()
    computer_choice = self.get_computer_choice()
    print(f"computer choice is {computer_choice}")
    print(self.select_winner(user_choice, computer_choice))




if __name__ == "__main__":

  game = Game_rock_paper_scissors()

  while True:
    game.play()
    user_act = input("Quit the game by pressing (q/Q) or continue by pressing any key : ")
    if user_act.lower() == "q":
      print("Bye")
      break