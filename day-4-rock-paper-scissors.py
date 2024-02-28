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

#Write your code below this line 👇
choices = [rock, paper, scissors]

player_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
computer_pick = random.randint(0,2)

print(f"Player: {choices[player_pick]}\nComputer: {choices[computer_pick]}")

if player_pick == computer_pick:
    print("Draw")
else:
    win_conditions = [(0,2), (1,0), (2,1)]
    if (player_pick, computer_pick) in win_conditions:
        print("You win")
    else:
        print("You lose")
