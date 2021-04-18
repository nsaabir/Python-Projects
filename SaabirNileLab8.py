#Nile Saabir
#6-29-17
#Lab 8
#Hillary Fleenor

#Prompt the user to enter a max number and total number of points recieved
print("Welcome to the quiz score program!")
maxPoints = eval(input("Enter a max number :"))
recievedPoints = eval(input("Enter the number of points recieved :"))
score = 100 * (recievedPoints / maxPoints)

#Compare points recieved to max points/let user enter number of points recieved
while recievedPoints > maxPoints or  recievedPoints < 0:
    recievedPoints = eval(input("Enter the number of points recieved :"))

#Convert each score to a letter grade
if score >= 90:
    print("Your score is: A")
elif score >= 80:
    print("Your score is: B")
elif score >= 70:
    print("Your score is: C")
elif score >= 60:
    print("Your score is: D")
else:
    print("Your score is: F")
