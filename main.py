#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
print("Welcome to the Number Guessing Game!")
def diff(difficulty):
    if difficulty.lower()=="easy":
        return 10
    elif difficulty.lower()=="hard":
        return 5
    else:
        return -1
        
def play():
    print("I'm thinking of a number between 1 and 100.")
    number=random.randint(1,100)
    print(f"Pssst, the correct answer is {number}")
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
    chances=diff(difficulty)
    while(chances<0):
        difficulty=input("Incorrect value. Please type 'easy' or 'hard': ")
        chances=diff(difficulty)
    guessed=False
    while(chances>0 and not guessed):
        print(f"You have {chances} attempts remaining to guess the number.")
        guessed_number=int(input("Make a guess: "))
        if(guessed_number==number):
            guessed=True
            print(f"You got it! The answer was {number}.")
        elif guessed_number <number:
            print("Too low.")
            chances-=1
        elif guessed_number >number:
            print("Too high.")
            chances-=1
        if not guessed and chances!=0:
            print("Guess again")
    if(not guessed):
        print("You've run out of guesses, you lose.")
    
    return input("Do you want to play again?Y/N\n")
    

while(play().lower()=="y"):
    play()