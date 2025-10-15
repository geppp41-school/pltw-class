my_courses = ["English", "Math", "CS"]
my_course_scores = []


# for each of the courses you are taking

for course in my_courses:
    redo = "y"
    while (redo == "y"):
        #  enter a point count
        print() # blank line
        print("Enter your points for " + course)

        points = int(input("Points -> "))
        #  display the corresponding letter grade based on point count
        # if you want to redo the grades
        # CODE SEGMENT TO ADD
        if (points >= 90):
            print("A")
        elif (points >= 80):
            print("B")
        elif (points >= 70):
            print("C")
        elif (points >= 60):
            print("D")
        else:
            print("F")

        redo = input("Do you need to re-do these grades? (y/n)")
        #  start over
        # otherwise
        #  program ends