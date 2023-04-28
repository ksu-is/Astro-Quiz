print("Welcome to AstroQuiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay then! lets takeoff.")

answer = input("Which planet is closest to the sun? ").lower()
if answer == "mercury":
    print("Correct!")
else:
    print("Incorrect :(" )
