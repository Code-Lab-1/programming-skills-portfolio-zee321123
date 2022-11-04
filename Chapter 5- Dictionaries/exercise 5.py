# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'cat',
    'name': 'puppy',
    'owner': 'zaid',
    'weight': 40,
    'eats': 'cat food',
}
pets.append(pet)

pet = {
    'animal type': 'tiger',
    'name': 'sheero',
    'owner': 'Angelina',
    'weight': 5,
    'eats': 'flesh',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'pinky',
    'owner': 'michael',
    'weight': 27,
    'eats': 'meat',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))