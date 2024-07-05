import random


def hangman():
    word=random.choice(["solar","environment","ocean","superman","batman","forest","mountain","nation","asia","europe","pineapple","custard","science","engish","story","terminal","command","virtual"])
    validletters='abcdefghijklmnopqrstuvwxyz'
    turns=10
    guessmade=''
    
    while len(word)>0: 
        main=''
        missed=0

        for letter in word:
            if letter in guessmade:
                main = main +letter
            else:
                main = main + "_"+" "

        if main == word :
            print(main)
            print("You Win!")
            break
        
        print("Guess the word: ", main)
        guess = input()

        if guess in validletters:
            guessmade=guessmade+guess
        else :
            print("Enter a valid character / Enter in small letter")
            print("")
                
        
        if guess not in word :
            turns=turns-1
            if turns == 9 :
                print("9 attempts left")
                print(" -----------  ")
                print("")
                print("")
                print("")
            if turns == 8 :
                print("8 attempts left")
                print(" ----------- ")
                print("       O     ")
                print("")
                print("")
                print("")
            if turns == 7 :
                print(" 7 attempts left")
                print(" ----------- ")
                print("       O     ")
                print("       |     ")
                print("")
                print("")
                print("")
            if turns == 6 :
                print(" 6 attempts left")
                print(" ----------- ")
                print("       O     ")
                print("       |     ")
                print("      /      ")
                print("")
                print("")
                print("")
            if turns == 5 :
                print(" 5 attempts left")
                print(" ----------- ")
                print("       O     ")
                print("       |     ")
                print("      / \    ")
                print("")
                print("")
                print("")
            if turns == 4 :
                print(" 4 attempts left")
                print(" ----------- ")
                print("    \  O     ")
                print("       |     ")
                print("      / \    ")
                print("")
                print("")
                print("")
            if turns == 3 :
                print(" 3 attempts left")
                print(" ----------- ")
                print("    \  O  /  ")
                print("       |     ")
                print("      / \    ")
                print("")
                print("")
                print("")
            if turns == 2 :
                print(" 2 attempts left")
                print(" ----------- ")
                print("    \  O |/  ")
                print("       |     ")
                print("      / \    ")
                print("")
                print("")
                print("")
            if turns == 1 :
                print(" 1 attempts left")
                print("Last breaths counting , Take care!")
                print(" ----------- ")
                print("    \  O_|/  ")
                print("       |     ")
                print("      / \    ")
                print("")
                print("")
                print("")
            if turns == 0 :
                print(" You Lost")
                print("You let a kind man die")
                print(" ----------- ")
                print("       O_|   ")
                print("    /  |  \  ")
                print("      / \    ")
                print("")
                print("")
                print("")
                break



name= input("Enter Your Name")
print("Welcome ",name)
print("---------------------")
print("Before finishing 10 attempts guess the word")
hangman()
print("")
