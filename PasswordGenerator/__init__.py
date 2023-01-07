import random
import string
import time


class PasswordGenerator():
    def __init__(self, length: int, difficulty: int):

        self.length = length
        self.difficulty = difficulty

        if self.difficulty > 3:
            raise ValueError("The difficulty of password is greater than 3")

        if self.difficulty == 1:
            chars = string.ascii_letters
            self.password = "".join(random.choice(chars) for _ in range(self.length))

        elif self.difficulty == 2:
            chars = string.ascii_letters + string.digits
            self.password = "".join(random.choice(chars) for _ in range(self.length))

        elif self.difficulty == 3:
            chars = string.ascii_letters + string.digits + string.punctuation
            self.password = "".join(random.choice(chars) for _ in range(self.length))

    def __str__(self):
        return self.password


    def PasswordAmount(self, amount: int):

        for i in range(1, amount+1):
            print("{}| {}".format(i, PasswordGenerator(self.length, self.difficulty)))


    def createWordList(self, name: str, amount: int, time_spent: bool):
        file = open(name, "w")
        file.close()

        file = open(name, "a")
        i = 1
        start = time.perf_counter()

        while i < amount+1:
            file.write(str(PasswordGenerator(self.length, self.difficulty)) + "\n")
            i += 1

        end = time.perf_counter()

        if time_spent:
            print(f"Operazione eseguita in: {(end - start):.6f} secondi")
        else:
            pass
        file.close()
