# sneak water gun game
'''
1 sneak
0 water
-1gun
'''

import random
computer=random.choice([0, 1, -1])

you_string=input("Enter your choice :")
choices_dict={
    's':1,
    'w':0,
    'g':-1
}
reverse_dict={
   1:"sneak",
   0:"water",
   -1:"gun"
}
you=choices_dict[you_string]

print(f"You chose {reverse_dict[you]} \nComputer chose {reverse_dict[computer]}")

if(computer==you):
    print("It's a draw")
else:
   if(computer-you==-2 or computer-you==1):
      print("you lose")
   else:
      print("you won")
   

# else:
#     if(you==1 and computer==0):
#        print("You Win")
#     elif(you==1 and computer==-1):
#        print("You lost")
#     elif(you==0 and computer==-1):
#       print("You Won")
#     elif(you==0 and computer==1):
#      print("You Lost")
#     elif(you==-1 and computer==1):
#      print("You Won")
#     elif(you==-1 and computer==0):
#       print("You Lost")

'''
computer - you is 1 or -2 when you are losing 
'''