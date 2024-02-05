# <<<-- S.S.S GOOD LUCK
# Book started with -> "Python Programming Illustrated by William Sullivan"
# -->>>

# list
cars = ["Audi", "Mercededs", "Jaguar", "BMW"] #index like JS, start with 0.
cars[2] = "GMC" #modifying an list item using reassign trick.
print(cars[1]) #print the third, yes the third and not the second item, because we start with 0 just like JS.
cars.append("Tesla") #push an item into the list.
print(cars)

# Tuples - They use () instead of []
# They are immutables, meaning that thei value cannot change.
clubTeams = ("FC Barcelona", "Real Madrid", "Chelsea")
# this code won't work => clubTeams(2) = "Arsenal"
# because Tuples are immuatbles just like JS const.
print(clubTeams)
# done

