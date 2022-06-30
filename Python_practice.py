import random


persons_selection = input("r, p, or s?")



selection = ("r","p","s")


computer_selection=random.choices(selection)

print(computer_selection)


if (computer_selection == "r" and persons_selection == "r"):
    print("tie")
elif (computer_selection == "r" and persons_selection == "p"):
    print("winner")
elif (computer_selection == "r" and persons_selection == "s"):
    print("loser")
elif (computer_selection == "p" and persons_selection == "r"):
    print("loser")
elif (computer_selection == "p" and persons_selection == "p"):
    print("tie")
elif (computer_selection == "p" and persons_selection == "s"):
    print("winner")
elif (computer_selection == "s" and persons_selection == "p"):
    print("loser")
elif (computer_selection == "s" and persons_selection == "r"):
    print("winnerr")
elif (computer_selection == "s" and persons_selection == "s"):
    print("tie")
else:
    print("Bad Coding")
