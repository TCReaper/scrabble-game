# import modules needed
import tkinter as tk
import storymenu as storymenu
import game_over as game_over

# write the new window function which
# will be called when button pressed

font_used = "Consolas"
padding = 30


class MainMenu(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Frank's Scrabble Game")
        self.configure(background="white")
        self.geometry('800x800')
        self.iconbitmap('img/favicon.ico')
        # Full Screen
        self.fullScreenState = True
        try:
            # The code for the fullscreen function was taken from the code found at 
            # https://www.delftstack.com/howto/python-tkinter/how-to-create-full-screen-window-in-tkinter/ 
            self.attributes('-fullscreen', self.fullScreenState)
            self.bind("<F11>", lambda event: self.attributes(
                "-fullscreen", not self.attributes("-fullscreen")))
            self.bind("<Escape>", lambda event: self.attributes(
                "-fullscreen", False))
        except:
            pass

        self.answer_label = tk.Label(self, text="\nWelcome to Scrabble!", background="white", font=(
            font_used, 40), width=20)
        self.answer_label.pack(pady=padding)

        # creating the meow picture
        self.bg_image2 = tk.PhotoImage(file="img/meow_easy.png")
        self.label2 = tk.Label(
            self,
            image=self.bg_image2,
        )
        self.label2.pack(pady=padding)

        button = tk.Button(self, text="MEOW!", font=(
            font_used, 30),
            command=lambda: self.init_game())
        button.pack(pady=padding)

        self.difficulty = "easy"

        self.difficulty_button = tk.Button(self, text="Difficulty: " + self.difficulty.capitalize(), font=(
            font_used, 25),
            command=lambda: self.change_difficulty())
        self.difficulty_button.pack(pady=padding)

        quit_button = tk.Button(self, text="Quit", font=(
            font_used, 20),
            command=lambda: self.credit_window())
        quit_button.pack(pady=padding)
        self.mainloop()

    def credit_window(self):
        self.destroy()
        game_over.GameOver(False)

    def change_difficulty(self):
        if self.difficulty == 'easy':
            self.difficulty = "medium"

        elif self.difficulty == 'medium':
            self.difficulty = "hard"
        elif self.difficulty == "hard":
            self.difficulty = "asian"
        elif self.difficulty == "asian":
            self.difficulty = "easy"
        else:
            self.difficulty = "easy"
        self.update_difficulty()

    def update_difficulty(self):
        string = "img/meow_" + self.difficulty + ".png"
        self.bg_image2.config(file=string)
        self.label2.config(image=self.bg_image2)

        self.difficulty_button.config(
            text="Difficulty: " + self.difficulty.capitalize())
        f = open('difficulty.txt', 'w')
        f.write(self.difficulty)
        f.close()

    def init_game(self):
        self.destroy()
        storymenu.StoryMenu()
