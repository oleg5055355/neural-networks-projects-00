from tkinter import ttk, Tk, PhotoImage, RIDGE, END
import random
from PIL import ImageTk, Image
from demodbfile import DbOperations



class Brand:
    def __init__(self, master):
        self.master = master
        self.createDefaultFrames()
        self.home()



    def createDefaultFrames(self):
        """
            Creates The static frames, the header and the menu frames.
            This will be call only once in the application, as they are going to be static frames.
        """
        self.master.geometry('640x500+250+150')
        self.master.title('Brand Identification Game')

        # # creating a Header Frame which contains Logo and Description of the app
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()

        self.logo = PhotoImage(file='python_logo.gif').subsample(3, 3)

        ttk.Label(self.frame_header, image=self.logo).grid(
            row=0, column=0, rowspan=4)

        ttk.Label(self.frame_header, text='Welcome to Brand Identification Game!').grid(
            row=0, column=1)

        ttk.Label(self.frame_header, text='Test Your Knowledge on Brands!').grid(
            row=1, column=1)
        #
        # # Creating a Header Menu which contains Options such as - Info
        self.frame_menu = ttk.Frame(self.master)
        self.frame_menu.pack()

        ttk.Button(
            self.frame_menu, text="Home", command=self.home).grid(row=0, column=0)

        ttk.Button(
            self.frame_menu, text="Info", command=self.info).grid(row=0, column=1)

        ttk.Button(
            self.frame_menu, text="Settings", command=self.settings).grid(row=0, column=2)

        ttk.Button(
            self.frame_menu, text="High scores",command=self.high_scores).grid(row=0, column=3)

    def create_frame_body(self):
        """
        This method erases the contents of the frame body and creates a new frame body, so that
        other menus options do not overlap with old frame contents.
        """
        try:
            self.frame_body.forget()
        except:
            pass
        self.frame_body = ttk.Frame(self.master)
        self.frame_body.pack()
        self.frame_body.config(relief=RIDGE, padding=(50, 15))

    def home(self):

        self.create_frame_body()
        self.score = 0
        ttk.Label(self.frame_body, wraplength=300, text="""        Welcome to this Brand Identification Game... Score points according to your guesses.
        Click on Clues to Reveal few Clues at the cost of half of a point. Click on Play Button to start scoring. Info button for More information.""").grid(row=0, column=0)
        self.db_obj = DbOperations()
        self.questions = {}
        for i in self.db_obj.select_question():
            self.questions[i[1]] = tuple([i[2],i[3]])
        ttk.Button(self.frame_body, text="Start", command=self.play_start).grid(
            row=1, column=0, columnspan=2, rowspan=1, padx=10, pady=20)
        ttk.Button(self.frame_body, text="How to play", command=self.info).grid(
            row=2, column=0, columnspan=2, rowspan=1, padx=10, pady=20)

    def info(self):
        self.create_frame_body()
        ttk.Label(self.frame_body,text="This is the information page").pack()

    def settings(self):
        self.create_frame_body()
        ttk.Label(self.frame_body, text="You can add or remove questions according to your needs. To Add A question, click on Add button below, Provide a question, and a clue to be an image, and comma separated correct answers", wraplength=300).grid(row=0, column=0)
        ttk.Button(self.frame_body, text="Add a question",
                   command=self.add_question).grid(row=1, column=0)

    def high_scores(self):
        self.create_frame_body()
        for i in self.db_obj.select_score():
            ttk.Label(self.frame_body, text=i).pack()

    def play_start(self):
        """
            In this method we are going to get the player's name, which we will use later.
        """
        self.create_frame_body()

        ttk.Label(self.frame_body, text="Enter your name").grid(row=0, column=0)

        self.player = ttk.Entry(self.frame_body)
        self.player.grid(row=1, column=0)

        ttk.Button(self.frame_body, text="Enter",
                   command=self.play).grid(row=2, column=0)



    def add_question(self):
        """
            This method is triggered when add question button is clicked. It gets the
            user input for the question, path to image, and answer.
            When Add button is clicked, we will call the save_question method, which will
            get the entry values and save to the database.
        """
        self.create_frame_body()
        ttk.Label(self.frame_body, text="Enter the question").grid(
            row=0, column=0)

        self.question_field = ttk.Entry(self.frame_body)
        self.question_field.grid(row=0, column=1)

        ttk.Label(self.frame_body, text="Enter the path to image for clue").grid(
            row=1, column=0)

        self.path_to_image_field = ttk.Entry(
            self.frame_body)
        self.path_to_image_field.grid(row=1, column=1)

        ttk.Label(self.frame_body, text="Enter the correct answers separated by comma").grid(
            row=2, column=0)

        self.add_answer_field = ttk.Entry(
            self.frame_body)
        self.add_answer_field.grid(row=2, column=1)

        ttk.Button(self.frame_body, text="Add", command=self.save_question).grid(
            row=3, column=1, columnspan=2)

    def save_question(self):
        """
            This method is triggered when the Add button is clicked from the Add question page.
            Here we will save the user's questions and answer to the database.
        """
        self.question = self.question_field.get()
        self.path_to_image = self.path_to_image_field.get()
        self.add_answer = set([self.add_answer_field.get()])
        self.db_obj.insert_question(self.question, self.path_to_image,self.add_answer)
        self.settings()



    def next_action(self, question):

        """
            This method will be triggered after the user answers the question and hits the next button. Here the answer is evaluated
            and the score is incremented is correct.
        """
        self.answer = self.answer_object.get()
        self.answer_object.delete(0, END)

        if self.answer.strip().lower() ==self.questions[question][1]:
            self.score += 10

        self.questions.pop(question)
        self.play()

    def clue(self, question):
        """
            This method will be triggered when the user clicks on the clue button. Here we
            disable the clue button, reduce the score by 5 and display the clue image, WITHOUT
            erasing the old frame contents.
        """
        self.score -= 5
        image = Image.open(self.questions[question][0])
        image = image.resize((80, 80))

        self.image = ImageTk.PhotoImage(image)

        self.clue_button['state'] = 'disabled'

        ttk.Label(self.frame_body, image=self.image).grid(
            row=2, column=0)

    def play(self):
        """
            This method will be called repetitively until the questions become empty.
            Here we question the user, and get the user's answer, and forward the question to either
            clue and next pages when the respective buttons are clicked.
        """
        self.create_frame_body()
        if self.questions:
            question = random.choice(list(self.questions.keys()))

            ttk.Label(self.frame_body, text=question).grid(row=0, column=0)

            self.answer_object = ttk.Entry(
                self.frame_body)
            self.answer_object.grid(row=1, column=0)

            self.clue_button = ttk.Button(
                self.frame_body, text="Clue", command=lambda: self.clue(question))
            self.clue_button.grid(row=3, column=0)

            ttk.Button(self.frame_body, text="Next", command=lambda: self.next_action(
                question)).grid(row=4, column=0)
        else:
            if self.score < 0:
                self.score = 0

            self.player_name = self.player.get()
            ttk.Label(self.frame_body, text=f"You have reached the end of the game, {self.player_name}'s score is {self.score}").grid(
                row=0, column=0)
            self.db_obj.create_score(self.player_name,self.score)
            self.db_obj.select_score()
            self.score = 0
            ttk.Button(self.frame_body, text="Play Again",
                       command=self.home).grid(row=2, column=0)

root = Tk()
Brand(root)
root.mainloop()
