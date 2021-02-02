import random
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
'''
ms = float(input('Enter your MATH score : '))
es = float(input('Enter your English score : '))

if int(ms) > 100 or int(ms) < 0:
    ms = input('Are you kidding me?????????\nThe score must between 0-100\n\nEnter your MATH score : ')
elif int(es) > 100 or int(es) < 0:
    es = input('Are you kidding me?????????\nThe score must between 0-100\n\nEnter your English score : ')

if int(ms) == 100 or int(es) == 100:
    print('\nprize')
elif ms>=90 and es>=90:
    print('\nprize')
else:
    print('\nnone')
'''
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
'''
ans = random.randint(1,10)
gus = input("Please guess a number that I'm thinking : ")
if int(gus) == int(ans):
    print("Congratulations! You're CORRECT")
else:
    print("Sorry~ You're WRONG (The ans is : {})".format(str(ans)))
'''
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
'''
ans = random.randint(1,10)

while True:
    gus = input("Please guess a number that I'm thinking : ")
    if int(gus) == int(ans):
        print("Congratulations! You're CORRECT (The ans is : {})".format(str(ans)))
        break
    else:
        print("Sorry~ You're WRONG")
'''
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#

def game():

    time = 5
    ans = random.randint(1,20)

    for i in range(5):
        
        print("--------------------------------------------------------------")
        gus = int(input("You still have {} chance(s) \nPlease guess the number that I'm thinking (1 to 20) : ".format(str(time))))
        
        if gus == ans:
            print('')
            print("--------------------------------------------------------------")
            print("\nCongratulations! You guess the CORRECT number (ans : {})".format(str(ans)))
            time -= 1
            break
        
        elif gus > ans:
            print('\nSorry~ You guess the Wrong number')
            print("THE NUMBER YOU GUESS IS TOO BIG")
            print('')
            time -= 1
        
        elif gus < ans:
            print('\nSorry~ You guess the Wrong number')
            print("the number you guess is too small")
            print('')
            time -= 1
        
        if time == 0:
            print("--------------------------------------------------------------")
            print("\nPoor you ~ You have already used all the chances I give to you\nThe ans is : {}".format(str(ans)))
        
        
    print("\nThe Game is Over\n\nYou have totaly guessed {} time(s)".format(str(5-time)))


yn = input("Do you want to play a game with me?\nIt's a game about guess number\n\n1(Yes) or 2(No) : ")

if int(yn) == 1 :
    print('')
    game()
else:
    print('\nThan Bye-Bye ~')

