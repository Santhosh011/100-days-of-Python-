print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
print("Welcome to the treasure island, your goal is to find the treasure")
left_or_right = input("Which way you wanna go 'left' or 'right'")
if left_or_right =="left":
  swim_case = input("you see a lake in front of you will you 'swim' or 'wait' for a boat")
  if swim_case == 'swim':
    print("You are eaten by hungry sharks. GAME OVER!")
  elif swim_case == 'wait':
    print("you successfully cross the lake and see a suspicious lady waiting")
    lady_case = input("will you cautiously approach the lady or will u try to flirt with her : 'caution' or 'flirt' ")
    if lady_case == "caution":
      print("you approach her and as she tries to kill you, you doge and kill her. nice one!")
      door_case = input("You see a house , you enter it and see 2 doors 'red' and 'green' which one will you open")
      if door_case == 'red':
        print("as soon as you open the door a spike kills you. GAME OVER")
      if door_case == 'green':
        print("You find a treasure chest full of gold congrajutation you have done it. ")
    elif lady_case == "flirt":
      print("turns out she was a witch and she knocks you out and chops you to make potions")
elif left_or_right =="right":
  dragon_case = input("you see a 3 head dragon coming to attack you what will you do 'fight' or 'run'")
  if dragon_case == "fight":
    print("You never stood a chance the dragon burns you alive. GAME OVER!")
  elif dragon_case == "run":
    print("The dragon cought up to you in no time and burns you. GAME OVER! :(")

  
