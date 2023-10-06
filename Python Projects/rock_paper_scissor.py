import random

#define list for rock paper scissor
lst = ["Rock", "Paper", "Scissor"]


while True:

    comp_choice = random.randint(1,3)

    result = "draw"
    
    print("1 -> Rock\n2 -> Paper\n3 -> Scissor")
    choice=int(input("Enter your choice :"))

    while choice > 3 or choice <1:
      choice=int(input('Enter a valid choice please ☺'))

    if choice == 1:
        choice_name= 'Rock'
    elif choice == 2:
        choice_name= 'Paper'
    else:
        choice_name= 'Scissor'

    if (choice==1 and comp_choice==2):
            print('paper wins')
            result='Paper'
    elif (choice==2 and comp_choice==1):
            print('paper wins')
            result='paper'


    if (choice==1 and comp_choice==3):
            print('Rock wins\n')
            result='Rock'
    elif (choice==3 and comp_choice==1):
            print('Rock wins\n')
            result='rock'

    if (choice==2 and comp_choice==3):
            print('Scissors wins')
            result='scissor'
    elif (choice==3 and comp_choice==2):
            print('Scissors wins')
            result='Scissor'

    if result == "draw":
        print("\n***** Tie *****")
    elif result == choice_name:
        print("\n***** User wins *****")
    else:
        print("\n***** Computer wins *****")

    print("Do you want to play again? (Y/N)")

    ans = input().lower
    if ans =='n':
        break
