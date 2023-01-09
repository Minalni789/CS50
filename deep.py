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