def convert(variable):

    printed = print(variable.replace(":)", "🙂").replace(":(", "🙁"))

    return printed



def main():
    call_input = input("Write :) or :( fo emojies in your text: ")
    converted = convert(call_input)
    print(converted)

main()
