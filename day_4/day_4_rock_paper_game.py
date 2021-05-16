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
RPC = [rock,paper,scissors]
try:
  user_case = int(input("What do you want to choose type 0 for rock, 1 for paper and 2 for scissors: \n"))
  print(RPC[user_case])

  computer_case = random.randint(0,2)
  print(f"The computer chose :\n{RPC[computer_case]}")

  if user_case == 0:
    if computer_case == 0:
      print("Its a draw")
    elif computer_case == 1:
      print("You loose")
    elif computer_case == 2:
      print("You win")

  elif user_case == 1:
    if computer_case == 0:
      print("You win")
    elif computer_case == 1:
      print("Its a draw")
    elif computer_case == 2:
      print("You loose")

  elif user_case == 2:
    if computer_case == 0:
      print("You loose")
    elif computer_case == 1:
      print("You win")
    elif computer_case == 2:
      print("Its a draw")
except:
  print("Enter a valid character")
