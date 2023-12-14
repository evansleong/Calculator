import random


def get_user_choice():
    user_choice = input("Enter R(ROCK), P(PAPER) or S(SCISSOR): ").lower()
    while user_choice != "r" and user_choice != "p" and user_choice != "s":
        user_choice = input("PLEASE RE-ENTER: ").lower()
    return user_choice


def generate_ai_choice():
    return random.choice(['r', 'p', 's'])


def determine_winner(user_choice, ai_choice):
    if ai_choice == 'r':
        print("AI CHOSE ROCK")
    elif ai_choice == 'p':
        print("AI CHOSE PAPER")
    elif ai_choice == 's':
        print("AI CHOSE SCISSOR")
    if user_choice == ai_choice:
        print("DRAW")
    elif ((user_choice == "r" and ai_choice == "s")
          or (user_choice == "p" and ai_choice == "r")
          or (user_choice == "s" and ai_choice == "p")):
        print("YOU WON")
        return True
    else:
        print("AI WON")


def start_game():
    user_score = 0
    replay = 'Y'
    while replay == 'Y' or replay == 'y':
        user_choice = get_user_choice()
        ai_choice = generate_ai_choice()
        if determine_winner(user_choice, ai_choice):
            user_score += 1
        print("Your score :", user_score)
        replay = input("Do you want to replay the game ?: ")


start_game()
