from Practice1 import ineuron


class course_type:
    def current_going_live_courses(self):
        print("Current Courses that going on!")
        l = ["FSDS", "FSDA", "Big Data", "NLP", "JS", "SQL"]
        for i in range(len(l)):
            print(i + 1, l[i])

        print("Select the courses that you want to master!!")
        a = input("Enter your fav. course: ")
        if a in l:
            print("Thank you for taking", a , "course")
            quit()
        else:
            print("We can help you in choosing best course for you\n\n fill your details")
            name = input("Name: ")
            email = input("Email: ")
            phone_number = input("Phone No.")
            details = ineuron(name, email, phone_number)
            details.chat_with_agent()
course = course_type()
course.current_going_live_courses()
