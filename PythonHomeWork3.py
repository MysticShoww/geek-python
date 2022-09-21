# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Enter coordinate: {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Error! Please enter an integer!")
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Enter point A coordinates: ")
pointA = inputNumbers(2)
print("Enter the coordinates of point B: ")
pointB = inputNumbers(2)

print(f"Distance between points: {format(calculateLengthSegment(pointA, pointB), '.2f')}")