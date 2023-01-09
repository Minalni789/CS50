'''In a file called playback.py, implement a program in Python that prompts the user for 
input and then outputs that same input, replacing each space with ... (i.e., three periods).'''

def main():
    indoor_voice = input("What's your input? ")
    print(indoor_voice.replace(" ", "..."))

main()
