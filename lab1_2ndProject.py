import random

Keep_playing = "yes"

while (Keep_playing == "yes") :

    computer_wins = 0
    user_wins = 0
    tie = 0
    print("Press enter to roll dice ")
    input()
    user_roll = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    computer_roll = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    print(user_roll)
    print(computer_roll)

    if ( computer_roll < user_roll) :
        print( "Congrats, you win!")
        user_wins = user_wins+1 
    elif ( computer_roll > user_roll): 
        print ("oops, you lose") 
        computer_wins = computer_wins+1
    else: 
        print("its a tie!") 
        tie = tie+1 

    Keep_playing  = input("Do you want to roll again?") 

if (Keep_playing == "no"):
    print("Computer wins ", computer_wins)
    print("User wins ", user_wins )
    print("ties ", tie)
    
    





