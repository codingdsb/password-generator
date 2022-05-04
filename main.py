import tkinter
from tkinter import messagebox
from random import randint, shuffle
import customtkinter

root = customtkinter.CTk()
root.title("Secure Password Generator")
root.geometry("650x200")
root.resizable(False, False)
customtkinter.set_appearance_mode("System")

# Constants
ENTRY_WIDTH = 400

# functions


def generate():

    # get all values
    try:
        length = int(lengthEntry.get())
        smallAlphabets = int(smallEntry.get())
        capitalAlphabets = int(capitalEntry.get())
        numbers = int(numbersEntry.get())
        specialChars = int(specialEntry.get())

        if smallAlphabets + capitalAlphabets + numbers + specialChars != length:
            messagebox.showerror(
                title="Error",
                message="The total of small alphabets, capital alphabets, numbers and special characters isn't equal to the total length of password",
            )
            return

    except Exception as e:
        messagebox.showerror(
            title="Error", message="Invalid character or empty fields found"
        )
        return

    password = ""

    chars = [
        [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ],
        [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ],
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        [
            "!",
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "*",
            "(",
            ")",
            "-",
            "[",
            "]",
            "{",
            "}",
            "/",
            "\\",
            "|",
            "+",
        ],
    ]

    for sa in range(smallAlphabets):
        character = chars[0][randint(0, len(chars[0]) - 1)]
        password += character

    for ca in range(capitalAlphabets):
        character = chars[1][randint(0, len(chars[1]) - 1)]
        password += character

    for n in range(numbers):
        character = chars[2][randint(0, len(chars[2]) - 1)]
        password += character

    for sc in range(specialChars):
        character = chars[3][randint(0, len(chars[2]) - 1)]
        password += character

    listOfPasswordChars = list(password)
    shuffle(listOfPasswordChars)
    password = "".join(listOfPasswordChars)
    finalPassword.delete(0, "end")
    finalPassword.insert(0, password)


# labels
lengthLabel = customtkinter.CTkLabel(root, text="Enter length of password: ")
lengthLabel.grid(column=0, row=0)

smallLabel = customtkinter.CTkLabel(root, text="Enter number of small alphabets:")
smallLabel.grid(column=0, row=1)

capitalLabel = customtkinter.CTkLabel(root, text="Enter number of capital alphabets:")
capitalLabel.grid(column=0, row=2)

numbersLabel = customtkinter.CTkLabel(root, text="Enter number of numeric characters: ")
numbersLabel.grid(column=0, row=3)

specialLabel = customtkinter.CTkLabel(root, text="Enter number of special characters: ")
specialLabel.grid(column=0, row=4)

# entries
lengthEntry = customtkinter.CTkEntry(root, width=ENTRY_WIDTH)
lengthEntry.grid(column=1, row=0, padx=3)
lengthEntry.focus()

smallEntry = customtkinter.CTkEntry(root, width=ENTRY_WIDTH)
smallEntry.grid(column=1, row=1, padx=3)

capitalEntry = customtkinter.CTkEntry(root, width=ENTRY_WIDTH)
capitalEntry.grid(column=1, row=2, padx=3)

numbersEntry = customtkinter.CTkEntry(root, width=ENTRY_WIDTH)
numbersEntry.grid(column=1, row=3, padx=3)

specialEntry = customtkinter.CTkEntry(root, width=ENTRY_WIDTH)
specialEntry.grid(column=1, row=4, padx=3)

finalPassword = customtkinter.CTkEntry(root, width=ENTRY_WIDTH)
finalPassword.insert(0, "Your password will come up here")
finalPassword.grid(column=1, row=5, padx=3)

# # buttons

genButton = customtkinter.CTkButton(
    root, text="Generate Password", bg="red", command=generate
)
genButton.grid(column=0, row=5)

root.mainloop()
