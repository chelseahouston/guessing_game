import random
myName = input("Hello! What is your name? ")
number = random.randint(1, 10)
print("Well, " + myName + " I am thinking of a number between 1 and 10.")
def main():
  guess = int(input("Take a guess: ") )
  if guess == number:
    print("Good job, " + myName + "! You guessed my number")
  else:
    print("Sorry, " + myName + " that's not the number I'm thinking of. Try again!")
    main()
main()