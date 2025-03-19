import random

print("#################################################")
print("Welcome to polish animal generator extravaganza!")
print("v0.2α")
print("In loving memory of my sanity")
print("Thanks to Daniel for the idea")
print("Thanks to Leonard for the names")
print("#################################################")

print("")
print("THE ANIMAL IS:")
print("")

while True:

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

    print(selected_animal)
    print("")

    again = input("Again (Y/n)? ")

    if again == "Y" or again == "y" or again == "":
        print("")
        continue
    elif again == "N" or again == "n":
        break