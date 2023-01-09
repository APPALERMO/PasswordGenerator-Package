import tkinter as tk
import tkinter.font as tkfont
from tkinter import scrolledtext
from PasswordGenerator.notifica import Notifica
from PasswordGenerator import PasswordGenerator

l_difficolta = ["1", "2", "3"]


class PasswordGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Password GUI ∼ @APPA_py on tg")
        self.geometry("750x500")
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.font_titolo = tkfont.Font(family="Verdana", size=15)
        self.variabileDifficolta = tk.StringVar()
        self.variabileDifficolta.set(" ")

        self.titolo_lunghezza = tk.Label(self, text="Lunghezza Password:", font=self.font_titolo)
        self.titolo_lunghezza.pack(anchor=tk.NW, padx=15, pady=10)

        self.lunghezza_password = tk.Entry(self)
        self.lunghezza_password.pack(anchor=tk.NW, fill=tk.BOTH, padx=15)
        self.lunghezza_password.insert(0, "0")
        self.lunghezza_password.config(validate="key", validatecommand=(self.lunghezza_password.register(self.check_int), "%P"))

        self.titolo_lunghezza = tk.Label(self, text="Difficoltà Password:", font=self.font_titolo)
        self.titolo_lunghezza.pack(anchor=tk.NW, padx=15, pady=10)

        self.conferma = tk.Button(self, text="Genera Password!", width=80, command=self.generaPassword)
        self.conferma.place(x=75, y=160)

        self.src = scrolledtext.ScrolledText(self, width=75, height=17)
        self.src.place(x=60, y=200)
        self.src.insert(tk.END, "Le tue Password verranno generate qui: ↲\n")
        self.src.config(state="disabled")

        self.bottone_pulisci = tk.Button(self, text="Pulisci\nOutput", command=lambda: (self.src.config(state="normal"), (self.src.delete(1.0, tk.END), (self.src.insert(tk.END, "Le tue Password verranno generate qui: ↲\n")), (self.src.config(state="disabled")))))
        self.bottone_pulisci.place(x=7, y=200)

        self.password_generate = tk.Label(self, text="Password\nGenerate:", font=("Verdana", 10, "bold"))
        self.password_generate.place(x=400, y=80)

        self.password_generate_quant = tk.Entry(self)
        self.password_generate_quant.place(x=490, y=90)
        self.password_generate_quant.insert(0, "1")
        self.password_generate_quant.config(validate="key", validatecommand=(self.password_generate_quant.register(self.check_int_passabout), "%P"))


        for i, livelli in enumerate(l_difficolta):
            self.checkButton = tk.Radiobutton(self, text=livelli, value=livelli, variable=self.variabileDifficolta)
            self.checkButton.pack(side=tk.LEFT, anchor=tk.NW, padx=15)


    def check_int(self, input):
        try:
            int(input)
            return True
        except ValueError:
            return False

    def check_int_passabout(self, input):
        try:
            if input == "":
                return True
            int(input)
            return True
        except ValueError:
            return False

    def generaPassword(self):
        try:
            self.livello = int(self.variabileDifficolta.get())
        except:
            Notifica("Inserimento Lunghezza password", False, "Inserisci il livello di sicurezza della Password")
        try:
            self.lunghezza = int(self.lunghezza_password.get())
            if (self.lunghezza == "0") or (self.lunghezza == 0):
                Notifica("Inserimento Lunghezza password", False, "Aggiungi la lunghezza della password")

        except:
            Notifica("Inserimento Lunghezza password", False, "Inserisci la lunghezza della password")

        try:
            quant_password = int(self.password_generate_quant.get())
            self.src.config(state="normal")

            for i in range(0, quant_password):
                password = PasswordGenerator(self.lunghezza, self.livello)
                self.src.insert(tk.END, "{}   |\n".format(password))

            self.src.config(state="disabled")
        except:
            pass
