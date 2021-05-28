from tkinter import *
from random import randint
from typing_extensions import final

root = Tk()
root.title('Secure Password Generator')
root.resizable(False, False)


# functions

def generate():
    length = int(lengthEntry.get())
    password = ''

    chars = [
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '[', ']', '{', '}', '/', '\\', '|', '+']
    ]

    for i in range(length):
        random_chars_list = chars[randint(0,len(chars)-1)]
        final_char = random_chars_list[randint(0, len(random_chars_list)-1)]
        password+=final_char

    finalPassword.delete(0, 'end') 
    finalPassword.insert(0, password)
        

# labels
lengthLabel = Label(root, text='Enter length of password: ')
lengthLabel.grid(column=0, row=0)

# entries
lengthEntry = Entry(root)
lengthEntry.grid(column=1, row=0)

finalPassword= Entry(root)
finalPassword.grid(column=1, row=1)

# buttons

genButton = Button(root, text="Generate Password", bg='red', command=generate)
genButton.grid(column=0, row=1)

root.mainloop()