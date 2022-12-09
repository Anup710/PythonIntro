def cuber(x):
    return pow(x, 3)


print(cuber(5))


def max_num(num1, num2, num3):
    temp = num1
    if num2 >= num1:
        temp = num2

    if num3 >= temp:
        temp = num3

    print("greatest number is: " + str(temp))


max_num(-1, -3, -2)


def string_equality(city):
    if city.lower() == "brussels":
        print("Damn we like the same city!")
    else:
        print("Such a bummer")


string_equality("Brussels")
string_equality("Vienna")
