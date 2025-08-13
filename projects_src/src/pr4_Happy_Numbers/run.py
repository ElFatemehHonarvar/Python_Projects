def is_happy(num : int):
    """
    Returns True if 'num' is a happy number, False otherwise.
    A happy number is defined by repeatedly replacing the number
    with the sum of the squares of its digits until it becomes 1
    (happy) or loops endlessly (unhappy).
    """
    seen_numbers = set()

    while (num != 1) and (not num in seen_numbers):
        seen_numbers.add(num)
        num = sum([(int(i)**2) for i in str(num)])

    return num == 1


if __name__ == "__main__":

    # test case
    assert is_happy(45) is False
    assert is_happy(19) is True