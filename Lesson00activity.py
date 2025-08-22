import tkinter as tk
from tkinter import ttk, messagebox
import random

APP_TITLE = "Rock • Paper • Scissors"
CHOICES = ("Rock", "Paper", "Scissors")
RESULT_COLORS = {
    "Win": "#22c55e",     # green
    "Lose": "#ef4444",    # red
    "Draw": "#6b7280",    # gray
}

class RPSApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.resizable(False, False)
        self.configure(padx=16, pady=16)

        # State
        self.user_score = tk.IntVar(value=0)
        self.cpu_score = tk.IntVar(value=0)
        self.draws = tk.IntVar(value=0)
        self.rounds = tk.IntVar(value=0)

        self.best_of = tk.IntVar(value=5)  # default match length

        # UI
        self._build_ui()

    # ---------------- UI -----------------
    def _build_ui(self):
        header = ttk.Label(self, text=APP_TITLE, font=("Segoe UI", 18, "bold"))
        header.grid(row=0, column=0, columnspan=3, pady=(0, 12))

        # Scoreboard
        board = ttk.Frame(self)
        board.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0, 12))
        for i in range(3):
            board.columnconfigure(i, weight=1)

        ttk.Label(board, text="You", font=("Segoe UI", 12, "bold")).grid(row=0, column=0)
        ttk.Label(board, text="CPU", font=("Segoe UI", 12, "bold")).grid(row=0, column=2)
        ttk.Label(board, textvariable=self.user_score, font=("Segoe UI", 20, "bold")).grid(row=1, column=0)
        ttk.Label(board, text="-", font=("Segoe UI", 20, "bold")).grid(row=1, column=1)
        ttk.Label(board, textvariable=self.cpu_score, font=("Segoe UI", 20, "bold")).grid(row=1, column=2)

        # Last round info
        info = ttk.Frame(self)
        info.grid(row=2, column=0, columnspan=3, sticky="ew", pady=(0, 12))
        for i in range(3):
            info.columnconfigure(i, weight=1)

        self.you_pick_lbl = ttk.Label(info, text="You: —", font=("Segoe UI", 11))
        self.cpu_pick_lbl = ttk.Label(info, text="CPU: —", font=("Segoe UI", 11))
        self.result_lbl = ttk.Label(info, text="Make your move!", font=("Segoe UI", 12, "bold"))

        self.you_pick_lbl.grid(row=0, column=0, sticky="w")
        self.result_lbl.grid(row=0, column=1)
        self.cpu_pick_lbl.grid(row=0, column=2, sticky="e")

        # Choice buttons
        btns = ttk.Frame(self)
        btns.grid(row=3, column=0, columnspan=3, pady=(0, 12))
        for i, choice in enumerate(CHOICES):
            ttk.Button(btns, text=choice, width=12, command=lambda c=choice: self.play(c)).grid(row=0, column=i, padx=6)

        # Controls row: best-of, stats, reset
        controls = ttk.Frame(self)
        controls.grid(row=4, column=0, columnspan=3, sticky="ew")
        controls.columnconfigure(3, weight=1)

        ttk.Label(controls, text="Best of:").grid(row=0, column=0, padx=(0, 6))
        best_combo = ttk.Combobox(controls, width=5, state="readonly", textvariable=self.best_of,
                                  values=(1, 3, 5, 7, 9, 11))
        best_combo.grid(row=0, column=1)
        best_combo.bind("<<ComboboxSelected>>", lambda e: self.reset(match_only=True))

        self.stats_lbl = ttk.Label(controls, text=self._stats_text())
        self.stats_lbl.grid(row=0, column=2, padx=12)

        ttk.Button(controls, text="Reset Match", command=self.reset).grid(row=0, column=4)

    # -------------- Logic ---------------
    def play(self, user_pick: str):
        cpu_pick = random.choice(CHOICES)
        result = self._decide(user_pick, cpu_pick)

        # Update picks and result UI
        self.you_pick_lbl.config(text=f"You: {user_pick}")
        self.cpu_pick_lbl.config(text=f"CPU: {cpu_pick}")
        self.result_lbl.config(text=result, foreground=RESULT_COLORS.get(result, "black"))

        # Update scores
        if result == "Win":
            self.user_score.set(self.user_score.get() + 1)
        elif result == "Lose":
            self.cpu_score.set(self.cpu_score.get() + 1)
        else:
            self.draws.set(self.draws.get() + 1)

        self.rounds.set(self.rounds.get() + 1)
        self.stats_lbl.config(text=self._stats_text())

        self._check_match_end()

    def _decide(self, user: str, cpu: str) -> str:
        if user == cpu:
            return "Draw"
        wins = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
        return "Win" if wins[user] == cpu else "Lose"

    def _stats_text(self) -> str:
        return f"Rounds: {self.rounds.get()}  •  Draws: {self.draws.get()}"

    def _check_match_end(self):
        # End the match when someone reaches majority in 'best_of'
        needed = self.best_of.get() // 2 + 1
        if self.user_score.get() >= needed or self.cpu_score.get() >= needed:
            winner = "You" if self.user_score.get() > self.cpu_score.get() else "CPU"
            messagebox.showinfo(APP_TITLE, f"{winner} win the match!\nFinal Score: {self.user_score.get()} - {self.cpu_score.get()}\nDraws: {self.draws.get()}")
            self.reset(match_only=True)

    def reset(self, match_only: bool = False):
        # Reset scores and round stats; keep best_of as chosen
        self.user_score.set(0)
        self.cpu_score.set(0)
        self.draws.set(0)
        self.rounds.set(0)

        self.you_pick_lbl.config(text="You: —")
        self.cpu_pick_lbl.config(text="CPU: —")
        self.result_lbl.config(text="Make your move!", foreground="black")
        if not match_only:
            self.best_of.set(5)
        self.stats_lbl.config(text=self._stats_text())


if __name__ == "__main__":
    # Use the system theme if available
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)  # crisper text on Windows
    except Exception:
        pass

    app = RPSApp()
    app.mainloop()
