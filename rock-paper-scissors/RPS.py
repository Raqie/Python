# rock-paper-scissors
import random
print("Welcome in Rock, Papper & Scissors game")

print("rock, papper or scissors? --->")
podanyZnak = input()

rock = "rock"
papper = "papper"
scissors = "scissors"

rps = [rock, papper, scissors]

computer = rps[random.randint(0, 2)]

player = False

while player == False:
    player = podanyZnak
    if player == computer:
        print("Tie")
    elif player == rock:
        if computer == papper:
            print("You lost!", computer, "beats", player)
        else:
            print("You Win!", player, "beats", computer)
    elif player == papper:
        if computer == scissors:
            print("Not this time pal", computer, "wins against", player)
        else:
            print("Yuppi! U win", player, "wins against", computer)
    elif player == scissors:
        if computer == rock:
            print("Sorry buddy", computer, "makes total distruction to ", player)
        else:
            print("Win", player, "destroys ", computer)
    else:
        print("Finito!")

player = False
computer = rps[random.randint(0, 2)]
