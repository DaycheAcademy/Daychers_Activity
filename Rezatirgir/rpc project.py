
# Rock Paper Scissors

import random

choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
wins = {1: 3, 2: 1, 3: 2}

user_score = 0
computer_score = 0

for i in range(5):

    while True:
        user = input("\n1. Rock\n2. Paper\n3. Scissors\nChoose: ")

        if user.isdigit():
            user = int(user)

            if user in [1, 2, 3]:
                break

        print("Invalid choice! Try again.")

    computer = random.randint(1, 3)

    print("You:", choices[user])
    print("Computer:", choices[computer])

    if user == computer:
        print("Draw")

    elif wins[user] == computer:
        print("You Win")
        user_score += 1

    else:
        print("Computer Wins")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}")

print("\n===== Final Result =====")
print("Your Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("You Win The Game!")

elif computer_score > user_score:
    print("Computer Wins The Game!")

else:
    print("Draw")
