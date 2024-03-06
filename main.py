# # string
# name = "Bravo Six"
# # integer
# callSign = 141
# # float
# score = 141.0
# # boolean
# is_deployed = True

# # list
# bravo_six_squad = ["Captain Price", "Ghost Simon", "Captain MC Tavish", "Sandman"]

# # Tuple
# us_jets = ("f16", "f15", "a10")

# # dictionaries
# f16_specs = {
#     'speed' : "mach 1.0",
#     'weight' : 4000,
#     'radarRange' : 300.75,
#     'ammunition' : ["AIM-9X", "30mm cannon"]
# }
# print(f16_specs["ammunition"][1])



# QUIZ

# - First create a list of names of the 5 people you'd like to come.
guests = ["Bike", "Screwdriver", "Tactical Nokia", "BlackRed Shoes", "T-90 Shtora"]

# - Print out a personalized invitation for 3 of them using f string.
# >>>>>> print(f'...')
print(f'-welcome my {guests[0]} to the party.')
print(f'Welcome Mr {guests[1]} to the party')
print(f'Welcome RED EYES AKA {guests[4]} don\'t be like a tank eyes')

# - one of your guests can't make it (Tactical Nokia) , modify your list and replace that guest.
guests[2] = "Walmart Core Prime"
print("-walmart replace nokia", guests)


# - You found a bigger table of 3 more people, add one at the end of the list , one in the middle and one at the beginning of the list.
# - BONUS : print the length of the list now.
newGuests = ["Black Cat", "Orange Cat", "Tree of Panthers"]

guests.append(newGuests[0]) # add one at the end of the list
guests.insert(3, newGuests[1]) # one in the middle
guests.insert(0, newGuests[2]) # one at the beginning of the list
 
print("-added new elements at different location", guests)
print(len(guests))  #print the length of the list now.

# - Turns out you'll only have space for 6 people, Remove 1 random person and one specific person by their name.
import random
# because [random.randint(a, b)] a and b refer to the range.
del guests[random.randint(0, len(guests))]
del guests[0]
print(guests)



# Time to organize the party! Print out a sorted list of your friends, Now reverse the list.
guests.sort()
print(guests)
guests.reverse()
print(guests)
