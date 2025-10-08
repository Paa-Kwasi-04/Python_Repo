"""
Number Guessing Game - Tkinter GUI
----------------------------------
A graphical interface for the number guessing game with leaderboard.
Uses the backend functions from main.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
from main import csv_read, csv_write, score_ranking, computer_number, player_guess


class NumberGuessingGame:
    """
    GUI for the Number Guessing Game.
    
    Uses backend logic from main.py for game mechanics and database operations.
    """

    def __init__(self, root):
        """
        Initialize the game GUI.
        
        Parameters
        ----------
        root : tk.Tk
            The root tkinter window
        """
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("600x750")
        self.root.resizable(False, False)

        # Game state variables
        self.player_name = ""
        self.computer_number = 0
        self.attempts = 0
        self.max_attempts = 20
        self.min_range = 1
        self.max_range = 100
        self.game_active = False
        self.total_rounds = 0

        # Configure style
        self.setup_styles()

        # Create GUI
        self.create_start_screen()

    def setup_styles(self):
        """Configure visual styles."""
        self.bg_color = "#f0f4f8"
        self.primary_color = "#3498db"
        self.success_color = "#2ecc71"
        self.danger_color = "#e74c3c"
        self.warning_color = "#f39c12"

        self.root.configure(bg=self.bg_color)

    def get_leaderboard(self):
        """Get top 10 players sorted by lowest score using backend."""
        try:
            db = csv_read()
            if db.empty:
                return []

            # Group by name and get minimum score for each player
            leaderboard = db.groupby(
                'Name')['Score'].min().sort_values().head(10)
            return [(name, score) for name, score in leaderboard.items()]
        except:
            return []

    def create_start_screen(self):
        """Create the initial start screen."""
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Main container
        container = tk.Frame(self.root, bg=self.bg_color)
        container.pack(expand=True, fill=tk.BOTH, padx=40, pady=40)

        # Title
        title_label = tk.Label(
            container,
            text="🎯 NUMBER GUESSING GAME",
            font=("Arial", 24, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        )
        title_label.pack(pady=(0, 10))

        subtitle = tk.Label(
            container,
            text="Can you guess the secret number?",
            font=("Arial", 12),
            bg=self.bg_color,
            fg="#7f8c8d"
        )
        subtitle.pack(pady=(0, 30))

        # Name entry frame
        name_frame = tk.Frame(container, bg=self.bg_color)
        name_frame.pack(pady=20)

        tk.Label(
            name_frame,
            text="Enter Your Name:",
            font=("Arial", 14, "bold"),
            bg=self.bg_color
        ).pack(pady=(0, 10))

        self.name_entry = tk.Entry(
            name_frame,
            font=("Arial", 16),
            width=25,
            relief=tk.SOLID,
            borderwidth=2
        )
        self.name_entry.pack(ipady=8)
        self.name_entry.focus()
        self.name_entry.bind('<Return>', lambda e: self.start_game())

        # Game settings frame
        settings_frame = tk.LabelFrame(
            container,
            text="Game Settings",
            font=("Arial", 12, "bold"),
            bg="white",
            relief=tk.SOLID,
            borderwidth=2
        )
        settings_frame.pack(pady=20, fill=tk.X)

        settings_inner = tk.Frame(settings_frame, bg="white")
        settings_inner.pack(padx=20, pady=15)

        # Range settings
        tk.Label(
            settings_inner,
            text=f"Range: {self.min_range} - {self.max_range}",
            font=("Arial", 11),
            bg="white"
        ).grid(row=0, column=0, sticky=tk.W, pady=5)

        tk.Label(
            settings_inner,
            text=f"Max Attempts: {self.max_attempts}",
            font=("Arial", 11),
            bg="white"
        ).grid(row=1, column=0, sticky=tk.W, pady=5)

        # Start button
        start_btn = tk.Button(
            container,
            text="START GAME",
            font=("Arial", 16, "bold"),
            bg=self.success_color,
            fg="white",
            relief=tk.RAISED,
            borderwidth=3,
            command=self.start_game,
            cursor="hand2"
        )
        start_btn.pack(pady=20, ipadx=20, ipady=10)

        # Leaderboard button
        leaderboard_btn = tk.Button(
            container,
            text="VIEW LEADERBOARD",
            font=("Arial", 12, "bold"),
            bg=self.primary_color,
            fg="white",
            relief=tk.RAISED,
            borderwidth=2,
            command=self.show_leaderboard,
            cursor="hand2"
        )
        leaderboard_btn.pack(pady=10, ipadx=15, ipady=8)

    def start_game(self):
        """Start a new game."""
        name = self.name_entry.get().strip().capitalize()

        if not name:
            messagebox.showwarning(
                "Name Required", "Please enter your name to start!")
            return

        self.player_name = name
        self.attempts = 1
        self.total_rounds = 0
        self.create_game_screen()
        self.new_round()

    def create_game_screen(self):
        """Create the main game screen."""
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Main container
        container = tk.Frame(self.root, bg=self.bg_color)
        container.pack(expand=True, fill=tk.BOTH, padx=30, pady=30)

        # Header
        header = tk.Frame(container, bg=self.primary_color, height=80)
        header.pack(fill=tk.X, pady=(0, 20))
        header.pack_propagate(False)

        tk.Label(
            header,
            text=f"Welcome, {self.player_name}!",
            font=("Arial", 18, "bold"),
            bg=self.primary_color,
            fg="white"
        ).pack(pady=(10, 5))

        self.round_label = tk.Label(
            header,
            text="Round: 1",
            font=("Arial", 12),
            bg=self.primary_color,
            fg="white"
        )
        self.round_label.pack()

        # Game info
        info_frame = tk.Frame(container, bg="white",
                              relief=tk.SOLID, borderwidth=2)
        info_frame.pack(fill=tk.X, pady=10)

        info_inner = tk.Frame(info_frame, bg="white")
        info_inner.pack(pady=15)

        self.attempts_label = tk.Label(
            info_inner,
            text=f"Attempts: 1/{self.max_attempts}",
            font=("Arial", 14, "bold"),
            bg="white",
            fg=self.primary_color
        )
        self.attempts_label.pack()

        tk.Label(
            info_inner,
            text=f"Guess a number between {self.min_range} and {self.max_range}",
            font=("Arial", 11),
            bg="white",
            fg="#7f8c8d"
        ).pack(pady=(5, 0))

        # Feedback area
        self.feedback_label = tk.Label(
            container,
            text="Make your first guess!",
            font=("Arial", 14, "bold"),
            bg=self.bg_color,
            fg=self.primary_color,
            wraplength=500,
            height=3
        )
        self.feedback_label.pack(pady=15)

        # Guess entry
        guess_frame = tk.Frame(container, bg=self.bg_color)
        guess_frame.pack(pady=10)

        self.guess_entry = tk.Entry(
            guess_frame,
            font=("Arial", 20, "bold"),
            width=15,
            relief=tk.SOLID,
            borderwidth=2,
            justify=tk.CENTER
        )
        self.guess_entry.pack(ipady=10)
        self.guess_entry.focus()
        self.guess_entry.bind('<Return>', lambda e: self.check_guess())

        # Guess button
        guess_btn = tk.Button(
            container,
            text="SUBMIT GUESS",
            font=("Arial", 14, "bold"),
            bg=self.primary_color,
            fg="white",
            relief=tk.RAISED,
            borderwidth=3,
            command=self.check_guess,
            cursor="hand2"
        )
        guess_btn.pack(pady=15, ipadx=20, ipady=10)

        # Action buttons frame
        action_frame = tk.Frame(container, bg=self.bg_color)
        action_frame.pack(pady=10)

        tk.Button(
            action_frame,
            text="New Round",
            font=("Arial", 10),
            bg=self.warning_color,
            fg="white",
            command=self.new_round,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5, ipadx=10, ipady=5)

        tk.Button(
            action_frame,
            text="End Game",
            font=("Arial", 10),
            bg=self.danger_color,
            fg="white",
            command=self.end_game,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5, ipadx=10, ipady=5)

        tk.Button(
            action_frame,
            text="Leaderboard",
            font=("Arial", 10),
            bg="#95a5a6",
            fg="white",
            command=self.show_leaderboard,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5, ipadx=10, ipady=5)

    def new_round(self):
        """Start a new round using backend computer_number function."""
        self.computer_number = computer_number(self.min_range, self.max_range)
        self.total_rounds += 1
        self.game_active = True

        self.round_label.config(text=f"Round: {self.total_rounds}")
        self.feedback_label.config(
            text="New round started! Make your guess!",
            fg=self.primary_color
        )
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

    def check_guess(self):
        """Check the player's guess."""
        if not self.game_active:
            messagebox.showinfo(
                "Start Round", "Click 'New Round' to start playing!")
            return

        try:
            guess = int(self.guess_entry.get())

            if not (self.min_range <= guess <= self.max_range):
                messagebox.showwarning(
                    "Invalid Range",
                    f"Please enter a number between {self.min_range} and {self.max_range}"
                )
                return

            if guess == self.computer_number:
                self.feedback_label.config(
                    text=f"🎉 CORRECT! You guessed {guess}!\nWould you like to play another round?",
                    fg=self.success_color
                )
                self.game_active = False
                self.guess_entry.delete(0, tk.END)

            elif self.attempts >= self.max_attempts:
                self.feedback_label.config(
                    text=f"❌ Game Over! You've used all {self.max_attempts} attempts.\nThe number was {self.computer_number}",
                    fg=self.danger_color
                )
                self.game_active = False
                self.guess_entry.delete(0, tk.END)

            elif guess > self.computer_number:
                self.attempts += 1
                self.attempts_label.config(
                    text=f"Attempts: {self.attempts}/{self.max_attempts}")
                self.feedback_label.config(
                    text=f"📉 {guess} is too HIGH! Try a lower number.",
                    fg=self.danger_color
                )
                self.guess_entry.delete(0, tk.END)
                self.guess_entry.focus()

            else:
                self.attempts += 1
                self.attempts_label.config(
                    text=f"Attempts: {self.attempts}/{self.max_attempts}")
                self.feedback_label.config(
                    text=f"📈 {guess} is too LOW! Try a higher number.",
                    fg=self.warning_color
                )
                self.guess_entry.delete(0, tk.END)
                self.guess_entry.focus()

        except ValueError:
            messagebox.showerror(
                "Invalid Input", "Please enter a valid number!")
            self.guess_entry.delete(0, tk.END)

    def end_game(self):
        """End the game and save score using backend csv_write."""
        response = messagebox.askyesno(
            "End Game",
            f"Are you sure you want to end the game?\nYour score will be saved as {self.attempts} attempts."
        )

        if response:
            csv_write(self.player_name, self.attempts)
            messagebox.showinfo(
                "Thanks for Playing!",
                f"Your score of {self.attempts} attempts has been saved!\n\nCheck the leaderboard to see how you rank!"
            )
            self.create_start_screen()

    def show_leaderboard(self):
        """Display the leaderboard in a new window."""
        leaderboard_window = tk.Toplevel(self.root)
        leaderboard_window.title("Leaderboard")
        leaderboard_window.geometry("400x500")
        leaderboard_window.resizable(False, False)
        leaderboard_window.configure(bg=self.bg_color)

        # Title
        title = tk.Label(
            leaderboard_window,
            text="🏆 LEADERBOARD",
            font=("Arial", 20, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        )
        title.pack(pady=20)

        # Leaderboard frame
        lb_frame = tk.Frame(leaderboard_window, bg="white",
                            relief=tk.SOLID, borderwidth=2)
        lb_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Headers
        header_frame = tk.Frame(lb_frame, bg=self.primary_color)
        header_frame.pack(fill=tk.X)

        tk.Label(
            header_frame,
            text="Rank",
            font=("Arial", 12, "bold"),
            bg=self.primary_color,
            fg="white",
            width=8
        ).pack(side=tk.LEFT, padx=5, pady=10)

        tk.Label(
            header_frame,
            text="Name",
            font=("Arial", 12, "bold"),
            bg=self.primary_color,
            fg="white",
            width=20
        ).pack(side=tk.LEFT, padx=5, pady=10)

        tk.Label(
            header_frame,
            text="Score",
            font=("Arial", 12, "bold"),
            bg=self.primary_color,
            fg="white",
            width=8
        ).pack(side=tk.LEFT, padx=5, pady=10)

        # Scrollable content
        canvas = tk.Canvas(lb_frame, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(
            lb_frame, orient="vertical", command=canvas.yview)
        content_frame = tk.Frame(canvas, bg="white")

        content_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Get leaderboard data using backend
        leaderboard = self.get_leaderboard()

        if not leaderboard:
            tk.Label(
                content_frame,
                text="No scores yet!\nBe the first to play!",
                font=("Arial", 14),
                bg="white",
                fg="#7f8c8d"
            ).pack(pady=50)
        else:
            for rank, (name, score) in enumerate(leaderboard, 1):
                row_frame = tk.Frame(content_frame, bg="white")
                row_frame.pack(fill=tk.X, pady=2)

                # Medal for top 3
                medal = ""
                if rank == 1:
                    medal = "🥇"
                elif rank == 2:
                    medal = "🥈"
                elif rank == 3:
                    medal = "🥉"

                tk.Label(
                    row_frame,
                    text=f"{medal} {rank}",
                    font=("Arial", 11, "bold" if rank <= 3 else "normal"),
                    bg="white",
                    width=8
                ).pack(side=tk.LEFT, padx=5, pady=5)

                tk.Label(
                    row_frame,
                    text=name,
                    font=("Arial", 11, "bold" if rank <= 3 else "normal"),
                    bg="white",
                    width=20,
                    anchor=tk.W
                ).pack(side=tk.LEFT, padx=5, pady=5)

                tk.Label(
                    row_frame,
                    text=str(score),
                    font=("Arial", 11, "bold" if rank <= 3 else "normal"),
                    bg="white",
                    fg=self.success_color if rank <= 3 else "black",
                    width=8
                ).pack(side=tk.LEFT, padx=5, pady=5)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Close button
        close_btn = tk.Button(
            leaderboard_window,
            text="CLOSE",
            font=("Arial", 12, "bold"),
            bg=self.primary_color,
            fg="white",
            command=leaderboard_window.destroy,
            cursor="hand2"
        )
        close_btn.pack(pady=15, ipadx=20, ipady=8)


def main():
    """Main entry point for the GUI application."""
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()


if __name__ == '__main__':
    main()
