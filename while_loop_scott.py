### we have a program to demonstrate the while loop


# import the random module
from random import randint

students_inf = int(input("how many numbers in a row would you like to hit ?: "))
students_other = randint(1,10) 

roll_number = 0
the_count = 0
the_prev_number = 0
# made a varible to catch the previous number
while the_count < students_inf and roll_number < 200000:
    the_number = randint(1,9)
    if the_number == the_prev_number:
        the_count = the_count + 1
        print(str(roll_number) + " the numbers match" + " "  + str(the_number) + " = " + str(the_prev_number))

    else: 
        the_count = 0
        print(str(roll_number) + " " + "the numbers do not match" + " "  + str(the_number) + " != " + str(the_prev_number))

    the_prev_number = the_number
    roll_number = roll_number + 1
    if roll_number == 200000:
        print("dont play the lottery")
input("press enter")