from PasswordGenerator import PasswordGenerator
from PasswordGenerator.gui import PasswordGUI

password = PasswordGenerator(100, 3)
print("Your password is:", password, end="\n")

PasswordGenerator.PasswordAmount(password, 10)
PasswordGenerator.createWordList(password, "Test_WordList.txt", 20000)

print("GUI Avviata")
PasswordGUI().mainloop()
print("GUI Chiusa")
