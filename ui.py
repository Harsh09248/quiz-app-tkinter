from tkinter import *
from quiz_brain import QuizBrain
from score_db import get_high_score, save_score

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.username = None

        self.name_prompt_window()

    def name_prompt_window(self):
        self.prompt = Tk()
        self.prompt.title("Enter Name")
        self.prompt.config(padx=20, pady=20)

        label = Label(self.prompt, text="Enter your name:", font=("Arial", 14))
        label.pack(pady=10)

        self.name_entry = Entry(self.prompt, width=30, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        submit_btn = Button(self.prompt, text="Start Quiz", command=self.get_username)
        submit_btn.pack(pady=10)

        self.prompt.mainloop()

    def get_username(self):
        self.username = self.name_entry.get().strip()
        if self.username:
            self.prompt.destroy()
            self.build_main_ui()

    def build_main_ui(self):
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=40, pady=40, bg=THEME_COLOR)
        self.window.geometry("500x600")

        high_scorer, high_score = get_high_score()

        self.high_score_label = Label(
            text=f"High Score: {high_scorer} = {high_score}",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 14, "bold")
        )
        self.high_score_label.grid(row=0, column=0, columnspan=2, sticky="w")

        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 14, "bold")
        )
        self.score_label.grid(row=0, column=1, sticky="e")

        self.canvas = Canvas(width=400, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            200, 125, width=380, text="Some question",
            fill=THEME_COLOR, font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(
            image=self.true_image, highlightthickness=0,
            command=self.true_pressed, height=100, width=100
        )
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        self.false_button = Button(
            image=self.false_image, highlightthickness=0,
            command=self.false_pressed, height=100, width=100
        )
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="That's all! Thanks for playing 🎉")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            save_score(self.username, self.quiz.score)

    def true_pressed(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        self.canvas.config(bg="green" if is_right else "red")
        self.window.after(1000, self.get_next_question)
