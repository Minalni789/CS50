'''In a file called camel.py, implement a program that prompts the user for the name of a 
variable in camel case and outputs the corresponding name in snake case. Assume that the 
user’s input will indeed be in camel case.
'''

def main():
    camel = (input("camelCase:"))


    for variable in camel:
        if variable.islower():
            print(variable, end="")
        else:
            print("_" + variable.lower(), end="" )



main()
