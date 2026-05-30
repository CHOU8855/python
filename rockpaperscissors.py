import random

while True:
    user_action = input('enter a choice (rock paper or scissors):')
    possible_actions = ['rock','paper','scissors']

    computer_action = random.choice(possible_actions)
    print(f'\nyou chose {user_action} computer chose {computer_action}.\n')


    if user_action == computer_action:
        print(f'both players selected {user_action}. its a tie')
    elif user_action == 'rock':
        if computer_action == 'scissors':
            print('Rock smashes scissors! You win!')
        else:
            print('paper covers rock! You lose.')
    
    elif user_action == 'paper':
        if computer_action == 'scissors':
            print('paper gets snipped by scissors! You lose!')
        else:
            print('paper covers rock! You win.')
    
    elif user_action == 'scissors':
        if computer_action == 'rock':
            print('rock crushes scissors! You lose!')
        else:
            print('scissor snipped paper! You win.')

    play_again = input('play again? (y/n): ')
    if play_again != 'y':
        break
    
    
    
    