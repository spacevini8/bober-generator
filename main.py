import random

print("#################################################")
print("Welcome to kurwa animal generator extravaganza!")
print("v0.2α")
print("In loving memory of my sanity")
print("Thanks to Daniel for the idea")
print("Thanks to Leonard for the names")
print("#################################################")
print("")
print("THE ANIMAL IS:")
print("")

kurwa_mode = False

# Temporary name list, waiting for Leonard to provide the real ones
# Do your homework quicker bruh

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
elif kurwa_mode == False:
    print(selected_animal)