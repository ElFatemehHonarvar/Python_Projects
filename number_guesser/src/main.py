import random

from src.utils.input_validator import validate_guess
from src.utils.hint_generator import give_hint
from src.utils.repeat_play import continue_play
from src.utils.random_generator import generate_random_int



def game(start, end, intial_score):
  actual_number = generate_random_int(start, end)
  score = intial_score
  LOSE_SCORE = 7


  while True :
    user_guess = input(f"guess an interger number between {start} and {end}: ")

    if user_guess == "q":
      print("You quit the game")
      break


    if validate_guess(user_guess, start, end):

      user_guess = int(user_guess)
      if user_guess == actual_number:
        print("Horaaaaa you win and score is : {score}")

        if continue_play(intial_score, start, end):
          continue
        break


      give_hint(user_guess, actual_number)
      score -= 1
      if score < LOSE_SCORE:
        print("sorry you lose the game")
        if continue_play(intial_score, start, end):
          continue
        break

    else:
      continue


if __name__=="__main__":
    game(1, 100, intial_score = 10)