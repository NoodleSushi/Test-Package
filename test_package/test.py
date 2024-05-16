def greet():
    print("Hello, world!")

def kek():
    # get text file from ./data/text.txt
    with open("data/text.txt") as f:
        print(f.read())