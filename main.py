# sneak water gun game
'''
1 sneak
0 water
-1gun
'''

import tkinter as tk
from tkinter import messagebox
import random
import json
import os

class SnakeWaterGunGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Water Gun Game")
        self.window.geometry("400x500")
        self.window.configure(bg="#f0f0f0")

        # Game state
        self.player_score = 0
        self.computer_score = 0
        self.choices = {
            'snake': 1,
            'water': 0,
            'gun': -1
        }
        self.reverse_choices = {
            1: "Snake",
            0: "Water",
            -1: "Gun"
        }

        # Load previous score if exists
        self.load_score()

        # Create GUI elements
        self.create_widgets()
        
        # Start the game
        self.window.mainloop()

    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.window,
            text="Snake Water Gun Game",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0"
        )
        title_label.pack(pady=20)

        # Score display
        self.score_frame = tk.Frame(self.window, bg="#f0f0f0")
        self.score_frame.pack(pady=10)
        
        self.score_label = tk.Label(
            self.score_frame,
            text=f"Score - You: {self.player_score} | Computer: {self.computer_score}",
            font=("Arial", 12),
            bg="#f0f0f0"
        )
        self.score_label.pack()

        # Choice buttons
        self.buttons_frame = tk.Frame(self.window, bg="#f0f0f0")
        self.buttons_frame.pack(pady=20)

        for choice in ['snake', 'water', 'gun']:
            btn = tk.Button(
                self.buttons_frame,
                text=choice.capitalize(),
                font=("Arial", 12),
                width=10,
                command=lambda c=choice: self.play_round(c)
            )
            btn.pack(pady=5)

        # Result display
        self.result_label = tk.Label(
            self.window,
            text="Choose your move!",
            font=("Arial", 12),
            bg="#f0f0f0"
        )
        self.result_label.pack(pady=20)

        # Control buttons
        control_frame = tk.Frame(self.window, bg="#f0f0f0")
        control_frame.pack(pady=20)

        new_game_btn = tk.Button(
            control_frame,
            text="New Game",
            font=("Arial", 12),
            command=self.new_game
        )
        new_game_btn.pack(side=tk.LEFT, padx=10)

        exit_btn = tk.Button(
            control_frame,
            text="Exit Game",
            font=("Arial", 12),
            command=self.exit_game
        )
        exit_btn.pack(side=tk.LEFT, padx=10)

        # Watermark
        watermark_frame = tk.Frame(self.window, bg="#f0f0f0")
        watermark_frame.pack(side=tk.BOTTOM, pady=10)
        
        watermark_text = "Originally created by Vaishnavi @geekyvaishnavi\nGUI updated by Pralin Khaira @pralinkhaira"
        watermark_label = tk.Label(
            watermark_frame,
            text=watermark_text,
            font=("Arial", 8),
            bg="#f0f0f0",
            fg="#666666"
        )
        watermark_label.pack()

    def play_round(self, player_choice):
        computer_choice = random.choice(list(self.choices.values()))
        player_value = self.choices[player_choice]
        
        # Update result display
        result_text = f"You chose: {player_choice.capitalize()}\nComputer chose: {self.reverse_choices[computer_choice]}"
        self.result_label.config(text=result_text)

        # Determine winner
        if computer_choice == player_value:
            result = "It's a draw!"
        elif computer_choice - player_value in [-2, 1]:
            result = "Computer wins!"
            self.computer_score += 1
        else:
            result = "You win!"
            self.player_score += 1

        # Update score display
        self.score_label.config(
            text=f"Score - You: {self.player_score} | Computer: {self.computer_score}"
        )
        
        # Show result
        messagebox.showinfo("Round Result", result)
        
        # Save score after each round
        self.save_score()

    def new_game(self):
        if messagebox.askyesno("New Game", "Are you sure you want to start a new game?"):
            self.player_score = 0
            self.computer_score = 0
            self.score_label.config(
                text=f"Score - You: {self.player_score} | Computer: {self.computer_score}"
            )
            self.result_label.config(text="Choose your move!")
            self.save_score()

    def exit_game(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit the game?"):
            self.window.quit()

    def save_score(self):
        score_data = {
            "player_score": self.player_score,
            "computer_score": self.computer_score
        }
        with open("game_score.json", "w") as f:
            json.dump(score_data, f)

    def load_score(self):
        try:
            if os.path.exists("game_score.json"):
                with open("game_score.json", "r") as f:
                    score_data = json.load(f)
                    self.player_score = score_data.get("player_score", 0)
                    self.computer_score = score_data.get("computer_score", 0)
        except:
            self.player_score = 0
            self.computer_score = 0

if __name__ == "__main__":
    game = SnakeWaterGunGame()

'''
computer - you is 1 or -2 when you are losing 
'''