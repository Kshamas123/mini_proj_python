#snake water gun
#Snake,water and gun is a variation of children's game "rock paper scissors" where players use hand gestures to represent the snake,water or gun.gun beats snake,water beats gun and the snake beats water
# Python program to create snake water gun game using if-else statement (no GUI used).

#symbols 0->snake,1->water,2->gun
import random
res=[['d','w','l'],['l','d','w'],['w','l','d']]
print("WELCOME TO SNAKE-WATER-GUN game")
print("rules:enter 0 if your choice is snake,1 if water and 2 for gun")
while(True):
    choice = int(input("if you want to continue enter 1 or else 0"))
    if choice==0:
        break
    l=[0,1,2]
    user=int(input("enter your choice"))
    computer=random.choice(l)
    result=res[user][computer]
    if(result=='w'):
        print("you won the game")
    elif(result=='l'):
        print("you lost the game")
    else:
        print("its a draw")
