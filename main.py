from PasswordGenerator import PasswordGenerator

password = PasswordGenerator(100, 3)
print("Your password is:", password, end="\n")

PasswordGenerator.PasswordAmount(password, 10)

PasswordGenerator.createWordList(password, "Test_WordList.txt", 20000)
