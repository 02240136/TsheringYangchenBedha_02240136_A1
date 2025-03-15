def game_menu():
    print("Welcome to the Game! ")
    print("Two Games ")
    print("1. Guess the number")
    print("2. Rock Paper Scissors")
    print("3. Exit the Game")
    choice = int(input("Enter your choice: "))
    return choice

choice = game_menu()

""" Guess the number game. """
def guess_number_game():
    
    import random
    number = random.randint(1, 100)      # Select a random number between 1 and 100
    max_attempts = 3                      # Maximum attempts allowed(set to 3)
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if guess < number:
             print("Too low! Try again.", max_attempts - attempts, "attempts left.")
            elif guess > number:
               print("Too high! Try again.", max_attempts - attempts, "attempts left.")
            else:
                print("Congratulations! You got it right in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 100.")

    if attempts == max_attempts and guess != number:                                # !=  Checks if the guess is not equal to the number
        print(f"Oh no! You lost. The number was {number}. End of the game.")        # f lets you put a variable in a string

def Rock_Paper_Scissors():
     """ Simple Rock Paper Scissors game."""
     import random
     choices = ["rock", "paper", "scissors"]
     your_choice = input("Enter Rock, Paper, or Scissors: ").lower() 
     computer_choice = random.choice(choices)
    
     print(f"Computer chose:, {computer_choice}")
    
     if your_choice == computer_choice:
        print("It's a tie!")
     elif(your_choice == "rock" and computer_choice == "scissors") or \
         (your_choice == "paper" and computer_choice == "rock") or \
         (your_choice == "scissors" and computer_choice == "paper"):
         print("You win!")
     else:
         print("You lose!")

def Exit_program():
    print("Goodbye! Thank you. ")
    return

while True:
    if choice == 1:
        guess_number_game()
    elif choice == 2:
        Rock_Paper_Scissors()
    elif choice == 3:
        print("Goodbye! Thank you.")
        break
    else:
        print("Invalid choice. Try again.")

    x = input("would you like to explore another option? (y/n): ")
    if x.lower() == "y":                                              #lower() converts the string to lowercase
        choice = game_menu()
    else:
        Exit_program()
        break


