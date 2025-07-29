("tribe", "langauge", "food", "festival", ("cloth", "greetings"))

cultures = [
    ("Ngas", "Ngas", "bwan", "Pusdung", ("Funkaya", "yala")),
    ("Berom", "Berom", "Gwote", "Nzem Berom", ("Ashui", "Shibyal")),
    ("Afizere", "Izere", "Tuwon Masara", "Izere Day", ("Angrari", "Mavo"))
]

# 1. Print the greeting used by the second tribe in the list.

# 2. Print the sentence:
# "The Ngas people wear Funkaya and eat bwan."

# 3. Unpack the third tuple into variables and print its festival name and popular food.

#4 what happens if you try to change the language of the first tribe?

print(cultures[1][-1][-1])
print(f"The {cultures[0][0]} people wear {cultures[0][-1][-2]} and eat {cultures[0][2]}")

popular_food, festival = cultures[2][2:4]
print("The festival is: ", festival," \n there popular food is: ", popular_food)
print("Explanation: Tuples are immutable, so their elements cannot be changed.")
