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

