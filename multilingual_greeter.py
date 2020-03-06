def language():
    
  print("Enter Number for Language:1-English, 2-French, 3-Spanish")
  
  global selection

  selection = int(input("Enter Here: "))

"""
Ask user to select language by number and stores number as selection.
"""

language()


def name_input():

  global name

  if selection == 1:
    name = input("Whats your name?: ")  
  elif selection == 2:
    name = input("Comment vous appelez-vous ? : ")
  elif selection == 3:
    name = input("¿Cómo te llamas?: ")
  else:
    print("1 of 3 languages not entered. Program Terminated")

"""
Ask user in what thier name is in desired language.
"""    

name_input()


def greet():
    
  if selection == 1:
    print("Hello " + str(name))
  elif selection == 2:
    print("Bonjour " + str(name))
  elif selection == 3:
    print("Hola " + str(name))

"""
Greets user by name in desired language.
"""

greet()