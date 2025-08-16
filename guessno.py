# -------------------------------------------------------
# Number Guessing Game with Fixed Secret Number [JKUAD0910]
# -------------------------------------------------------

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game [JKUAD0910]")
    print("I have chosen a number between 1 and 10. Can you guess it?")

    secret_number = 6   # fixed secret number
    attempts = 0
    guessed = False

    while not guessed:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("📉 Too low! Try a higher number.")
            elif guess > secret_number:
                print("📈 Too high! Try a lower number.")
            else:
                print(f"🎉 Correct! The secret number is 6. You guessed it in {attempts} attempts. [JKUAD0910]")
                guessed = True

        except ValueError:
            print("⚠ Please enter a valid number!")

    print("Thanks for playing! [JKUAD0910]")


if __name__ == "__main__":
    number_guessing_game()
