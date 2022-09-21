# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("It's not a number")
    return number


def checkNumber(num):
    if 6 <= num <= 7:
        print("Yes")
    elif 0 < num < 6:
        print("No")
    else:
        print("There are seven days in every week! Try again :)")


num = InputNumbers("Enter the number: ")
checkNumber(num)