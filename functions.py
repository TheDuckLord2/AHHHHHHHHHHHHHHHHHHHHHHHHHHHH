import math

## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    if isinstance(filename, str) and ".txt" in filename:
        infile = open(filename, "r")

        print("File opened.")
    else:
        print("The file does not exist.")

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    try:
        return num1 / num2
    except:
        return "You cannot divide a number by zero/the numbers must be of the same datatype."


## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    if not all(isinstance(p, (int, float)) for p in [x1, y1, x2, y2]):
        raise TypeError("Input parameters must be numeric")
    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = math.sqrt(dist)

    return dist

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    if not temp:
        return False
    if not isinstance(temp, str):
        return False
    test = temp[::-1]

    if(test == temp):
        return True

    else:
        return False

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    try:   
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))

        div = num1 / num2

        print("Your numbers divided is:", div)
    except:
        print("Cannot divide by zero or non number.")

## returns the squareroot of a particular number
def sq(num):
    try:
        if num == True:
            num = 1
        elif num == False:
            num = 0
        return math.sqrt(num)
    except:
        return "non number or negative values used."

## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    if not all(isinstance(arg, str) for arg in (first, middle, last)):
        raise TypeError("All arguments must be strings")
    
    if not all(arg for arg in (first, middle, last)):
        raise ValueError("All arguments must be non-empty")
        
    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    if len(numbers) == 0:
        raise ValueError("The input list cannot be empty")
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("The input list should only contain numbers")
    try:
        return "Your item at " + str(index) + " index is " + str(numbers[index])
    except IndexError:
        raise IndexError("Index out of range")
