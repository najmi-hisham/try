import tkinter as tk
import random

def create_button(root, row, col):
    button = tk.Button(root, text="", width=3, height=2, bg="red", command=lambda: on_button_click(row, col, button))
    button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
    return button

def place_word(button,word):
    for word in word:
        word_length = len(word)
        mode = random.choice(["hori","verti"])

        if mode == "hori":
            row = random.randint(0,9)
            col = random.randint(0,9-word_length)
            if all(button[row][col + i]['text'] == '' for i in range(len(word))):
                    for i in range(len(word)):
                         button[row][col+i].config(text=word[i])
        else:
            row = random.randint(0,9-word_length)
            col = random.randint(0,9)
            if all(button[row + i][col]['text'] == '' for i in range(len(word))):
                for i in range(word_length):
                    button[row+i][col].config(text=word[i])

def on_button_click(row, col, button):
    global first, current

    if not first:
        first = button
        current = button
        button.config(bg="green")
        clicked.append(button)
    else:
        first_row, first_col = first.grid_info()['row'], first.grid_info()['column']
        prev_row, prev_col = current.grid_info()['row'], current.grid_info()['column']
        row, col = button.grid_info()['row'], button.grid_info()['column']

        hori = abs(col - prev_col)
        verti = abs(row - prev_row)

        if (row == prev_row and hori == 1 and first_row == row) or (col == prev_col and verti == 1 and first_col == col):
            button.config(bg="green")
            current = button
            clicked.append(button)
        else:
            reset_all()
            button.config(bg="green")
            first = button
            current = button
            clicked.append(button)
            
    text_var.set(button["text"])

def reset_all():
    for btn in clicked:
        btn.config(bg="red")
    clicked.clear()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("My Game")

    for i in range(10):
        root.columnconfigure(i, weight=1)
        root.rowconfigure(i, weight=1)

    first, current = None, None
    clicked = []

    buttons = [[create_button(root, row, col) for col in range(10)] for row in range(10)]

    word = ["GORILLA","ZEBRA","ANT","CAT","DOG","HAMSTER"]
    place_word(buttons,word)
    

    text_var = tk.StringVar()
    text_box = tk.Entry(root, textvariable=text_var, justify="center")
    text_box.grid(row=11, column=0, columnspan=10, pady=10)

    root.mainloop()
