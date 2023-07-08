print("Welcome To my Game")
name = input("Please Enter Your Name: ")
age = int(input("Enter your age: "))
if age == 8 :
    print("Let's Start")
elif age == 9 :
    print("Let's Start")
elif age == 10 :
    print("Let's Start")
else:
    print("This Game not For Your Age")
    quit()

#start the game

answer = input ("In which direction does the sunrise? ") .lower()
if answer == "east" :
    print("Good Job",name)
    print("Next Question")
    score=+1
else:
    print("Is not the right answer")
    print("The Right answer is : East")

answer = input ("How many zeros are there in one hundred thousand? ") .lower()
if answer == "five" or 5 :
    print("Good Job",name)
    print("Next Question")
else:
    print("Is not the right answer")
    print("The Right answer is : Five")

answer = input ("How many months of the year have 31 days? ") .lower()
if answer == "january, march, may, july, august, october and december"  :
    print("Good Job",name)
    print("Next Question")
else:
    print("Is not the right answer")
    print("The Right answer is : january, march, may, july, august, october and december")

answer = input ("How many weeks are there in one year? ") .lower()
if answer == 52 or "52":
    print("Good Job",name)
    print("Next Question")
else:
    print("Is not the right answer")
    print(52)

answer = input ("Which are the colors in a rainbow? ") .lower()
if answer == "violet, indigo, blue, green, yellow, orange, red":
    print("Good Job",name)
    print("Next Question")
else:
    print("Is not the right answer")
    print("violet, indigo, blue, green, yellow, orange, red")