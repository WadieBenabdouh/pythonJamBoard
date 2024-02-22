legal_age = 18
user_age = input()
# converting the input from str to integer.
converted_age = int(user_age)

# verification system using conditionals.
if legal_age < converted_age:
    print("You are allowed to access the club")
    
elif legal_age == converted_age:
    print("Perfect age amigo")
    
else :
    print("You are not allowed for entry")