""" Creating random integer """
import random

random_integer = random.randint(1, 10)
print(random_integer)
d20 = random.randint(1, 20)
print(d20)
import random

''' Creating random floating point number '''
import random

random_float = random.random()
print(random_float)
d20 = round(random_float*20)
print(d20)
random_float = random.uniform(1, 10)
print(random_float)

''' Coin toss (Can be an intriguing exercise) '''
import random

coin = random.randint(0, 1)
if coin == 0:
    print('head')
else:
    print('tail')

''' Importing variable from another file '''
from pi import num_pi
print(num_pi)


''' Python list '''
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america)
print(states_of_america[0])
print(states_of_america[-1])
print(len(states_of_america))

states_of_america.append('Turuland')
print(states_of_america)
print(states_of_america[-1])

states_of_america.extend(['Panland', 'Eruland', 'Bimoland'])
print(states_of_america)

# Exercise: Who'll pay the bill
import random

friends = ['Turu', 'Pan', 'Eru', 'Bimo', 'Alek', 'Wari', 'Adi']
# rand_num = random.randint(0, len(friends)-1)
# print(friends[rand_num])

print(random.choice(friends))

# Nested List
fruit = ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
veggie = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']
dirty_dozens = [fruit, veggie]
print(dirty_dozens)
print(dirty_dozens[0][0])  # Strawberries
print(dirty_dozens[1][0])  # Spinach

""" Final Project: Rock Paper Scissor """
import random

HAND_SIGNS = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

# TODO 1: Defining user input and showing the hand sign
user_hand = int(input("Please select [1] Rock / [2] Paper / [3] Scissor:\t"))-1
if user_hand == 0:
    hand_code = 'ROCK'
elif user_hand == 1:
    hand_code = 'PAPER'
elif user_hand == 2:
    hand_code = 'SCISSOR'
else:
    print("Please enter correct answer [1/2/3]")
print(f"You choose: {hand_code}\n{HAND_SIGNS[user_hand]}")

print("\t\tvs")

# TODO 2: Defining opponent input (using random) and showing the hand sign
opponent_hand = random.randint(0, 2)
if opponent_hand == 0:
    hand_code = 'ROCK'
elif opponent_hand == 1:
    hand_code = 'PAPER'
else:
    hand_code = 'SCISSOR'
print(f"\nYour opponent choose: {hand_code}\n{HAND_SIGNS[opponent_hand]}")

# TODO 3: Finding the winner
# Exception for the main logic:
if user_hand == 0 and opponent_hand == 2:
    print("Player WINS!!!")
elif user_hand == 2 and opponent_hand == 0:
    print("Opponent WINS!!!")
# Main logic: rock [0] <- paper [1] <- scissor [2]
elif user_hand > opponent_hand:
    print("Player WINS!!!")
elif user_hand < opponent_hand:
    print("Opponent WINS!!!")
# Main logic: if the hand sign the same, they're draw
elif user_hand == opponent_hand:
    print("DRAW!!!")
