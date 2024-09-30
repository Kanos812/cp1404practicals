looptype = float(input('Please make your choice here: '));

#Every odd number 1-20 printed
if looptype == 1:
    for i in range(1, 21, 2):
        print(i, end=' ')
#Every 10th number 1-100 printed
elif looptype == 2:
    for i in range(0, 101, 10):
        print(i, end=' ')
#Increasing rows of * until specified number is reached
elif looptype == 3:
    n = int(input('Specify the number of "*" you wish to print'));
    for i in range(0, n + 1, 1):
        print("*" * i, end='\n')
#Countdown 20-1 in increments of 1
elif looptype == 4:
    for i in range (20, 0, -1):
        print(i, end=' ')
#Error Checking
else:
    print("invalid input, please input something else")