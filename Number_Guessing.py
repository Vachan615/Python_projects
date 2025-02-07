,--.  ,--.                  ,--.                      ,----.                               ,--.                
|  ,'.|  |,--.,--.,--,--,--.|  |-.  ,---. ,--.--.    '  .-./   ,--.,--. ,---.  ,---.  ,---.`--',--,--,  ,---.  
|  |' '  ||  ||  ||        || .-. '| .-. :|  .--'    |  | .---.|  ||  || .-. :(  .-' (  .-',--.|      \| .-. | 
|  | `   |'  ''  '|  |  |  || `-' |\   --.|  |       '  '--'  |'  ''  '\   --..-'  `).-'  `)  ||  ||  |' '-' ' 
`--'  `--' `----' `--`--`--' `---'  `----'`--'        `------'  `----'  `----'`----' `----'`--'`--''--'.`-  /  
                                                                                                       `---'   
"""
print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty: easy or hard? ").lower()
random_num = random.randint(1, 100)

attempts = 10 if difficulty == "easy" else 5

for i in range(attempts, 0, -1):
    print(f"You have {i} attempts remaining to guess the number.")
    choice = int(input("Make a guess: "))

    if choice < random_num:
        print("Too low.\nGuess again.")
    elif choice > random_num:
        print("Too high.\nGuess again.")
    else:
        print("YOU WON!")
        break
else:
    print(f"Out of attempts! The correct number was {random_num}.")

