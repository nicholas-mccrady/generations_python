### This file will use if statements to determine someones 
### generation based on the year they were born
birth_year = int(input("enter your birthyear: "))
print(birth_year)


if birth_year >= 2010:
    print("you are part of gen A.")
elif birth_year >= 1995:
    print("you are part of gen Z.")
elif birth_year >= 1977:
    print("you are part of millenial.")
elif birth_year >= 1965:
    print("you are gen x.")
elif birth_year >= 1946:
    print("your are a baby boomer.")
elif birth_year >= 1925:
    print("you are part of the silent generation.")
elif birth_year == 1924:
    print("go biy a lottery ticket")


else:
    print("you are (/snicker) alive i hope.")



input("hit enter to continue")
