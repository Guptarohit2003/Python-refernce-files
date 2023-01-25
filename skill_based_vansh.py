import random
print("----------------------------------------")
print("\n\t\tWELCOME TO THE NUMBER GUESSING GAME")
while True:
    n= random.randint(1,100)
    print("\nThe number lies from 1 to 100")
    print("\nYou have 7 chances to guess the number")
    print("\nBest of Luck :)\n")
    number_of_guesses=5
    while (number_of_guesses>0):
        guess_number = int(input("Guess the number : "))
        if guess_number+10<n:
            print("\nYour Guess is too low!!!\n")
        elif guess_number<n:
            print("\nYou're so close...\n")
            print("guess a little greater number\n")
        elif guess_number-10>n:
            print("\nYour Guess is too high!!!\n")
        elif guess_number>n:
            print("\nYou're so close...\n")
            print("guess a little smaller number\n")
        else:
            print("\nyou won\n")
            print(5-number_of_guesses,"no.of guesses took to guess the number")
            break
        print("\nNumber of guesses left :",number_of_guesses)
        number_of_guesses -= 1

    if number_of_guesses == 0:
        print("YOU LOST...:(")
        print("The number was ",n)
        print("Better Luck Next Time")
        
    print("Enter 1 if you want to play again : ")
    print("Enter any other key to EXIT")
    ch = int(input("Enter Your Choice : "))
    
    if ch != 1:
        print("Exiting The Game...")
        break