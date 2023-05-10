print("Hello World")
confess = False
while not confess:
    user_input = input("Admit Aniket is a Good Boy : ('y' for YES)")
    for _ in range (10):
        print("BOOM!")
    if user_input == "y" :
        confess = True
    else:
        confess = False