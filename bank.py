def main():
    prompt = input("Greeting: ").casefold().strip()
    beginning = prompt.startswith("h")
    if "hello" in prompt:
        print("$0")
    elif beginning == True:
        print("$20")
    else:
        print("$100")

main()