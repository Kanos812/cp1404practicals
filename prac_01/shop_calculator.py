#Gets the total number of items the person is buying.
items = int(input("How many items are you purchasing?"))
totalcost = 0
#Loop based on previous input, that occurs inputted no of times
for i in range(items):
    #Gets the new items cost and adds it to the total before displaying said total
    itemcost = float(input("Provide Item Cost $: "))
    totalcost = totalcost + itemcost
    print(f"the new total is {totalcost:.2f}$")
#Checks if total is above $100 and applied discount as neccessary
if totalcost >= 100:
    totalcost = totalcost * 0.9
    print("10% Discount has been applied")
#Provides final cost
print(f"The cost of all your items is {totalcost:.2f}$")