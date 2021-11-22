from tkinter import *
import tkinter.ttk as ttk
import random as ran
import time
game = Tk()
game.title("Scrambble")
game.geometry("800x800")
list_of_words = [["PYTHON", "MEOW", "FRANK", "HAOSH", "GIZELLE", "LYN"], ["A programming language", "Cat Sound",
                    "u know it", "multi-talented", "poker face", "hard working"]]
no_of_words = list(range(0,len(list_of_words[0])-1))

global answer_buttons
answer_buttons = []
global answer_pressed
answer_pressed = ""

#VARIABLES TO TRY
lost_value = -100
win_value = 50

#lifeline
global lifeline
lifeline = ["❤","❤","❤","❤","❤"]

#MOCKERY
mockery = ["Come on man, one more u die", "You can do it try again!", "WHAT DO U MEANN!", "u can do better!", "meow, ur answer wrong!"]

#Global variable for mixed
global mixed
mixed = ""

#shuffler
def mix_words():
    global mixed
    mixed = ""
    if (progress != win_value) and (len(lifeline) != 0):
        restart_button.pack_forget()
    hint_text_properties.config(text="")
    ans.delete(0, END)
    ans_text_properties.config(text="")
    global word_no
    global word
    word_no = (ran.choice(no_of_words))
    word= list_of_words[0][word_no]

    break_word = list(word)
    ran.shuffle(break_word)
    #print(break_word)
    mixed=break_word[0]
    for i in range(1, len(break_word)):
        mixed = mixed+" " + break_word[i]
    scrambled_text_properties.config(text=mixed)

def update_progress_bar():
    progress_bar_properties["value"] = abs(progress)
    progress_text.config(text="Progress: " +str(progress)+" %")

def check_answer():
    global progress
    if word == (ans.get()).upper():
        # ans_text_properties.config(text="You are Right!")

        #progress update
        progress+=10
        update_progress_bar()
        check_progress()
        lifeline_check()
        #time.sleep(1)
        mix_words()
    else:
        ans_text_properties.config(text=mockery[len(lifeline)-1])
        try:
            lifeline.pop()
        except:
            pass

        lifeline_check()
        

def check_progress():
    global progress

    if progress >= win_value:
        game_over_win()

def lifeline_check():

    lifeline_text = ""
    for i in lifeline:
        lifeline_text += i + " "
    lifeline_label_properties.config(text="Lifeline\n"+lifeline_text)

    if len(lifeline) == 0:
        game_over_lost()
    


def game_over_lost():
    for widget in game.winfo_children():
        widget.pack_forget()
    lose_text_properties = Label(game, text="): Game Over :(", font=("Consolas", 40))
    lose_text_properties.pack(pady=200)
    restart_button.pack()


def game_over_win():
    for widget in game.winfo_children():
        widget.pack_forget()
    lose_text_properties = Label(game, text="WOOHOOOO\n!!CONGRATSS!!\n:D", font=("Consolas", 40))
    lose_text_properties.pack(pady=200)
    restart_button.pack()

def restart():
    for widget in game.winfo_children():
        widget.pack_forget()
    global progress
    global mixed
    progress = 0
    update_progress_bar()
    global lifeline
    lifeline = ["❤","❤","❤","❤","❤"]
    mixed = ""
    
    lifeline_label_properties.pack(side=TOP, anchor=NE, padx =10)
    lifeline_check()
    progress_bar_properties.pack(pady=(30, 0))
    progress_text.pack(pady=(0,20))
    scrambled_text_properties.pack(pady=20)
    ans.pack(pady=20)
    button_frame.pack(pady=30)
    next_button.grid(row=0, column=2, padx=10)
    hint_button.grid(row=0, column=1, padx=10)
    ans_button.grid(row=0, column=0, padx=10)
    hint_text_properties.pack(pady=20, padx=00)
    ans_text_properties.pack(pady=20, padx=00)
    mix_words()

def answer_button():

def assign_letter( content, button):
        # print(self, content, button)
        answer = answer + str(content)
        generate_label()
        button.grid_forget()

        # print(len(self.button))
        if len(self.answer) == len(self.button):
            self.check_tf()
        return
    
    
    
    

def hint():
    hint_text_properties.config(text=list_of_words[1][word_no])

# lifeline_label_properties = Label(game, text="Lifeline", font=("Consolas", 15, "bold"),fg="red")
# lifeline_label_properties.pack(padx=35,side=TOP, anchor=NE)
lifeline_label_properties = Label(game, text="Lifeline\n", font=("default",15, "bold"),fg="red")
lifeline_label_properties.pack(side=TOP, anchor=NE, padx =10)


#theme for progress bar
ttk_style = ttk.Style()
ttk_style.theme_use('classic')
ttk_style.configure("red.Horizontal.TProgressbar", foreground='red', background='red')

#Progress Bar
progress_bar_properties = ttk.Progressbar(game, style="", orient=HORIZONTAL, length=300, mode='determinate')
progress_bar_properties.pack(pady=(30, 0))

#Progress
progress = 0
progress_text = Label(game, text="Progress: " + str(progress) +" %", font=("Consolas", 15))
progress_text.pack(pady=(0,20))


#scrambled word text properties 
scrambled_text_properties = Label(game, text="", font=("Consolas", 48))
scrambled_text_properties.pack(pady=20)


ans = Entry(game, text="", font=("Consolas", 12) )
ans.pack(pady=20)
#button

answer_buttons_frame =Frame(game)
for i in range(len(mixed)):
    
    answer_buttons.append(Button(
    answer_buttons_frame, text=mixed[i].upper(), command=lambda idx=i: self.assign_letter(question[idx].upper(), self.button[idx])))
    self.button[i].grid(row=1, column=i, padx=5, pady=5)

    return




button_frame = Frame(game)
button_frame.pack(pady=30)

next_button = Button(button_frame, text="Next word", command=mix_words)
next_button.grid(row=0, column=2, padx=10)

hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=1, padx=10)

ans_button = Button(button_frame, text="Submit", command=check_answer)
ans_button.grid(row=0, column=0, padx=10)
game.bind('<Return>', lambda event: check_answer())

hint_text_properties = Label(game, text="", font=("Consolas", 18))
hint_text_properties.pack(pady=20, padx=00)

ans_text_properties = Label(game, text="test", font=("Consolas", 18))
ans_text_properties.pack(pady=20, padx=00)

restart_button = Button(game, text="Restart", font=("Consolas", 30), command=restart)
restart_button.pack(pady =20)
# game.bind('<Return>', lambda event: restart())


lifeline_check()
mix_words()
game.mainloop()
