def validate_guess(user_guess, start, end):

  if not user_guess.isdigit():
    print(" Invalid input, your input is not integer, Please enter a number between 1 to 100")
    return False

  user_guess = int(user_guess)
  if (int(user_guess) < start) or (int(user_guess) > end):
    print("Invalid input, Please enter a number between 1 to 100")
    return False

  return True

