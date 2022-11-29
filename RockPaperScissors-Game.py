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
strike = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors: "))

pc_strike = [rock, paper, scissors]
random_pc = random.randint(0,2)

if strike == random_pc:
  print(pc_strike[strike])
  print("Computer chose:\n")
  print(pc_strike[random_pc])
  print("\nIs a draw.")
elif strike == 0 and random_pc == 1:
  print(pc_strike[strike])
  print("Computer chose:\n")
  print(pc_strike[random_pc])
  print("\nYou lose.")
elif strike == 1 and random_pc == 2:
  print(pc_strike[strike])
  print("Computer chose:\n")
  print(pc_strike[random_pc])
  print("\nYou lose.")
elif strike == 2 and pc_strike == 0:
  print(pc_strike[strike])
  print("Computer chose:\n")
  print(pc_strike[random_pc])
  print("\nYou lose.")
elif strike >= 3:
    print("You typed an incorrect number. The options are only : 0 - 1 - 2, BYE.")
else:
  print(pc_strike[strike])
  print("Computer chose:\n")
  print(pc_strike[random_pc])
  print("\nYou win!!")
