import random

#What did you see on line 1?
# 7
#What was the smallest number you could have seen, what was the largest?
# 5 was the smallest possible integer, 20 was the largest possible integer

#What did you see on line 2?
# 9
#What was the smallest number you could have seen, what was the largest?
# 3 was the smallest possible integer, 9 was the largest
#Could line 2 have produced a 4?
# No, as this coded only outputs odd numbers (as it produces integers in steps of 2 starting from an odd number)

#What did you see on line 3?
# 5.429084....
#What was the smallest number you could have seen, what was the largest?
# 2.5 is the smallest possible number, 5.4999999..... is the largest

# Write code to produce a random number between 1 and 100 inclusive.
random_number_between_1_and_100 = random.randint(1, 100)
print(f"Random integer between 1 and 100: {random_number_between_1_and_100}")