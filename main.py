import random
import emoji
myName = input("Hello! What is your name? ")
number = random.randint(1, 10)
print("Well, " + myName + " I am thinking of a number between 1 and 10. You have 6 attempts to guess it!")
def main():
  count=5
  while count > -1:
    guess = input("Take a guess: ")
    try:
      guess = int(guess)
    except ValueError:
      print("Error: Incorrect Value. Please enter a number.")
      main()
    if guess == number:
      print("Good job, " + myName + "! You guessed my number")
      break
    elif guess > number:
      print(f"Sorry, {myName}, that's not the number I'm thinking of. Your guess is too high!")
      print(f"You have {count} attempt(s) left.")
      count -=1
    elif guess < number:
      print(f"Sorry, {myName}, that's not the number I'm thinking of. Your guess is too low!")
      print(f"You have {count} attempt(s) left.")
      count -=1
  print(f"The correct number was {number}. " + emoji.emojize(":winking_face_with_tongue:"))
main()
