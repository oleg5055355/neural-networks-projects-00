import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def insert1(data):
    if type(data)== list:
        for item in data:
            t.insert(END,item+'\n')
    else:
        t.insert(END,data+'\n')



def dictionary():
    word=ent_val.get()
    word=word.lower()
    if word in data:
       insert1(data[word])
    elif word.title() in data:
        insert1(data[word.title()])
    elif word.upper() in data:
        insert1(data[word.upper()])
    else:
        if len(get_close_matches(word,data.keys()))==0:
            insert1(["No word Found"])
        else:
            tell=tkinter.messagebox.askquestion("Word Suggestion","Is your word  "+get_close_matches(word,data.keys())[0]+"?")
        if tell == "yes":
            insert1(data[get_close_matches(word,data.keys())[0]])
        else:
            insert1("Check Word")

def clear():
    t.delete(1.0,END)
    ent.delete(0,END)
    
    dictionary





from tkinter import *
import tkinter.messagebox

root=Tk()

head=Label(root,text="Python Dictionary",bg="red",fg="white")
head.pack(fill=X)
label1=Label(root,text="Enter Word")
label1.pack(fill=X)

ent_val=StringVar()
ent=Entry(root,textvariable=ent_val)
ent.pack()

button=Button(root,text="Meaning",command=dictionary,bg="orange")
button.pack()

t=Text(root)
t.pack(fill=X)

label2=Label(root,text="Clear Screen")
label2.pack()

button2=Button(root,text="Clear",command=clear,bg="orange")
button2.pack()


root.title("Dictionary")

root.mainloop()
