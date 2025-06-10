import random
import string
from abc import ABC , abstractmethod

import nltk

class PasswordGenerator(ABC):

    @abstractmethod
    def generate(self):
        pass


class PinCodeGenerator(PasswordGenerator):

    def __init__(self, length):
        self.length = length

    def generate(self):
            pass_num = "".join(random.choices(string.digits, k=self.length))
            print(pass_num)


class RandomPasswordGenerator(PasswordGenerator):

    def __init__(self, length, include_numbers=True, include_symbols=True):

        self.length = length
        self.include_numbers = include_numbers
        self.include_symbols = include_symbols
        self.characters = string.ascii_letters

        if self.include_numbers:
            self.characters += string.digits

        if self.include_symbols:
            self.characters += string.punctuation



    def generate(self):

        password = "".join(random.choices(self.characters, k=self.length))
        return password


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, num_of_words, random_captalize, separator, vocabulary=None):

        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()

        self.num_of_words = num_of_words
        self.random_captalize = random_captalize
        self.separator = separator
        self.vocabulary = vocabulary

        if self.separator not in string.punctuation:
            self.separator = "-"  # Enter is an issue

    def generate(self):

        words = random.choices(self.vocabulary, k=self.num_of_words)
        if self.random_captalize:
            upper_words = [word.upper() if random.choice([True, False]) else word.lower() for word in words]

        return self.separator.join(upper_words)



if __name__ == "__main__":
    mem_password = MemorablePasswordGenerator(5, True, "_" )
    mem_password.generate()