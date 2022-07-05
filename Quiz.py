count=0
print("Quiz Competition")
Play=input ("Do you want to play this game? ")
if Play.lower()== "yes":
    print("Let's start playing the game")
    q1=input("What us the full form of CPU? ")
    if q1.lower() =="central processing unit":
        print("correct answer")
        count+=1
    else:
        print("wrong Answer")
    q2= input("What is the full form of UPS? ")
    if q2.lower()=="uninterruptible power supply":
        print("Correct Answer")
        count += 1
    else:
        print("Wrong Answer")
    q3 = input("What is the full form of WHO? ")
    if q3.lower()=="world health organisation":
        print("Correct Answer")
        count += 1
    else:
        print("Wrong Answer")
    q4 = input("What is the full form of WTO? ")
    if q4.lower()=="world trade organisation":
        print("Correct Answer")
        count += 1
    else:
        print("Wrong Answer")
else:
    quit()
wrong=4-count
percent_marks=str((count/4)*100)+"%"
print("Correct Answer:",count)
print("Wrong Answer:",wrong)
print("You got :", percent_marks)