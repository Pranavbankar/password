from tkinter import *
import bcrypt




def validate(password):
    hash =b'$2b$12$wR0pSrnCOKPqKS4JqAzROezCcXdICLDDozP67tgzklbeFeWkzgng.'  
    password = bytes(password, encoding='utf-8')
    
    if bcrypt.checkpw(password, hash):
        print('login successful')
    else:
        print('invalid password')




root = Tk()
root.geometry("300x300")

password_entry = Entry()
password_entry.pack()

button = Button(text="validate",command=lambda:validate(password_entry.get()))
button.pack()
root.mainloop()

 