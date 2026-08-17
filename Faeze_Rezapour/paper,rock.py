import random

print("you can choice ROCK,PAPER,SCISSORS ")
#creat the list
game_select = ["ROCK", "PAPER", "SCISSORS"]
#creat the dic
mapping = {"R": "ROCK", "r": "ROCK", "rock": "ROCK",
           "P": "PAPER", "p": "PAPER", "paper": "PAPER",
           "S": 'SCISSORS', "s": 'SCISSORS', "scissors": "SCISSORS"}

while True:
    rounds_elm = input("enter your round game: ")
    if rounds_elm.isdigit():
        rounds_elm = int(rounds_elm)
        break
    else:
        print("please enter a valid number")

current_rounds = 1
while current_rounds <= rounds_elm:
    print(f"\n-- round of {current_rounds} from {rounds_elm}")

    player_select = input("enter your choice from ROCK,PAPER,SCISSORS: ").lower().strip()


    if player_select not in mapping:
        print("please enter a valid choice")
        continue

    player = mapping[player_select]
    computer = random.choice(game_select)
    print(f"computer choice is {computer}")
    print(f"player choice is {player}")

    if computer == player:
        print("score is equal")
    elif (player == "ROCK" and computer == "SCISSORS") or \
            (player == "PAPER" and computer == "SCISSORS") or \
            (player == "PAPER" and computer == "ROCK"):
        print("you win")
    else:
        print("you lose")

    current_rounds += 1

count = input("can you continue playing again? or q to quit:").lower().strip()
if count == "n":
        pass


