from token_generator import GeneratePassword
import tkinter

PasswordToBeDisplayedOnEntry = tkinter.StringVar()
NumberOfPasswordElements = tkinter.StringVar()

def GeneratePasswordAction():
    defaultNumberOfElement = 25
    try:
        password = GeneratePassword.generate_password(int(NumberOfPasswordElements.get()))
    except:
        password = GeneratePassword.generate_password(defaultNumberOfElement)
    
    PasswordToBeDisplayedOnEntry.set(password)


