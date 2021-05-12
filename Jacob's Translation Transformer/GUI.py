from tkinter import *
from Translator import translateMe

class App(Tk):
    
    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.currentLanguage = None

        for frame in (Home, Learn, Translate):
            newFrame = frame(container, self)
            self.frames[frame] = newFrame
            newFrame.grid(row = 0, column = 0, sticky ="nsew") 

        self.show_frame(Home)
        
    def show_frame(self, cont):
        newFrame = self.frames[cont]
        newFrame.tkraise()

    def translate(self, txt, translatedToText, language, isClicked):
        isClicked = True
        langCodeDict = {
            "Chinese": "zh-CN",
            "French": "fr",
            "German": "de",
            "Japanese": "ja",
            "Russian": "ru",
            "Spanish": "es",
            "Thai": 'th'
        }
        langCode = langCodeDict[language.get()]

        translatedToText.configure(state='normal')
        if isClicked:
            Translate.question.place(rely=0.83, relx=0.5, anchor=CENTER)
            
        if not txt:
            translatedToText.delete("1.0", END)

        else:
            translatedToText.delete("1.0", END)
            translatedToText.insert(END, translateMe(txt, langCode))

        translatedToText.configure(state='disabled')
       
    def getCurrentLanguage(self, var):
        currentLanguage = Translate.currL.get()
        var.set(f"Check out these fundamentals when learning {currentLanguage}.")

    def mult_funcs(self, *funcs):
        def func(*args, **kwargs):
            val = None
            for function in funcs:
                val = function(*args, **kwargs)
            return val
        return func

class Home(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        learnButton = Button(self, text="Learn", command= lambda : controller.show_frame(Learn))
        learnButton.place(rely=0.4, relx=0.5, anchor=CENTER)

        translateButton = Button(self, text="Translate", command= lambda : controller.show_frame(Translate))
        translateButton.place(rely=0.5, relx=0.5, anchor=CENTER)

        nav = Menubutton(self, text="Navigate", relief=RAISED)

        nav.menu = Menu(nav, tearoff=0)
        nav["menu"] = nav.menu



        nav.menu.add_command(label="Learn", command= lambda : controller.show_frame(Learn))
        nav.menu.add_command(label="Translate", command= lambda : controller.show_frame(Translate))

        nav.place(rely=0, relx=1, x=0, y=0, anchor=NE)

class Learn(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        nav = Menubutton(self, text="Navigate", relief=RAISED)

        nav.menu = Menu(nav, tearoff=0)
        nav["menu"] = nav.menu

        nav.menu.add_command(label="Home", command= lambda : controller.show_frame(Home))
        nav.menu.add_command(label="Translate", command= lambda : controller.show_frame(Translate))

        nav.place(rely=0, relx=1, x=0, y=0, anchor=NE)

        Learn.learnGreet = StringVar()
        title = Label(self, textvariable=Learn.learnGreet)
        title.place(relx=0.5, rely=0.3, x=0, y=0, anchor=CENTER)

        #b = Button(self, text="Tell me More", command =lambda :  controller.getCurrentLanguage(learnGreet))
        #b.pack()

        info = Text(self, height=3, width=45)
        info.insert(END,"This is where I will use my team member's microservice to display additional info about the language")
        info.configure(state="disabled")
        info.place(relx=0.5, rely=0.4, x=0, y=0, anchor=CENTER)

class Translate(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.isClicked = False

        nav = Menubutton(self, text="Navigate", relief=RAISED)
        nav.menu = Menu(nav, tearoff=0)
        nav["menu"] = nav.menu
        nav.menu.add_command(label="Learn", command= lambda : controller.show_frame(Learn))
        nav.menu.add_command(label="Home", command= lambda : controller.show_frame(Home))
        nav.place(rely=0, relx=1, x=0, y=0, anchor=NE)

        translateHeader = Label(self, text="Enter the text you want translated here!")
        translateHeader.pack(side=TOP)

        textEnter = Text(self, height=6, width=50)
        textEnter.pack(pady=10)
        textEnter.focus()

        translatedHeader = Label(self, text="Select a Language to translate to:")
        translatedHeader.place(rely=0.45, relx=0.4, anchor=CENTER)

        languageOptions = [
            "Chinese",
            "French",
            "German",
            "Japanese",
            "Russian",
            "Spanish",
            "Thai"
        ]

        language = StringVar()
        language.set("Spanish")

        Translate.currL = language

        dropdown = OptionMenu(self, language, *languageOptions)
        dropdown.place(rely=0.45, relx=0.73, anchor=CENTER)

        translatedToText = Text(self, height=6, width=50)
        translatedToText.place(rely=0.63, relx=0.5, anchor=CENTER)
        
        Translate.questionToolTip = Label(self, text='', bd=1, relief=SUNKEN, anchor=E)
        Translate.questionToolTip.pack(fill=X, side=BOTTOM)
        Translate.question =  Translate.question = Button(self, text=u'\u003F', command= lambda : controller.mult_funcs(controller.getCurrentLanguage(Learn.learnGreet), controller.show_frame(Learn)))
        Translate.question.bind("<Enter>", self.hover)
        Translate.question.bind("<Leave>", self.leave)
        

        submit = Button(self, text="Translate", command= lambda : controller.translate(textEnter.get("1.0", 'end-1c'), translatedToText, language, self.isClicked))
        submit.place(rely=.9, relx=.85, x=0, y=0, anchor=S)

    def hover(self, e):
        Translate.questionToolTip.config(text=f"Click the ? icon to learn more about the {Translate.currL.get()} language.")
    
    def leave(self, e):
        Translate.questionToolTip.config(text=f"")

    

app = App()
app.geometry("400x400")
app.mainloop()

# I used and manipulated the code from https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/ as my boilerplate for my app to have the appearance of a multiple page app