import math
import tkinter as tk
from tkinter import messagebox

# -----------------------------
# GAME LOGIC
# -----------------------------
board = [" " for _ in range(9)]  # global board

def empty_cells():
    empty_list = []              
    for i, spot in enumerate(board): #returns tuple (index , value)
        if spot == " ":          
            empty_list.append(i) 
    return empty_list            
        
def is_winner(player): 
    win_states = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(board[spot] == player for spot in combo) for combo in win_states)
    #“Return True if there exists at least one winning 
    #combination where all positions are occupied by the same player.”

def is_draw():
 return len(empty_cells()) == 0 and not is_winner("X") and not is_winner("O")


# Minimax AI
def minimax(is_maximizing):
    if is_winner("O"): #max
        return 1
    if is_winner("X"): #min human
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in empty_cells():
            board[move] = "O"
            score = minimax(False)
            board[move] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in empty_cells():
            board[move] = "X"
            score = minimax(True)
            board[move] = " "
            best_score = min(best_score, score)
        return best_score

def ai_move():
    best_score = -math.inf
    best_move = None
    for move in empty_cells():
        board[move] = "O"
        score = minimax(False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    if best_move is not None:
        board[best_move] = "O"
    

# -----------------------------
# UI (Tkinter)
# -----------------------------
root = tk.Tk()
root.title("xo")
root.resizable(False, False)

buttons = []

def update_ui():
    for i in range(9):
        buttons[i]["text"] = board[i]

def end_game():
    # Disable all buttons
    for btn in buttons:
        btn.config(state="disabled")

def handle_click(index):
    if board[index] != " ":
        return  # ignore clicking filled spot

    # Player move
    board[index] = "X"
    update_ui()

    if is_winner("X"):
        messagebox.showinfo("Game Over", "You win!")
        end_game()
        return

    if is_draw():
        messagebox.showinfo("Game Over", "It's a draw!")
        end_game()
        return

    # AI move
    ai_move()
    update_ui()

    if is_winner("O"):
        messagebox.showinfo("Game Over", "AI wins!")
        end_game()
    elif is_draw():
        messagebox.showinfo("Game Over", "It's a draw!")
        end_game()

# Create 3×3 grid buttons
frame = tk.Frame(root)
frame.pack()

for i in range(9):
    btn = tk.Button(
        frame,
        text=" ",
        font=("Arial", 32),
        width=3,
        height=1,
        command=lambda i=i: handle_click(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()