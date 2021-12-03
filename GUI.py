import tkinter as GUI


mainWindow = GUI.Tk()
mainWindow.title("Token Generator")
mainWindow.resizable(False,False)
mainWindow.geometry("400x400+400+0")


import actions


GeneratePasswordButton = GUI.Button(mainWindow, text="Generate",
command=actions.GeneratePasswordAction)
GeneratePasswordButton.pack()


label1 = GUI.Label(mainWindow,text="Enter Number of Token Elements")
label1.pack()

NumberOfElementInPassword = GUI.Entry(mainWindow, width=50, textvariable=actions.NumberOfPasswordElements)
NumberOfElementInPassword.pack()

label1 = GUI.Label(mainWindow,text="Here is the token")
label1.pack()

TokenEntry = GUI.Entry(mainWindow, width=50, textvariable=actions.PasswordToBeDisplayedOnEntry)
TokenEntry.pack()



mainWindow.mainloop()