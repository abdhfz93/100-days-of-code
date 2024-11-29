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
sign=[rock,paper,scissors]
human=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
human=int(human)
print("You choose " + str(human))
print(sign[human])
computer=random.randint(0,2)
print("Computer choose " + str(computer))
print(sign[int(computer)])

if computer==human:
    print("Draw")
elif (computer==0 and  human==1) or (computer == 1 and  human==2) or (computer==2 and  human==0):
    print("You Win")
else:
    print("You Lose")
