print("Hello World")
print("Life is beautiful")

confess = False
while not confess:
    user_input = input("Admit Aniket is a Good Boy ('y' for YES) : ")
    if user_input == "y" :
        confess = True
        print("\tTHANK YOU!")
    else:
        confess = False
    for _ in range (10):
        print("B-O-O-M!")

