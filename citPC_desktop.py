from tkinter import*
import json
import os
import requests
import time
import threading
from connector import connect

root=Tk()
T =None


def load_details():
    if os.path.exists("details.json"):
        with open("details.json","r") as file:
            detail = json.load(file)
            return detail
    else:
        return {"username":"","password":""}
        
def save_details(username,password):
   with open("details.json","w") as file:
       details={"username":username,"password":password}
       json.dump(details,file)

def login():
    userid= username_entery.get()
    password =password_entery.get()
    print(f"Username: {userid}, Password: {password}")
    save_details(userid,password)
    


def clear_placeholder(event,entery,placeholder):
    if entery.get()==placeholder:
        entery.delete(0,END)
        entery.config(fg='black',show="*" if entery== password_entery else '')

def add_placeholder(event,entery,placeholder):
    if entery.get=='':
        entery.insert(0,placeholder)
        entery.config(fg='grey',show='')



root.title("CITPC Connector")
root.configure(background='sky blue')



details = load_details()
username_placeholder="080bel038"
password_placeholder="1009-9100"

username = Label(root, text="Username", font=("Courier", 15))
username.pack(pady=10)
username_entery = Entry(root, bd=2, bg="light gray",font=("Courier", 15),width=30,fg='blue')
username_entery.insert(0,details.get("username"))
username_entery.bind("<FocusIn>",lambda event: clear_placeholder(event, username_entery,username_placeholder))
username_entery.bind("<FocusOut>",lambda event: add_placeholder(event, username_entery,username_placeholder))
username_entery.pack(pady=10)

password = Label(root, text="Password",font=("Courier", 15))
password.pack(pady=10)  
password_entery= Entry(root, bd=2, bg="light grey",font=("Courier", 15),width=30,fg='blue')
password_entery.insert(0,details.get("password"))
password_entery.bind("<FocusIn>",lambda event: clear_placeholder(event, password_entery,password_placeholder))
password_entery.bind("<FocusOut>",lambda event: add_placeholder(event, password_entery,password_placeholder))
password_entery.pack(pady=10)

def on_enter(event=None):
    login()
    global T
    result,status=connect(username_entery,password_entery)
    if T: T.destroy()
    T = Text(root,bg="light grey",font=("Courier", 15),height=5,width=30)
    if result==True:

        T.insert("5.3",f"Connected! Now ready to use")
        T.config(fg='green')
    else:
        if status == "WRONG CREDENTIALS":
            T.insert("5.3","Invalid Credentials")
            T.config(fg='red')
        else:
            T.insert("5.3","Connection not made! the device maynot be connected to wifi")
            T.config(fg='red')

    T.pack(pady=10)
    connectingLabel['text'] = ""

def on_enter_1(event=None):
    connectingLabel['text'] = "Connecting..."
    threading.Thread(target=on_enter).start()


connectingLabel = Label(text="",bg='skyblue',font=("Times",20))
connectingLabel.pack()
button=Button(root,text="Connect",command=on_enter_1,font=("Courier", 15),height=3,width=20,fg="green",bg="goldenrod")
button.pack(pady=10)

root.bind('<Return>',on_enter_1)

root.mainloop()