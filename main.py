import tkinter as tk
from tkinter import messagebox
import math

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.buttons = [[None]*3 for _ in range(3)]
        self.current_player = 'X'
        self.initialize_board()
        self.root.mainloop()

    def initialize_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=('Arial', 20), width=4, height=2,
                                                command=lambda i=i, j=j: self.play_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def play_move(self, row, col):
        if self.buttons[row][col]['text'] == "":
            self.buttons[row][col]['text'] = self.current_player
            if self.check_winner(self.current_player):
                messagebox.showinfo("Winner", f"{self.current_player} wins!")
                self.reset_board()
            elif self.check_board_full():
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.current_player == 'O':
                    self.ai_move()

    def check_winner(self, player):
        for i in range(3):
            if all(self.buttons[i][j]['text'] == player for j in range(3)) or \
                    all(self.buttons[j][i]['text'] == player for j in range(3)):
                return True
        if all(self.buttons[i][i]['text'] == player for i in range(3)) or \
                all(self.buttons[i][2 - i]['text'] == player for i in range(3)):
            return True
        return False

    def check_board_full(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text'] == "":
                    return False
        return True

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""
        self.current_player = 'X'

    def minimax(self, depth, alpha, beta, maximizing_player):
        if self.check_winner('X'):
            return -1
        if self.check_winner('O'):
            return 1
        if self.check_board_full():
            return 0

        if maximizing_player:
            max_eval = -math.inf
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j]['text'] == "":
                        self.buttons[i][j]['text'] = 'O'
                        eval = self.minimax(depth + 1, alpha, beta, False)
                        self.buttons[i][j]['text'] = ""
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = math.inf
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j]['text'] == "":
                        self.buttons[i][j]['text'] = 'X'
                        eval = self.minimax(depth + 1, alpha, beta, True)
                        self.buttons[i][j]['text'] = ""
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    def ai_move(self):
        best_move = None
        best_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text'] == "":
                    self.buttons[i][j]['text'] = 'O'
                    eval = self.minimax(0, -math.inf, math.inf, False)
                    self.buttons[i][j]['text'] = ""
                    if eval > best_eval:
                        best_eval = eval
                        best_move = (i, j)
        self.buttons[best_move[0]][best_move[1]]['text'] = 'O'
        if self.check_winner('O'):
            messagebox.showinfo("Winner", "AI wins!")
            self.reset_board()
        elif self.check_board_full():
            messagebox.showinfo("Draw", "It's a draw!")
            self.reset_board()
        else:
            self.current_player = 'X'

if __name__ == "__main__":
    TicTacToe()
