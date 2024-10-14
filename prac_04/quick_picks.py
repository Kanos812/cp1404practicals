import random

numbers_per_line = 6
minimum = 1
maximum = 45

def main():
    """Generates lottery quick picks."""
    number_of_quick_picks = int(input("How many quick picks? "))

    for _ in range(number_of_quick_picks):
        quick_pick = []
        while len(quick_pick) < numbers_per_line:
            number = random.randint(minimum, maximum)
            if number not in quick_pick:
                quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))

if __name__ == "__main__":
    main()