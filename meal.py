def main():
    t = input("What time is it? ")
    con = convert(t)
    if 7 <= con <= 8:
        print("breakfast time")
    elif 12 <= con <= 13 :
        print("lunch time")
    elif 18 <= con <= 19:
        print("dinner time")

def convert(time):

    hours, minutes = time.split(":")
    inte = int(hours)
    return inte


if __name__ == "__main__":
    main()