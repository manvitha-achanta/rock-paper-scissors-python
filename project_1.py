                    # ROCK PAPER SCISSORS GAME
import random
computer_list=[0,1,2]
computer_choice=random.choice(computer_list)
user_number=int(input("enter your number;0 for rock , 1 for paper , 2 for scissor :"))
print(f"computer choice is :{computer_choice}")
if user_number in [0,1,2]:
    if user_number==computer_choice:
        print("tie")
    elif user_number==0 and computer_choice==2:
        print("you win")
    elif user_number==2 and computer_choice==0:
        print("you lose")
    elif computer_choice>user_number:
        print("you lose")
    elif computer_choice<user_number:
        print("you win")
else:
    print("you lose")



