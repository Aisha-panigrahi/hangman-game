

import random
def hangman():
    list_of_words = ['ATALNTICA','INDIA','MALAYSIA','MALDIVES','AMERICA']
    word = random.choice(list_of_words)
    turn = 10
    guessmade =''
    valid_entry= set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    while len(word)>0:
        main_word = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main_word = main_word + letter
            else:
                main_word = main_word +'_ '

        if main_word == word:
            print("YOU GUESSED THE CORRECT WORD:",main_word)
            print("YOU WON!!")
            break

        print("Guess the word",main_word)
        guess = input()

        if guess in valid_entry:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turn = turn-1

            if turn==9:
                print("9 turns left")
                print("------------------")

            if turn==8:
                print("8 turns left")
                print("------------------")
                print("         O        ")

            if turn==7:
                print("7 turns left")
                print("---------------------")
                print("          O          ")
                print("          |          ")

            if turn==6:
                print("6 turns left")
                print("---------------------")
                print("         \O          ")
                print("          |          ")

            if turn==5:
                print("5 turns left")
                print("---------------------")
                print("         \O/         ")
                print("          |          ")
               

            if turn==4:
                print("4 turns left")
                print("---------------------")
                print("         \O/         ")
                print("          |          ")
                print("         /           ")
                

            if turn==3:
                print("3 turns left")
                print("---------------------")
                print("         \O/         ")
                print("          |          ")
                print("         / \         ")

            if turn==2:
                print("2 turns left")
                print("---------------------")
                print("         \O/  |      ")
                print("          |          ")
                print("         / \         ")


            if turn==1:
                print("Only 1 turn left!! Your hangman is about to die!! ")
                print("---------------------")
                print("          O__|       ")
                print("         /|\         ")
                print("         / \         ")
                

            if turn==0:
                print("YOU LOOSE")
                print("HANGMAN DIED")
                break

name=input("Enter your name->")
print("WELCOME",name,"!")
print("----------------------------")
print("Try to guess the word in less than 10 attempts")
hangman()
