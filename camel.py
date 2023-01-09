def main():
    camel = (input("camelCase:"))


    for variable in camel:
        if variable.islower():
            print(variable, end="")
        else:
            print("_" + variable.lower(), end="" )



main()