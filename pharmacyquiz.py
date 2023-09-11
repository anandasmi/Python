import os

# Clearing the Screen
os.system("cls")

# CREATING QUIZ IN PYTHON

# GREETINGS
print("Hey There?")
name = input("Your Name?")

print(
    "Hello "
    + name
    + ", I want to welcome you to this little quiz that we're going to play!"
)

print("Are you Ready?")
answer = input(" ")
if answer == "Yes":
    print("We shall move on then!")
else:
    print("Someone's scared.....")

# 1st Q
print("------------------------------\n")

print("Moving onto the 1st question!\n" + "Tell me who invented the C language?")
print(
    "Your Options are :\n"
    "A. Mahadeva Lal Schroff \n"
    "B. William Procter Jr.\n"
    "C. David walters\n"
    "D. Abu al-Qasim al-Zahrawi\n"
)
answer1 = input(" ")
if answer1 == "B":
    print("Your answer is correct!!")
else:
    print("I'm afraid your answer is wrong")

# 2nd Q
print("---------------------------------\n")

print("Your next question is...\n" + "Which year did pharmacy exactly begin?")
print(
    "The options are :\n" "A. 1523 A.D\n" "B. 1345 A.D\n" "C. 100 B.C\n" "D. 1526 B.C\n"
)

answer2 = input(" ")
if answer1 == "D":
    print("Your answer is correct!!")
else:
    print("I'm afraid your answer is wrong")

print("----------------------------------\n")
# 3rd Q
print(
    "Your next questions is....\n"
    + "The field of pharmacy that concerns with the lawful pratices and \njudiciary approval of different pharmacy products is ?"
)
print(
    "The options are : \n"
    "A. Phamacy administration\n"
    "B. Drug regulatory affairs\n"
    "C. Both\n"
    "D. Pharmacy practice\n"
)

answer3 = input(" ")
if answer1 == "B":
    print("Your answer is correct!!")
else:
    print("I'm afraid your answer is wrong")
