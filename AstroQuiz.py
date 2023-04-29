print("Welcome to AstroQuiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay then! lets takeoff.")
score = 0

answer = input("I am the closest planet to the sun. Who am I? ").lower()
if answer == "mercury":
    print("Correct!")
    score += 1 
else:
    print("Incorrect :( the correct answer is Mercury" )

answer = input("My nickname is the red planet. What is my real name? ").lower()
if answer == "mars":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is Mars" )

answer = input("I have a thick atmosphere that is hot enough to melt lead, what am I called? ").lower()
if answer == "venus":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is Venus" )

answer = input("I am the largest planet in our solar system. Who am I? ").lower()
if answer == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is jupiter" )

answer = input("I am smaller than Earth and my surface is covered with craters. Who am I? ").lower()
if answer == "mercury":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is Mercury" )

answer = input("I am sometimes called the morning star or evening star. Who am I? ").lower()
if answer == "venus":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is Venus" )

answer = input("I am home to the only known intelligent life in the universe, do you know me? ").lower()
if answer == "earth":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is Earth but now im starting to have my doubts..." )

answer = input("I am a potential destination for future human colonization. What do they call me? ").lower()
if answer == "mars":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is Mars" )

answer = input("I have four major moons named Io, Europa, Ganymede, and Callisto. Who am I? ").lower()
if answer == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is Jupiter" )

answer = input("My beautiful rings are one of my most famous features. Whats my name? ").lower()
if answer == "saturn":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is Saturn" )

answer = input("I have a surface that's about 71 percent covered by water. What is my name? ").lower()
if answer == "earth":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is Earth" )

answer = input("My density is less than water, so I could float in it. Guess who? ").lower()
if answer == "saturn":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is Saturn" )

answer = input("I rotate sideways and I am classified as an ice giant. What planet am i? ").lower()
if answer == "uranus":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is Uranus" )

answer = input("I am the furthest planet from the Sun and appear blue. Whats my name? ").lower()
if answer == "neptune":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is Neptune" )

answer = input("I was once considered the ninth planet, but now I am classified as a dwarf planet. What do they call me? ").lower()
if answer == "pluto":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is Pluto" )

answer = input("I am a space laboratory orbiting Earth, where astronauts from different countries conduct research. Whats my name? ").lower()
if answer == "international space station" or answer == "iss" or answer =="the international spacestation":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is International space station or ISS" )

answer = input("I have a blue-green color due to the presence of methane in my atmosphere. Who am I? ").lower()
if answer == "uranus":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is Uranus" )

answer = input("I have the largest volcano in the solar system, named Olympus Mons. Guess who am I? ").lower()
if answer == "mars":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is Mars" )

answer = input("I am now the smallest planet in the solar system after pluto got kicked out of the club. Who am I? ").lower()
if answer == "mercury":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is Mercury" )

answer = input("Astronauts landed on me in the summer of 1969. Whats my name? ").lower()
if answer == "moon" or answer == "the moon":
    print("Correct!")
    score += 1
else:
    print("Incorrect :( the correct answer is the Moon" )

print("Congrats cadet! You got " + str(score) + " out of 20 questions correct." )
print("Your final score is " + str((score / 4) * 100) + "%." )
