print("Welcome to my First and Very Simple Game!")
print("")

name = ""
age = 0

while not name.strip():
    name = input("What's your name? ")

try:
    age = int(input("Hi " + name + ", how old are you? "))
except:
    print("")
    print("Ops")
    print("Nice try but we need numbers to tell your age.")

print("")

if age >= 18:
    print("Nice", name + ", once you are",  age,
          "years old, you can play this game.")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's play!")
        print("")

        health = 10

        print("Your health is 10.")

        left_or_right = input("First choice... Left or Right (left/right)? ")

        if left_or_right == "left":

            print("")
            ans = input(
                "Nice, you follow the path to reach a lake... Do you swim across or go around (across/around)? ")
            print("")

            if ans == "around":
                print("You went around and reached the other side of the lake.")

            elif ans == "across":
                print(
                    "You managed to get across, but you were bit by a poisounous fish ☠️ and lost 3 health.")
                health -= 3
                print("Your health is now", health)

            ans = input("You notice a house and a river nearby. Which do you go to (river/house)?")
            if ans == "house":
                print("")
                ans == input("You see a tall and strong man, his face is not friendly. You are getting closer to him, but before talking to him, do you get a branch on the floor or keep going anyway (branch/go)? ")

                if ans == "branch":
                    print("")
                    print("You could find a good strong branch and hid it behind you. When he saw you coming, he screamed asking what were you doing there, you tried to answer but when you saw his eyes, it was burning in anger. He came running towards you. You waited for the right moment and, when he was close enough you hit him with the branch, he passed out and fell over you making you fall over a rock, making an injury at your back, taking 4 of health from you. When you could get him off of you, you got into his house and spent the night there.")
                    health=-4
                    print("Your health is now", health)
                elif ans == "go":
                    print("")
                    print("You decided to go and talk to that strange man. He screamed asking what were you doing there, you tried to answer but when you saw his eyes, it was burning in anger. You tried to argue, but you couldn't see his fist coming into your chin making you dizzy. He then got you and throwed you into the river. However you tried, you couldn't swim, then you drowned loosing 7 of health.")
                    health=-7
                    print("Your health is now", health)

            else:
                print("")
                ans == input("This is a river with fast waters. You look back and see a tall and strong man coming after you from the house. His face is not friendly, do you jump in the river or wait for the man (jump/wait)? ")

                if ans == "jump":
                    print("")
                    print("So you jumped into the river, its fast and turbulent waters dragged you far from the edge. You swam as faster as you could but you hit your leg on a rock underwater that made a deep cut. You reached the other side of the river, but you lost a lot of blood. You lost 7 of health.")
                    health=-7
                    print("Your health is now", health)

                elif ans == "wait":
                    print("")
                    print("You decided to wait and talk to that strange man. He screamed asking what were you doing there, you tried to answer but when you saw his eyes, it was burning in anger. You tried to argue, but you couldn't see his fist coming into your chin making you dizzy. He then got you and throwed you into the river. However you tried, you couldn't swim, then you drowned loosing 7 of health.")
                    health=-7
                    print("Your health is now", health)

            if health == 0:
                print("")
                print("On no, you died!")
            else:
                print("")
                print("You win")

        else:
            print(
                "It was the harder path, so you fell down, broke your ankle and died alone...")

    elif wants_to_play == "no":
        print("Alright, see you next time.")
    else:
        print("Sorry, I didn't get what you said, so I'll understand it's a no.")
else:
    print("You're too young to play this game...")
