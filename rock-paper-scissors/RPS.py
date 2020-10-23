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
        print("remis")
    elif player == rock:
        if computer == papper:
            print("Przegroł żech!", computer, "kryje", player)
        else:
            print("Wygrałeś!", player, "kryje", computer)
    elif player == papper:
        if computer == scissors:
            print("Przegrałeś", computer, "bije", player)
        else:
            print("Wygroł żech bo", player, "tnie", computer)
    elif player == scissors:
        if computer == rock:
            print("Przegrałeś", computer, "bije", player)
        else:
            print("Wygrana", player, "rozpierdala", computer)
    else:
        print("Nie ma takiego bicia synek!")

player = False
computer = rps[random.randint(0, 2)]
