import random
def guess(x):
 random_number=random.randint(1,x)
 guess=0
 while guess!= random_number:
   guess=int(input(f"Guess a number betweeen 1 and {x}\n"))
   if guess < random_number:
     print("Sorry,you'll have to guess again.Too low!\n")
   elif guess > random_number:
     print("Sorry,you'll have to guess again.Too high!\n")

 print(f"Yay,congratulations!You just entered the correct {random_number}")
guess(10)

#In Python, the import statement is used to bring external modules or libraries into
#a Python script or program, allowing you to use the functionality provided by those modules.
#Modules are files containing Python code that define functions, variables, and classes, among other things.
#Basically, the randint() method in Python returns a random integer value between the two lower and higher 
#limits (including both limits) provided as two parameters. 
#Python’s randint function is a powerful tool in your coding arsenal. 
#It’s like a digital dice, capable of generating random numbers for a variety of applications.
#It should be noted that this method is only capable of generating integer-type random value
#The import random line at the beginning is necessary because randint is part of the random module in Python.
# The function random.randint(1, 10) then generates a random integer within the range of 1 and 10.