from tkinter import *

def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    return(a/b)

def mod(a,b):
    return(a%b)

def lcm(a,b):
    L= a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1

def hcf(a,b):
    H= a if a<b else b
    while H >=1 :
        if a%H == 0 and b%H == 0 :
            return H
        H-=1

def extract(text):
    l=[]
    for t in text.split(' '):
        try :
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try :
                l=extract(text)
                r=operations[word.upper()](l[0],l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'Error , please try again')
            finally :
                break
        else:
            list.delete(0,END)
            list.insert(END,'Error , please try again')

operations = {'ADD': add, 'ADDITION':add,'SUM':add,'PLUS':add,'SUBTRACT':sub,'DIFFERENCE':sub,'MINUS':sub,'SUBTRACTION':sub, 'LCM':lcm,      'HCF':hcf,'PRODUCT' : mul,'MULTIPICATION' : mul,'MULTIPLY' : mul,'DIVISION':div,'DIV':div,'DIVIDE':div,'MOD':mod,'REMAINDER':mod,'MODULUS':mod}

win = Tk()
win.geometry('550x300')
win.title('Smart Calculator')
win.configure(bg='skyblue')

l1=Label(win, text='I am a smart calculator',width=20,padx=3)
l1.place(x=190,y=10)

l2 = Label(win, text="Please Enter Instructions to execute", width=30,padx=3)
l2.place(x=160,y=100)

textin = StringVar()
e1=Entry(win , width=30 , textvariable=textin)
e1.place(x=180,y=140)

b1= Button(win , text='Execute', command=calculate)
b1.place(x=230,y=170)

list =Listbox(win , width=20, height=4)
list.place(x=200,y=200)

win.mainloop()