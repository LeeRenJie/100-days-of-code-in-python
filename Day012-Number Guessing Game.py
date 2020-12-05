from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  # print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()


#/////////////////////MY SOLUTION//////////////////////////
# random_number = randint(1,100)

# game_over = False
# while not game_over:
#   print(logo)
#   print("Welcome to the number guessing game!")
#   print("I'm thinking of a number between 1 and 100. Can you guess?")
#   # print(f"psst the correct answer is {random_number}")

#   if (input('Choose a difficuly! Type "Easy" or "Hard".\n').lower()) == "easy":
#     life = 10
#   else:
#     life = 5

#   while life > 0 and game_over == False:
#     print(f"You have {life} attempts to remaining to guess the number.")
#     guess = int(input("Your guess: "))

#     if guess > random_number:
#       if life == 1:
#         print("Too high!\nYou've run out of guesses, you lose..")
#       else:
#         print("Too high!\nGuess Again!")
#       life -= 1
#     elif guess < random_number:
#       if life == 1:
#         print("Too low!\nYou've run out of guesses, you lose..")
#       else:
#         print("Too low!\nGuess Again!")
#       life -= 1
#     else:
#       print(f'You got it! The number is {random_number}')
#       game_over = True

#   game_over = True




