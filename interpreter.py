'''In a file called interpreter.py, implement a program that prompts the user
for an arithmetic expression and then calculates and outputs the result as a 
floating-point value formatted to one decimal place. Assume that the user’s 
input will be formatted as x y z, with one space between x and y and one space between y and z ''' 


def main():
    take_input = input("Expression: ")
    x, y, z = take_input.split(" ")
    xfloat = float(x)
    zfloat = float(z)

    if y == "+":
        print(xfloat + zfloat)
    elif y == "-":
        print(xfloat - zfloat)
    elif y == "*":
        print(xfloat * zfloat)
    elif y == "/":
        print(xfloat / zfloat)






main()

