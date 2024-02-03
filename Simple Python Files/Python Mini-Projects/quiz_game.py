print("Welcome to my quiz!")

play = input("Do you want to play? (yes) to play: ")

if play != "yes":
    quit()

print("Let's play :)")
score = 0
count = 0

answer = input("What is the capital city of France? ")
if answer == "Paris":
    print('Correct!')
    score += 1
    count += 1
else:
    print('Incorrect')

answer = input("Which planet is known as the ""Red Planet""? ")
if answer == "Mars":
    print('Correct!')
    score += 1
    count += 1
else:
    print('Incorrect')

answer = input("Who painted the Mona Lisa? ")
if answer == "Leonardo da Vinci":
    print('Correct!')
    score += 1
    count += 1
else:
    print('Incorrect')

answer = input("What is the chemical symbol for gold? ")
if answer == "Au":
    print('Correct!')
    score += 2
    count += 1
else:
    print('Incorrect')

print("You got " + str(count) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")