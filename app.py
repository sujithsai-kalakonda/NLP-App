
from tkinter import *
from mydb import Database
from tkinter import messagebox
from nlp_api import API

class NLPApp:

    def __init__(self):

        # create db object
        self.dbo = Database()

        # create api object
        self.apio = API()

        # GUI of login
        self.root = Tk() # Creating obj of Tk() and storing in root variable
        self.root.title("NLP App")
        self.root.iconbitmap('resources/favicon.ico') # Put your custom icon
        self.root.geometry('350x600')
        self.root.configure(bg='#DCDCDC')

        self.login_gui()

        self.root.mainloop() # this is there to hold the screen


    def login_gui(self):
        self.clear_screen()

        heading = Label(self.root, text="NLP App", bg='#DCDCDC', fg='#34495E')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        # Email Section
        label_1 = Label(self.root, text="Enter Email")
        label_1.pack(pady=(10,10))

        self.email_input = Entry(self.root, width=45) # Box where we enter the email (Entry class does have height parameter)
        self.email_input.pack(pady=(5,10), ipady=3)

        # Password Section:
        label_2 = Label(self.root, text="Enter Password")
        label_2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=45, show='*')  # Box where we enter the password
        self.password_input.pack(pady=(5, 10), ipady=3)

        # Login Button:
        login_button = Button(self.root, text='Login', width=25, height=2, command=self.perform_login)
        login_button.pack(pady=(10, 10))

        # Not a member? Register
        label_3 = Label(self.root, text="Not a member?", fg='#C0392B')
        label_3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text="Register Now", command=self.register_gui)
        redirect_btn.pack(pady=(10,10))


    def register_gui(self):
        self.clear_screen()

        heading = Label(self.root, text="NLP App", bg='#DCDCDC', fg='#34495E')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        # Name
        label_0 = Label(self.root, text="Enter Name")
        label_0.pack(pady=(10, 10))

        self.name_input = Entry(self.root,
                                 width=45)  # Box where we enter the email (Entry class does have height parameter)
        self.name_input.pack(pady=(5, 10), ipady=3)

        # Email Section
        label_1 = Label(self.root, text="Enter Email")
        label_1.pack(pady=(10, 10))

        self.email_input = Entry(self.root,
                                 width=45)  # Box where we enter the email (Entry class does have height parameter)
        self.email_input.pack(pady=(5, 10), ipady=3)

        # Password Section:
        label_2 = Label(self.root, text="Enter Password")
        label_2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=45, show='*')  # Box where we enter the password
        self.password_input.pack(pady=(5, 10), ipady=3)

        # Register Button:
        register_button = Button(self.root, text='Register', width=25, height=2, command=self.perform_registration)
        register_button.pack(pady=(10, 10))

        # Already a member? Login
        label_3 = Label(self.root, text="Already a member?", fg='#C0392B')
        label_3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text="Login", command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))


    def clear_screen(self):
        # Clear existing GUI
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_login(self):
        # Check whether the email exists. If so, then check password
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email, password)
        if response == 0:
            messagebox.showinfo('Success', "Login Successful")
            # Show options related to NLP
            self.home_gui()
        elif response == 1:
            messagebox.showerror("Incorrect password")
        else:
            messagebox.showerror("Email does not exists")


    def perform_registration(self):
        # fetch data which was entered while registering
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)
        if response == 0:
            messagebox.showerror("Email already exists")
        elif response == 1:
            messagebox.showinfo('Success', 'Registration successful. You can login now')
        elif response == 2:
            messagebox.showerror("Name not given")
        elif response == 3:
            messagebox.showerror("Email not given")
        else:
            messagebox.showerror("Password not given")


    def home_gui(self):
        self.clear_screen()

        # Heading
        heading = Label(self.root, text="NLP App", bg='#DCDCDC', fg='#34495E')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        # Heading 2
        heading2 = Label(self.root, text="HOME", bg='#DCDCDC', fg='#34495E')
        heading2.pack(pady=(7, 1))
        heading2.configure(font=('verdana', 20, 'bold'))

        # NER:
        ner_button = Button(self.root, text='NER (Name-Entity Recognition)', width=30, height=3, command=self.ner_analysis)
        ner_button.pack(pady=(45,20))

        # Sentiment Analysis
        sentiment_button = Button(self.root, text='Sentiment Analysis', width=30, height=3, command=self.sentiment_analysis)
        sentiment_button.pack(pady=(20,20))

        # Emotion Analysis
        emotion_button = Button(self.root, text='Emotion Analysis', width=30, height=3, command=self.emotion_analysis)
        emotion_button.pack(pady=(20,15))

        # Exit
        exit_button = Button(self.root, text='Exit', width=30, height=3, bg='#EC7063', command=self.login_gui)
        exit_button.pack(pady=(80,20))


    # GUI of NER analysis
    def ner_analysis(self):
        self.clear_screen()

        # Heading 1
        heading = Label(self.root, text="NLP App", bg='#DCDCDC', fg='#34495E')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        # Heading 2
        heading2 = Label(self.root, text="NER (Named-Entity Recognition)", bg='#DCDCDC', fg='#34495E')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 15))

        # Paragraph box:
        label_1 = Label(self.root, text="Enter the text")
        label_1.pack(pady=(20, 10))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5,10), ipady=4)

        analyse_button = Button(self.root, text="Analyse", width=10, height=1, command=self.do_ner_analysis)
        analyse_button.pack(pady=(10,10))

        self.ner_result = Label(self.root, text="", bg='#DCDCDC', fg='#34495E')
        self.ner_result.pack(pady=(10,10))
        self.ner_result.configure(font=('verdana', 20))


        # back to home
        home_button = Button(self.root, text='Home', width=10, height=1, bg='#2E86C1', command=self.home_gui)
        home_button.pack(pady=(70, 10))


    # GUI of Sentiment analysis
    def sentiment_analysis(self):
        self.clear_screen()

        # Heading 1
        heading = Label(self.root, text="NLP App", bg='#DCDCDC', fg='#34495E')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        # Heading 2
        heading2 = Label(self.root, text="Sentiment Analysis", bg='#DCDCDC', fg='#34495E')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        # Paragraph box:
        label_1 = Label(self.root, text="Enter the text")
        label_1.pack(pady=(20, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5,10), ipady=4)

        analyse_button = Button(self.root, text="Analyse", width=10, height=1, command=self.do_sentiment_analysis)
        analyse_button.pack(pady=(10,10))

        self.sentiment_result = Label(self.root, text="", bg='#DCDCDC', fg='#34495E')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('verdana', 20))


        # back to home
        home_button = Button(self.root, text='Home', width=10, height=1, bg='#2E86C1', command=self.home_gui)
        home_button.pack(pady=(70, 10))


    # GUI of Emotion Analysis
    def emotion_analysis(self):
        self.clear_screen()

        # Heading 1
        heading = Label(self.root, text="NLP App", bg='#DCDCDC', fg='#34495E')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        # Heading 2
        heading2 = Label(self.root, text="Emotion Analysis", bg='#DCDCDC', fg='#34495E')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        # Paragraph box:
        label_1 = Label(self.root, text="Enter the text")
        label_1.pack(pady=(20, 10))

        self.emotion_input = Entry(self.root, width=50)
        self.emotion_input.pack(pady=(5,10), ipady=4)

        analyse_button = Button(self.root, text="Analyse", width=10, height=1, command=self.do_emotion_analysis)
        analyse_button.pack(pady=(10,10))

        self.emotion_result = Label(self.root, text="", bg='#DCDCDC', fg='#34495E')
        self.emotion_result.pack(pady=(10,10))
        self.emotion_result.configure(font=('verdana', 20))


        # back to home
        home_button = Button(self.root, text='Home', width=10, height=1, bg='#2E86C1', command=self.home_gui)
        home_button.pack(pady=(70, 10))


    # Gets the info from ner_analysis function of API class from nlp_api.py
    def do_ner_analysis(self):
        text = self.ner_input.get()
        result = self.apio.ner_analysis(text)
        print(result)

        txt = ""
        num = 3
        for i in result['entities']:
            if num:
                # Only printing Top 3
                for j in i:
                    if (j != 'confidence_score'):
                        # Not printing the confidence_input
                        txt += f"{j} : {i[j]}" + '\n'
                txt += '\n'
                num -= 1
            else:
                break

        self.ner_result['text'] = txt

    # Gets the info from sentiment_analysis function of API class from nlp_api.py
    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)
        print(result)

        txt = ""
        for i in result['sentiment']:
            txt += f"{i} : {result['sentiment'][i]}" + '\n'


        self.sentiment_result['text'] = txt

    def do_emotion_analysis(self):

        text = self.emotion_input.get()
        result = self.apio.emotion_analysis(text)
        print(result)

        emoji = {'Fear': '😱', 'Bored': '🥱', 'Excited': '🤩', 'Angry': '😡', 'Happy': '🙂', 'Sad': '😔'}
        txt = ""

        for i in result['emotion']:
            txt += f"{i} {emoji[i]}: {result['emotion'][i]}" + '\n'

        self.emotion_result['text'] = txt



nlp = NLPApp()

# Kantara is a continuation of his engagement with regional content; he has once again experimented with the much-discussed issue of feudalism, environmental protection and forest land encroachment in general. In Kantara, he has turned his focus on folklore and the native cultures including Yakshagana, Paddana, Bhoota Kola, Daivaradhane, Naagaradhane and Kambala. The film also be viewed as a critique of the suffering of the native tribes, who have been subjected to unspeakable atrocities owing to caste hierarchy.