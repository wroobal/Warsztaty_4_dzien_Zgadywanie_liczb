import random

# draw a number
drawn_number = random.randint(1, 100)

while True:
    # checking is a number is integer
    try:
        get_number = int(input("Guess the number: "))

        # checking that a number is bigger than drawn number
        if drawn_number < get_number:
            print("To big!")
        # checking that a number is smaller than drawn number
        elif drawn_number > get_number:
            print("To small!")
        # checking is that correct number
        else:
            print("You win !")
            break
    except ValueError:
        print("It's not a number!")
