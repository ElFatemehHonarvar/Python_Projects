def give_hint(user_guess, actual_number):

    if user_guess > actual_number:
        print(f"you should select a actual_number which is smaller than {user_guess}")

    else:
        print(f"you should select a actual_number which is bigger than {user_guess}")