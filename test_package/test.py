import os
script_dir = os.path.dirname(__file__)

def greet():
    print("Hello, world!")

def kek():
    # get text file from ./data/text.txt
    text_file = os.path.join(script_dir, "data/text.txt")
    with open(text_file) as f:
        print(f.read())