from Art import logo, vs
from GameData import data
import random


def RandomChar():
    return random.choice(data)


def HighOrLow(characterA, characterB):
    print(logo)
    print(f"Compare A: {characterA['name']}, a {characterA['description']}, from {characterA['country']}")
    print(vs)
    print(f"Against B: {characterB['name']}, a {characterB['description']}, from {characterB['country']}")


def main():
    while True:
        characterA = RandomChar()
        characterB = RandomChar()

        HighOrLow(characterA, characterB)

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if user_choice == 'a' and characterA['follower_count'] > characterB['follower_count']:
            print("You guessed correctly! A has more followers.")
        elif user_choice == 'b' and characterB['follower_count'] > characterA['follower_count']:
            print("You guessed correctly! B has more followers.")
        else:
            print("Sorry, you guessed wrong.")

        play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
        if play_again != 'yes':
            break


if __name__ == "__main__":
    main()
