print("Welcome to my Computer Quiz")
is_playing = input("Do you want to play? yes/no:")
count=0

if is_playing.lower() != "yes":
    quit()

print("okay, let's play")

print("Question 1: What is the full form of CPU?")
print("A. Central Peripheral Unit\n"
      "B. Central Processing Unit\n"
      "C. Core Processing Unit\n"
      "D. Computer Processing Unit\n")

answer = input("Enter your choice: ")
if answer=="B":
    print("You are Correct")
    count+=1
else:
    print("You are wrong")

print("Question 2: What is the full form of RAM?")
print("A. Random Access Memory\n"
      "B. Random Memory\n"
      "C. RAM\n"
      "D. Restricted Access Memory\n")

answer = input("Enter your choice: ")
if answer=="A":
    print("You are Correct")
    count+=1
else:
    print("You are wrong")

print("Question 3: What is the full form of GPU?")
print("A. Graphics Processing Unit\n"
      "B. Gaming Processing Unit\n"
      "C. GPU Processing Unit\n"
      "D. Geometric Processing Unit\n")

answer = input("Enter your choice: ")
if answer=="A":
    print("You are Correct")
    count+=1
else:
    print("You are wrong")

print(f"You got {count} correct out of 3 questions")


#This is not a pro-level code, just a beginner code to help me familiarize with python.
