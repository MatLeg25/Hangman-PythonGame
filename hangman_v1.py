import random
import os
os.system("cls || clear")

words = [
    ["jeden","dwa","trzy","sto","osiem"],
    ["Polska","Niemcy","Anglia","Czechy","Holandia"],
    ["gżegżółka","ortodoksyjny","Szczebrzeszyn","ekwiwalentny","melancholia"],
    ]

lives = 5
lives_show = [chr(2), chr(2), chr(2), chr(2), chr(2)]

#story ={" "}
#story.clear()
story =[]

#losowanie słowa z danego poziomu
def start_losowanie(): 
    poziom = input("Choose level 1,2,3  Lvl.")

    if (poziom == "1" or poziom =="2" or poziom =="3"):

        poziom = int(poziom)
        poziom = poziom -1

        random_number = random.randint(0,4)
        guess = words[poziom][random_number]

        return guess
        
    else:
        return start_losowanie()

#sprawdzanie czy litera była już wcześniej podana
def check_on_list(story, letter):
    for i in range(len(story)):
        if story[i] == letter:
            return True
        else:
            pass
    return False



def play(word, lives):
    
    #zgadywane slowo
    hangman = []
    for i in range(len(word)):
        hangman.append("_")

    user_try="go"
    good_letter=0
    count=0

    while not (user_try == "exit" or lives < 0 or good_letter == len(word)):

        os.system("cls || clear")
        print("\t\t\t")
        print(*hangman, sep=" ")
        print("\n")
        print("Lives left: ",*lives_show, sep=" ")
        print("\n")
        print("State: ",good_letter,"/", len(word),"\t Try:",count)
        print("\n")
        print("Story: ",*story, sep=" ")
        print("\n")
        user_try = input("Give a letter: ")
        count+=1

        bad_letter=0
        good_letter=0

#porównanie input uzytkownika vs szukane słowo
        for i in range(len(word)):
            if (word[i].upper() == user_try.upper()):
                hangman[i] = word[i]
            else:
                bad_letter = bad_letter+1
                check_previous = check_on_list(story, user_try)
                if bad_letter == len(word) and check_previous==False:
                    lives = lives -1
                    lives_show[lives] = "X"

            if(word[i] == hangman[i]):
                good_letter +=1

        
        #story.add(user_try)
        story.append(user_try)

    #koniec petli WHILE


#podsumowanie
    Color_start = '\x1b[1;34;40m'
    Color_end = '\x1b[0m'

    print(Color_start) #kolor start
    os.system("cls || clear")
    print("The game is over, stats: ")
    print("\n Looking words: \t",guess)
    print("\n Your results: \t",*hangman, sep=" ")
    print("\n Done: \t",good_letter,"/", len(word))
    print("\n Number of attemps: \t",count)
    print("\n\n\n\n\n\n")
    print(Color_end) #kolor koniec



#play('Codecool', 6)

guess = start_losowanie()

#guess = "napis"
guess = words[2][0] #gżegżółka

play(guess, lives)
