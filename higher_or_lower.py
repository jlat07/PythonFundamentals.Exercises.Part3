from random import randrange

def higher_or_lower():
  
  random_num = randrange(10)

  user_guess = int(input("Pick a number from 1-10: "))
  print("Random number was " + str(random_num))

  if random_num > user_guess:
    print("Your guess was " + str(user_guess))
    print("Too low")

  elif random_num < user_guess:
    print("Your guess was " + str(user_guess))
    print("Too high")

  elif random_num == user_guess:
    print("Correct! Your guess was " + str(user_guess) + " you guessed correct!")

"""
Random number is generated. User inputs a number and it is compared to random
number by if, else statements that will print according to randomnum vs guess
"""    

higher_or_lower()