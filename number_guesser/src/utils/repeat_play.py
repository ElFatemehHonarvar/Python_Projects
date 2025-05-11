from src.utils.random_generator import generate_random_int

def continue_play(intial_score, start, end):

    play_again = input("Would you like to play again? select y or n ")
    if play_again == "y":

        actual_number = generate_random_int(start, end)
        score = intial_score

        return True, score
    return False