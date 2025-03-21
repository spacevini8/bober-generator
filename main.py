import random

print("#################################################")
print("Welcome to polish animal generator extravaganza!")
print("v0.10α")
print("In loving memory of my sanity")
print("Developed by spacevini8")
print("Thanks to Daniel for the idea")
print("Thanks to Leonard for the names")
print("#################################################")

family_select = input("Family friendly mode ((default) Y/ n)? ")

family_mode = False
stop = False

while True:

    if family_select == "Y" or family_select == "y" or family_select == "":
        family_mode = False
    elif family_select == "N" or family_select == "n":
        family_mode = True
    else:
        print("invalid input")
        break

    print("")
    print("THE ANIMAL IS:")
    print("")

    animal_names=("Bóbr",
                "Pingwin",
                "Skunks",
                "Jeż",
                "Krowa",
                "Pies",
                "Kot",
                "Mysz",
                "Szczur",
                "Chomik",
                "Dżdżownica",
                "Ślimak",
                "Żòłw",
                "Owca",
                "Indyk",
                "Bocian",
                "Papuga"
                )

    selected_animal = random.choice(animal_names)

    if family_mode == True:
        print("kurwa " + selected_animal + "!")
        print("")
    elif family_mode == False:
        print(selected_animal)
        print("")

    again = input("Again ((default) Y/n)? ")

    if again == "Y" or again == "y" or again == "":
        print("")
        continue
    elif again == "N" or again == "n":
        break
    else:
        print("Invalid input")
        break