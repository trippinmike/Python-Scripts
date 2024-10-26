#author: N3m0m3N
#date: 10/20/2024
#description: List Comprehensions (Day 8)

# Make a two-player Rock-Paper-Scissors game.

player_1 = input("Enter your choice (rock, paper, scissors): \n")
player_2 = input("Enter your choice (rock, paper, scissors): \n")

if player_1 == "rock" and player_2 == "paper":
    print("Paper covers rock.  \nPlayer 2 wins!")
elif player_1 == "rock" and player_2 == "scissors":
    print("Rock smashes scissors.  \nPlayer 1 wins!")
elif player_1 == "rock" and player_2 == "rock":
    print("Draw.  \nGo again.")
elif player_1 == "paper" and player_2 == "rock":
    print("Paper covers rock.  \nPlayer 1 wins!")
elif player_1 == "paper" and player_2 == "scissors":
    print("Scissors cut paper.  \nPlayer 2 wins!")
elif player_1 == "paper" and player_2 == "paper":
    print("Draw.  \nGo again.")
elif player_1 == "scissors" and player_2 == "paper":
    print("Scissors cut paper.  \nPlayer 1 wins!")
elif player_1 == "scissors" and player_2 == "rock":
    print("Rock smashes scissors.  \nPlayer 2 wins!")
elif player_1 == "scissors" and player_2 == "rock":
    print("Draw.  \nGo again.")
elif player_1 or player_2 != "paper" or player_1 or player_2 != "rock" or player_1 or player_2 != "scissors":
    print("Invalid input.  Run again.")




