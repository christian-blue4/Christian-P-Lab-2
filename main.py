import random

game_number = random.randint(1,10)
guess_count = 0

while(True):

    user_guess = int(input("Guess a number between 1 and 10: "))
    guess_count += 1

    if user_guess > game_number:
        print("Too High")
    elif user_guess < game_number:
        print ("Too Low")
    else:
        print(f"You win!!! It took you {guess_count} guesses.")
        if guess_count == 1:
            print("Amazing, you got it on your first guess!")
        elif guess_count <= 3:
            print("Great job!")
        else:
            print("You got it! Keep practicing to guess it faster.")
        break