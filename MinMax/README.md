#  — Tic-Tac-Toe with Minimax AI

A desktop Tic-Tac-Toe game built with Python and Tkinter, featuring an unbeatable AI opponent powered by the Minimax algorithm.

## Features

- Clean 3×3 grid GUI built with Tkinter
- Unbeatable AI using the Minimax algorithm
- Instant win/draw detection
- No external dependencies — runs on the Python standard library

## Requirements

- Python 3.x
- Tkinter (included with most Python installations)

## How to Run

```bash
python MinMax.py
```

## How to Play

- You play as **X**, the AI plays as **O**
- Click any empty cell to make your move
- The AI responds immediately after your move
- A popup announces the result when the game ends — win, loss, or draw

## Project Structure

```
xo.py
├── Game Logic
│   ├── empty_cells()     — returns list of available board positions
│   ├── is_winner(player) — checks all rows, columns, and diagonals
│   ├── is_draw()         — true when board is full with no winner
│   ├── minimax()         — recursive algorithm that scores every possible game state
│   └── ai_move()         — picks the move with the highest Minimax score
└── UI (Tkinter)
    ├── 3×3 button grid
    ├── handle_click()    — processes player input and triggers AI response
    ├── update_ui()       — syncs button labels with the board state
    └── end_game()        — disables all buttons after the game concludes
```

## How the AI Works

The AI uses **Minimax**, a classic game-tree search algorithm. After every player move, it simulates all possible future moves to find the outcome that maximizes its own score while minimizing the player's:

| Outcome | Score |
|---------|-------|
| AI wins | `+1`  |
| Draw    | `0`   |
| Player wins | `-1` |

Because Minimax explores the entire game tree, the AI plays perfectly — it will never lose. The best result a human player can achieve is a draw.
