from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

# filepaths
true_image = r"C:\Without_Sync\Py\python-100-days\Day_34\images\true.png"
false_image = r"C:\Without_Sync\Py\python-100-days\Day_34\images\false.png"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        global true_image, false_image
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="Some Question Text", fill=THEME_COLOR, font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2,
                         pady=20)  # Important for padding

        # Buttons
        true_image = PhotoImage(file=true_image)
        self.true_button = Button(
            image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file=false_image)
        self.false_button = Button(
            image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        # ScoreLevel
        self.score_level = Label(
            text="Score : 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, "normal"))
        self.score_level.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_level.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You have reached at the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
