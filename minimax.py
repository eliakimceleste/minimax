import tkinter as tk
from copy import deepcopy
from tkinter import messagebox
from tkinter import simpledialog

class TicTacToe(object):
    def __init__(self):
        self.contenu = [[' ' for j in range(3)] for i in range(3)]

    def __str__(self):
        res = ""
        for i in range(0, 3):
            res = res + "\n+---+---+---+\n| "
            for j in range(0, 3):
                res = res + str(self.contenu[i][j]) + " | "
        res = res + '\n+---+---+---+\n'
        return res

    def joue(self, what, x, y):
        if x < 0 or x > 2:
            return ()
        if y < 0 or y > 2:
            return ()
        if what != 'o' and what != 'x':
            return ()
        if self.contenu[x][y] == ' ':
            self.contenu[x][y] = what

    def minmax(self, joueur, autre, moi, coupsPossibles, racine):
        if self.agagne(joueur):
            if moi:
                return +1
            else:
                return -1
        if self.agagne(autre):
            if moi:
                return -1
            else:
                return +1
        if not coupsPossibles:
            return 0
        valeur = [0] * 9
        for coup in coupsPossibles:
            newPos = deepcopy(self)
            newPos.joue(joueur, coup // 3, coup % 3)
            cp = deepcopy(coupsPossibles)
            cp.remove(coup)
            valeur[coup] = newPos.minmax(autre, joueur, not moi, cp, False)
        if moi:
            v = valeur[coupsPossibles[0]]
            which = coupsPossibles[0]
            for coup in coupsPossibles:
                if valeur[coup] > v:
                    v = valeur[coup]
                    which = coup
            if racine:
                return which
            else:
                return v
        else:
            v = valeur[coupsPossibles[0]]
            which = coupsPossibles[0]
            for coup in coupsPossibles:
                if valeur[coup] < v:
                    v = valeur[coup]
                    which = coup
            if racine:
                return which
            else:
                return v

    def agagne(self, joueur):
        for i in range(0, 3):
            if self.contenu[i] == [joueur, joueur, joueur]:
                return True
        for i in range(0, 3):
            if (self.contenu[0][i] == joueur) and (self.contenu[1][i] == joueur) and (self.contenu[2][i] == joueur):
                return True
        if (self.contenu[0][0] == joueur) and (self.contenu[1][1] == joueur) and (self.contenu[2][2] == joueur):
            return True
        if (self.contenu[0][2] == joueur) and (self.contenu[1][1] == joueur) and (self.contenu[2][0] == joueur):
            return True
        return False

def choisir_symboles():
    symbole_joueur1 = input("Choisissez votre symbole ('x' ou 'o'): ").lower()
    if symbole_joueur1 not in ['x', 'o']:
        print("Symbole non valide. Choisissez 'x' ou 'o'.")
        return choisir_symboles()

    symbole_joueur2 = 'x' if symbole_joueur1 == 'o' else 'o'
    print(f"Donc l'ordi a pour symbole '{symbole_joueur2}'.")

    return symbole_joueur1, symbole_joueur2

symbole_joueur1, symbole_joueur2 = choisir_symboles()

class TicTacToeGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Tic Tac Toe")
        self.geometry("100x150")

        self.player_turn = True

        self.game = TicTacToe()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.message_box = tk.Text(self, height=2, width=30, bd=2, relief="ridge")
        self.message_box.grid(row=3, columnspan=3, sticky="ew")

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self, text="", font=('Arial', 30), width=3, height=1, bd=2, relief="ridge",
                                command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j, sticky="nsew")

        for i in range(3):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)
    def on_button_click(self, i, j):
        if self.game.contenu[i][j] == ' ' and self.player_turn:
            self.game.joue(symbole_joueur1, i, j)
            self.buttons[i][j].config(text=symbole_joueur1)
            self.player_turn = False  # Mettre à jour le tour du joueur
            if self.game.agagne(symbole_joueur1):
                self.update_message("Vous avez gagné")
                self.disable_buttons()
                self.after(2000, self.ask_play_again) #Délai de 2 secondes
                self.ask_play_again()
            elif any(' ' in row for row in self.game.contenu):
                self.after(1000, self.ordinateur_joue)
            else:
                self.update_message("Partie nulle")
                self.after(2000, self.ask_play_again) #Délai de 2 secondes
                self.ask_play_again()


            # if any(' ' in row for row in self.game.contenu):
            #     caseAjouer = self.game.minmax(symbole_joueur2, symbole_joueur1, False, self.get_available_moves(), True)
            #     self.game.joue(symbole_joueur2, caseAjouer // 3, caseAjouer % 3)
            #     self.buttons[caseAjouer // 3][caseAjouer % 3].config(text=symbole_joueur2)
            #     if self.game.agagne(symbole_joueur2):
            #         self.update_message("L'ordinateur a gagné")
            #         self.disable_buttons()
            #         self.ask_play_again()
            #         return
            # else:
            #     self.update_message("Partie nulle")
            #     self.ask_play_again()
            #     return
            
    def ordinateur_joue(self):
        caseAjouer = self.game.minmax(symbole_joueur2, symbole_joueur1, False, self.get_available_moves(), True)
        self.game.joue(symbole_joueur2, caseAjouer // 3, caseAjouer % 3)
        self.buttons[caseAjouer // 3][caseAjouer % 3].config(text=symbole_joueur2)
        self.player_turn = True  # Mettre à jour le tour du joueur
        if self.game.agagne(symbole_joueur2):
            self.update_message("L'ordinateur a gagné")
            self.disable_buttons()
            self.ask_play_again()
        elif not any(' ' in row for row in self.game.contenu):
            self.update_message("Partie nulle")
            self.ask_play_again()

    def reset_game(self):
        self.game = TicTacToe()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.update_message("")

    def get_available_moves(self):
        return [i * 3 + j for i in range(3) for j in range(3) if self.game.contenu[i][j] == ' ']

    def update_message(self, message):
        self.message_box.delete(1.0, tk.END)
        self.message_box.insert(tk.END, message)
    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)

    def ask_play_again(self):
        play_again = tk.messagebox.askyesno("Rejouer", "Voulez-vous rejouer ?")
        if play_again:
            self.reset_game()
        else:
            self.destroy()
if __name__ == "__main__":
    app = TicTacToeGUI()
    app.mainloop()
