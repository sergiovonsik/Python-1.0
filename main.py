print("How many pencils would you like to use:")
x = input()
# ----1y2-----
error = 0

try:
    x = int(x)
    if x <= 0:
        if x == 0:
            print("The number of pencils should be positive")
            error = 1
        elif x <= -1:
            print("The number of pencils should be numeric")
            error = 1
    elif x > 0:
        error = 0

except ValueError:
    print("The number of pencils should be numeric")
    error = 1

while error == 1:
    x = input()
    try:
        x = int(x)
        if x <= 0:
            print("The number of pencils should be positive")
            error = 1
        elif x > 0:
            error = 0

    except ValueError:
        print("The number of pencils should be numeric")
        error = 1

# ----1y2-----

y = "|"
visual_pencils = x * y
number_of_pencils = x
print("Who will be the first (John, Jack):")
first = str(input())
# -----3------
paso_2 = 0

if first == "John" or first == "Jack":
    paso_2 = 1
else:
    while paso_2 == 0:
        print("Choose between 'John' and 'Jack'")
        first = str(input())
        if first == "John" or first == "Jack":
            paso_2 = 1
# -----3------
print(visual_pencils)
print(first, "'s turn")


if first == "Jack":
    actual_player = "Jack"
elif first == "John":
    actual_player = "John"








while number_of_pencils > 0:
    if actual_player == "John":
        # --------5--------------------
        minus_pencils = input()
        possible_answers = ["1", "2", "3"]
        if minus_pencils in possible_answers:
            pass
        else:
            while minus_pencils not in possible_answers:
                print("Possible values: '1', '2' or '3'")
                minus_pencils = input()
        minus_pencils = int(minus_pencils)
        if minus_pencils <= number_of_pencils:
            pass
        else:
            while minus_pencils > number_of_pencils:
                print("Too many pencils were taken")
                minus_pencils = input()
                possible_answers = ["1", "2", "3"]
                if minus_pencils in possible_answers:
                    pass
                else:
                    while minus_pencils not in possible_answers:
                        print("Possible values: '1', '2' or '3'")
                        minus_pencils = input()
                minus_pencils = int(minus_pencils)

        # --------5-------------------
        number_of_pencils -= minus_pencils
        if number_of_pencils == 0:
            print("Jack won!")
            break
        else:
            pass
        # print(number_of_pencils)
        print(number_of_pencils * y)
        if number_of_pencils > 0:
            print("Jack's turn")
            actual_player = "Jack"
        else:
            pass

# --------6-------------------
    elif actual_player == "Jack":
        a_devolver = 0

        while number_of_pencils >= 5:
            number_of_pencils -= 4
            a_devolver += 4

        if number_of_pencils <= 5:
            if number_of_pencils % 4 == 0:
                minus_pencils = 3
            elif number_of_pencils % 3 == 0:
                minus_pencils = 2
            elif number_of_pencils % 2 == 0:
                minus_pencils = 1
            else:
                minus_pencils = 1
            number_of_pencils += a_devolver

        print(minus_pencils)
# --------6-------------------
        number_of_pencils -= minus_pencils
        if number_of_pencils == 0:
            print("John won!")
            break
        else:
            pass
        # print(number_of_pencils)
        print(number_of_pencils * y)
        if number_of_pencils > 0:
            print("John's turn")
            actual_player = "John"
        else:
            pass


