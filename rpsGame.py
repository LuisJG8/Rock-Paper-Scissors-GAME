import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps_list = [rock, paper, scissors]

random_choice = random.choice(rps_list)
user_choice = input("Rock, paper, scissors: ").lower()

if user_choice == 'rock':
    user_choice = rps_list[0]
elif user_choice == 'paper':
    user_choice = rps_list[1]
elif user_choice == 'scissors':
    user_choice = rps_list[2]
else:
    print('Wrong input')

print(user_choice)
print(f'Computer:\n {random_choice}')

if user_choice == rock and random_choice == scissors:
    print('You won')
elif user_choice == rock and random_choice == paper:
    print('You lost')
elif user_choice == paper and random_choice == scissors:
    print('You lost')
elif user_choice == paper and random_choice == rock:
    print('You won')
elif user_choice == scissors and random_choice == paper:
    print('You won')
elif user_choice == scissors and random_choice == rock:
    print('You lost')
else:
    print('Draw')