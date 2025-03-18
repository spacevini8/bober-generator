import random

print("#################################################")
print("Welcome to kurwa animal generator extravaganza!")
print("v0.2α")
print("In loving memory of my sanity")
print("Thanks to Daniel for the idea")
print("Thanks to Leonard for the names")
print("#################################################")

kurwa_select = input("Kurwa mode (Y/n)? ")

print("")
print("THE ANIMAL IS:")
print("")

kurwa_mode = False

if kurwa_select == "Y" or kurwa_select == "y":
    kurwa_mode = True
elif kurwa_select == "N" or kurwa_select == "n" or kurwa_select == "":
    kurwa_mode = False

# Temporary name list, waiting for Leonard to provide the real ones
# Do your homework quicker bruh

while True:

    animal_names=("Bóbr",
                "Ratatuj",
                "Skunks",
                "Chomik",
                "Pingvin",
                "Krt",
                "Pies",
                "Forfiter",
                "Borsuk",
                "Jezyk")

    selected_animal = random.choice(animal_names)

    if kurwa_mode == True:
        print("kurwa " + selected_animal + "!")
        print("")
    elif kurwa_mode == False:
        print(selected_animal)
        print("")

    again = input("Again (Y/n)? ")

    if again == "Y" or again == "y" or again == "":
        print("")
        continue
    elif again == "N" or again == "n":
        break