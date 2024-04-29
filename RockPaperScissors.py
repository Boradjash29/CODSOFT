import random


def get_user_choice():
    while True:
     user_choice =input("Enter the our choice [Rock , Paper , Scissors] : ")
     
     if user_choice in ['Rock' , 'Paper' , 'Scissors' ]:
         return user_choice
     else:
         print("Invalid choice. Please Enterr the valid choice !!")
       
def get_computer_choice():
    return random.choice(['Rock' , 'Paper' , 'Scissors' ])     


def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        print("Its a Tie!!")
    elif ((user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == 'Scissors' and computer_choice == 'Paper') or (user_choice == 'Paper' and computer_choice == 'Rock')):
         return "You Win !!"
    else:
        return "Computer Win!!"    

while True:

 
    print("---------------Let's play Rock ,Paper, Scissors !!!---------------")
    
    user_choice =get_user_choice()
    computer_choice =get_computer_choice()
    
    print("You Chose :",user_choice)
    print("Computer Chose:",computer_choice)
    print(determine_winner(user_choice,computer_choice))
    
    play_again =input("Do you want play again ? (y/no):").lower()
    if play_again !='y':
        break