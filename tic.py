import tkinter as tk
from tkinter import messagebox

def create_widgets():
    for i in range(9):
        button = tk.Button(root, text=" ", font="Arial 20 bold", height=3, width=6,
                           command=lambda i=i: make_move(i))
        button.grid(row=i//3, column=i%3)
        buttons.append(button)

def make_move(index):
    global current_player
    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player)
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif " " not in board:
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return False

def reset_game():
    global board, current_player
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text=" ")
    current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    board = [" " for _ in range(9)]
    current_player = "X"
    buttons = []
    create_widgets()
    root.mainloop()
