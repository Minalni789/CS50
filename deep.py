''' In deep.py, implement a program that prompts the user for the answer to the Great Question of Life,
the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two 
or forty two. Otherwise output No. '''

def main():
    question = input("What is the answer to the great question of life, the Universe, and everything? ")
    answer = question.casefold().strip()
    if answer == "42":
        print("Yes")
    elif answer == "forty-two" or answer == "forty two":
        print("Yes")
    elif answer == "Forty Two":
        print("Yes")
    else:
        print("No")

main()
