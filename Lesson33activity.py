import random #importing module
playing = True #initialise
number = str(random.randit(10,20)) #random in-built function


print("I will generate a number form 0 to 9, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")
#iterate loop till the condition is true
while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("You win the game")
        print("the number was" , number)
        break
    
    else:
        print("Your guess is not right, try again and again if you want. \n")