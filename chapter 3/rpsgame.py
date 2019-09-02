from __future__ import print_function
import random

def play():
    winner=''
    choices=['Rock','Paper','Scissor']
    computer_choice=random.choice(choices)
    user_choice=''
    while (user_choice!='Rock' and user_choice!='Paper' and user_choice!='Scissor'):
        user_choice=input(user +' ,what is your choice, Rock, Paper, or Scissor?')
        if computer_choice == user_choice:
            winner= 'Tie'
        elif computer_choice == 'Paper' and user_choice == 'Rock':
            winner='Computer'
        elif computer_choice == 'Rock' and user_choice=='Scissor':
            winner='Computer'
        elif computer_choice == 'Scissor' and user_choice == 'Paper':
            winner='Computer'
        else:
            winner= (user)
        if winner=='Tie':
            print('We both chose',computer_choice+'.')
        else:
            print(winner,' won. The computer Chose', computer_choice+'.')

user=input("what is your name? ")
play_or_not = input(user+': Would you like to play Rock, Paper, Scissors?:y/n ')
if play_or_not == 'y':
    play()
while True:
    play_more =input('Do you want to play again? y/n?. ')
    if play_more == 'Y' or play_more == 'y':
        play()
    else:
        print('maybe we can play later', user)
        break
