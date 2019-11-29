from guizero import *

def unscramble(letters):
    print(letters)

app = App(title = "Unscrambler", height=400, width=400, bg=(255, 255, 255))

Text(app, text="Enter Letters To Unscramble", size=20, color=(0, 0, 0), font="Times New Roman")

letters = TextBox(app, width=30)

PushButton(app, text="UNSCRAMBLE!", command=unscramble(letters))

app.display()