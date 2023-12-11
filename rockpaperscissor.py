import random


def get_user_choice():
    user_choice = input("Enter Rock, Paper or Scissor: ")
    return user_choice


def generate_ai_choice():
    return random.choice(['Rock', 'Paper', 'Scissor'])


def determine_winner(user_choice, ai_choice):
    user_score = 0
    print(ai_choice)
    if user_choice == ai_choice:
        print("draw")
    elif ((user_choice == "Rock" and ai_choice == "Scissor")
          or (user_choice == "Paper" and ai_choice == "Rock")
          or (user_choice == "Scissor" and ai_choice == "Paper")):
        print("You won")
        user_score += 1
    else:
        print("ai won")

    print("Your score :", user_score)


def start_game():
    replay = 'Y'
    while replay == 'Y' or replay == 'y':
        user_choice = get_user_choice()
        ai_choice = generate_ai_choice()
        determine_winner(user_choice, ai_choice)
        replay = input("Do you want to replay the game ?: ")


start_game()
