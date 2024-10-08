import random

def get_user_choice():
    choices = ['1', '2', '3']
    user_choice = input("Välj 1, 2 eller 3: ").lower()
    while user_choice not in choices:
        print("Ogiltigt val. Försök igen.")
        user_choice = input("Välj 1, 2 eller 3: ").lower()
    return user_choice

def get_computer_choice():
    choices = ['1', '2', '3']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"Du valde {user_choice} och datorn valde {computer_choice}, Datorn vinner!"
    else:
        return f"Du valde {user_choice} och datorn valde {computer_choice}, du vinner!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"Du valde: {user_choice}")
    print(f"Datorn valde: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()


