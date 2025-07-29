# ("Animal", "Sound", "Lifespan", "Habitat", ("Favorite Food", "Unique Feature"))

animals = [
    ("Lion", "Roar", 15, "Savannah", ("Meat", "Mane")),
    ("Elephant", "Trumpet", 60, "Forest", ("Grass", "Tusks")),
    ("Dolphin", "Click", 40, "Ocean", ("Fish", "Intelligence"))
]

### Questions:

1. #Print the unique feature of the second animal in the list.**

print(animals[1][4][-1])

2. #Print the sentence:** "The Lion lives in the Savannah and loves eating Meat."

print(f"The {animals[0][0]} lives in the {animals[0][3]} and loves eating {animals[0][4][-2]}")

3. #Unpack the third tuple into variables and print its habitat and sound.**

sound = animals[2][1]
habitat = animals[2][3]
print(sound)
print( habitat)

4. #What happens if you try to change the lifespan of the first animal? Test it and explain the result.**

#animals[0][2]=30
#print(animals)

print("TypeError: 'tuple' object does not support item assignment")
