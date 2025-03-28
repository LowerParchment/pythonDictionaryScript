# This imports the random module
import random

# Sample dictionary
dictionary = {}

# Figure out dictionary length
amountOfValues = input("Let's make a dictionary! How many values do you want in it?\n>> ")

# Convert the length to an int
amountOfValues = int(amountOfValues)

# Add values to the dictionary
for i in range(0, amountOfValues):
    value = input("\nWhat will value "  + str(i) + " be?\n>> ") 
    dictionary["Value" + str(i)] = int(value)

# Accessing dictionary values
print("\nDictionary Values Before Changes:\n", dictionary)
print("\n")

# Get a random index
randomValueIndex = random.randint(0, amountOfValues)
# Accessing random dictionary values
for i in range(randomValueIndex, amountOfValues):
  randomValueIndex = random.randint(0, amountOfValues)
  # Print the randomly selected keys  
  print(dictionary["Value" + str(i)])
  dictionary["Value" + str(i)] = int(value + value)
  
print("\nDictionary Values After Changes:\n", dictionary)
print("\n")

print("\nPrint an entry that doesnt exist:\n")
print("ValueA:\n")
print("ValueA" in dictionary)

print("\nPrint all odd elements in an Array:\n")
array = [23, 3, 7, 4, 8]

for i in array:
    if (i % 2 == 0):
        print(i)
  
