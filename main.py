# GUESSING GAME --
def main():
  # IMPORT --
  import random
  import emoji
  # END IMPORT --

  # RANDOM NUMBER BETWEEN 1-10 --
  number = random.randint(1, 10)

  # USER INPUT NAME --
  myName = input("Hello! What is your name? ")
  print(f"Well, {myName}, I am thinking of a number between 1 and 10. You have 6 attempts to guess it!")

  # GUESS COUNTDOWN NUMBER --
  count=5
  while count > -1:
    guess = input("Take a guess: ")

    # CONVERT INPUT TO INTEGER - IF NOT NUMBER RESTART --
    try:
      guess = int(guess)
    except ValueError:
      print("Error: Incorrect Value. Please enter a number. Restarting game...")
      main()

    # CORRECT ANSWER --
    if guess == number:
      print("Good job, " + myName + "! You guessed my number!")
      break

    # GUESS TOO HIGH --
    elif guess > number:
      print(f"Sorry, {myName}, that's not the number I'm thinking of. Your guess is too high!")
      print(f"You have {count} attempt(s) left.")
      count = count -1

    # GUESS TOO LOW --
    elif guess < number:
      print(f"Sorry, {myName}, that's not the number I'm thinking of. Your guess is too low!")
      print(f"You have {count} attempt(s) left.")
      count = count -1

  # REVEAL CORRECT NUMBER --
  print(f"The correct number was {number}. " + emoji.emojize(":winking_face_with_tongue:"))
main()
