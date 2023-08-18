import random

while True:
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("Your choice:", player_choice, "🙌")
    print("Computer's choice:", computer_choice, "🤖")

    if player_choice == computer_choice:
        print("It's a tie!", "🔁")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!", "🎉")
    else:
        print("Computer wins!", "😢")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
