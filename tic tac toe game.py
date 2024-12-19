import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("500x500")  
        self.root.config(bg="#000080")  
        
        
        self.board = [' ' for _ in range(9)]
        self.current_player = "X"
        self.buttons = []

        # Title of game
        self.title_label = ttk.Label(self.root, text="Tic-Tac-Toe-Game", font=("Fantasque-Sans-Mono", 26, "bold"), background="#000080", foreground="#ffffff")
        self.title_label.grid(row=0, column=0, columnspan=3, pady=20)

        #3x3 grid
        for i in range(3):
            for j in range(3):
                button = ttk.Button(self.root, text=" ", command=lambda i=i, j=j: self.on_button_click(i, j),
                                    style="TButton", width=10)
                button.grid(row=i+1, column=j, padx=10, pady=10, sticky="nsew")
                self.buttons.append(button)

        # resizing for columsxs
        for i in range(3):
            self.root.grid_rowconfigure(i+1, weight=2)
            self.root.grid_columnconfigure(i, weight=2)

        # button styles for the 2 players
        self.style = ttk.Style()

        # button
        self.style.configure("TButton",
                             font=("Helvetica", 24, "bold"),
                             padding=10,
                             relief="flat", 
                             background="#f2f2f2",
                             foreground="#008000")

        # x and o
        self.style.configure("X.TButton", foreground="green", background="#4CAF50", font=("Helvetica", 24, "bold"))
        self.style.configure("O.TButton", foreground="green", background="#f44336", font=("Helvetica", 24, "bold"))

        # Hover =
        self.style.map("TButton", 
                       background=[("active", "#d1d1d1"), ("pressed", "#b0b0b0")])

    def on_button_click(self, i, j):
        index = i * 3 + j
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            
            if self.current_player == "X":
                self.buttons[index].config(style="X.TButton")
            else:
                self.buttons[index].config(style="O.TButton")

            if self.check_winner():
                self.end_game(f"Player {self.current_player} wins!")
            elif ' ' not in self.board:
                self.end_game("It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.reset_game()

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = "X"
        for button in self.buttons:
            button.config(text=" ", style="TButton")

def main():
    # tinker
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
