#Using the terminal, take an input of r, p or s which will stand for rock, paper, and scissors.
#Have the computer randomly pick one of these three choices.
#Compare the user's input to the computer's choice to determine if the user won, lost, or tied.
import random
options=['r','p','s']
computerChoice=random.choice(options)
print(computerChoice)
userChoice=input("Make your Choice: (r)ock,(p)aper,(s)cissors? ")

if computerChoice == userChoice:
    print("You have tied")
elif computerChoice == "r" and userChoice == "s":
    print("Rock beats scissors. Computer wins")
elif computerChoice == "r" and userChoice == "p":
    print("Paper beats rock. User wins")
elif computerChoice == "s" and userChoice =="p":
    print("Sciccors beats paper. Computer wins")
elif computerChoice =="s" and userChoice == "r":
    print("Rock beats scissors. User wins")
elif computerChoice =="p" and userChoice =="r":
    print("Paper beats rock. Computer wins")
elif computerChoice=="p" and userChoice=="s":
    print("Scissors beats paper. User wins")
