#pr2 : rock, paper, scissors
"""- function score

- paly again

--------------
- get_user_choice
  - (validation)
- get_computer_choice
  - (random choice)
- compare
- run, play"""


# first solution
import random

class Play_rock_paper_scissors:

  def __init__(self,):

    self.items = ["rock", "paper", "scissors"]

  def get_user_choice(self,):
    user_act = input("chooce one of the items : rock, paper or scissors : or Quit the game by pressing (q/Q)")

    if user_act.lower() == "q":
      return False

    elif user_act.lower() not in self.items:
      print("wrong choice, you should choose rock, paper or scissors")
      return self.get_user_choice()  ## return function, you can use while loop as well.

    return user_act.lower()

  def get_computer_choice(self,):
    computer_choice = random.choice(self.items)
    return computer_choice

  def select_winner(self,):

    user_choice = self.get_user_choice()
    computer_choice = self.get_computer_choice()

    if not user_choice:
      return "Bye"


    if user_choice == computer_choice:
      return "equal"


    winner_options = [("paper", "rock"), ("rock", "scissors"), ("scissors", "paper")]

    for item in winner_options:
      if [user_choice, computer_choice] == item :

        return "you win"

    else:
      return "you lose the game"


play = Play_rock_paper_scissors()

play.select_winner()

