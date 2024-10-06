 #Session 2
#1 List- Basics
#1.1 Listing courses
courses = ['Introduction to Programing', 'Calculus I', 'Data Structure and Algorithms', 'Linear Algorithms', 'Linear Algebra', 'Physics I', 'Chemistry I', 'Biology I', 'Microeconomics','Macroeconomics','Physcology I', 'History I','English Composition I', 'Introduction to Philosophy', 'Calculus II', 'Discrete Mathmatics']
#1.2 Printing the list
print("Course list: ", courses)

# List- sorted()
#2.1 and #2.2 Printing list in alphabetically order
print("Alphabetical order: ", sorted(courses))
#2.3 and #2.4 Printing the list in reverse alphabetical order
print("Reverse alphabetical order: ", sorted(courses, reverse= True))

# List - reverse()
#3.1 and #3.2 Printing list in its original state step.1
courses.reverse()
print("Reversed list: ", courses)

# step.2
courses.reverse()
print("Reversed list: ", courses)

#3.3 and #3.4 Using reverse() to reverse the order again
courses.reverse()
print("Reversed list: ", courses)

#Lists - sort()
#4.1 and #4.2 Using sort() to reverse the list again
courses.sort()
print("Sorted courses: ", courses)

#4.3 and #4.4 Using sort() to reverse the list again
courses.sort(reverse= True)
print("Sorted list(reversed): ",courses)

#Lists - Create useable coding
units = ['Introduction to Programing', 'Calculus I', 'Data Structure and Algorithms', 'Linear Algorithms', 'Linear Algebra', 'Physics I', 'Chemistry I', 'Biology I', 'Microeconomics','Macroeconomics','Physcology I', 'History I','English Composition I', 'Introduction to Philosophy', 'Calculus II', 'Discrete Mathmatics']
#1 Sorting the list in alphabetical order with sort()
units.sort()
print("Units avaliable: ",units)
#1.1 and #1.2
print("The following courses are available for expression of interest if the students meet the prerequisites: ",units)

#2 Replacing a unit with a new course announcement 
print("ANNOUNCEMENT: One of the courses is no longer available and has been withdrawn and replaced by a new course. ")
#2.1 and #2.2 Replacing one of the untis and showing both the original course and the new course, with a message to confirm the withdrawn course and new course
print ("Unrevised units: ", units)
units[9] = "Advanced Programming"
print("Revised units: ", units)
print('The course "Introduction to programming" has been offically replaced with "Advanced Programming"') 

#3 Introduction of Three new courses in the semester
#3.2 Using insert() to add a new unit
units.insert (0, "Artificial Intelligence")
print("Courses after inserting at index 0: ", units)
#3.3 Using insert() to add a new course to the middle of my list
units.insert (9, "Machine Learning")
print("Courses after inserting at index 7: ", units)
#3.4 Using append() to add a new course to the end of my list
units.append ("Cloud computing")
print("Courses after appending at the end of the list: ", units)
#3.5 Printing the messages showing the available courses
print("All avaliable courses are as follows: ", units)

#4 Withdrawal of Four courses in the semester 
#4.2 Creating a message to inform the students that the following courses  are unavailable
unavaliable_courses = ['History I','English Composition I', 'Introduction to Philosophy',  'Calculus II']
print ("The following courses have been withdrawn from the semester: ",unavaliable_courses)

#4.3 Using pop() to remove four courses from my list one at a time
first_pop= units.pop(8)
print("Withdrawn unit 1: ",first_pop)

second_pop = units.pop(7)
print("Withdrawn unit 2: ",second_pop)

third_pop= units.pop(8)
print("Withdrawn unit 3: ",third_pop)

fourth_pop = units.pop(3)
print("Withdrawn unit 4: ", fourth_pop)

#4.4. Printing the messages showing the available courses and those no longer available
print("Courses avaliable this semster: ", units)
print("Courses terminated from the semseter: ", unavaliable_courses)


#Woeksheet 2
#Tuples and Loops

#1 and #1.1 Listing tuples containing course_id and course_name
courses = [(1,'Introduction to Programming'), (2,'Calculus I'), (3,'Data Structures and Algorithms'), (4,'Linear Algebra'), (5,'Physic I'), (6,'Chemistry I'), (7,'Biology I'),(8,'Microeconomics'), (9,'Macroeconoics'), (10,'Psychology I'), (11,'History I'), (12,'English composition I'), (13,'Introduction to Philosophy I'), (14,'Calculus II'), (15,'Discrete Mathamatics')]

#1.2 Creating an empty list to store both course IDs and Names
course_info= []

#2 Looping through each list
for course in courses:
#2.1 Extracting the course Name and ID from the tuple
    course_id, course_name = course
#2.2 Adding the course name to the empty list
    course_info.append(course)
#3 Printing the course information from the new list
    for course in course_info:
        print((f'Course ID: {course[0]}, Course Name: {course,[1]}'))
        # {course[0]} prints the first element and  {course,[1]} prints the second element 

#A.Conditional Statement
#Using if, elif and else to find a course 

departments = ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology", "Economics", "Psychology", "History", "English", "Philosophy"]

#Department Classifications:
stem_departments = ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology"]
social_sciences_departments = ["Economics", "Psychology", "History"]
humanities_departments = ["English", "Philosophy"]

#Units in classified departments:
stem_units = ["Introduction to Programming", "Calculus I", "Data Structures and Algorithms", "Linear Algebra", "Physics I", "Chemistry I", "Biology I", "Calculus II", "Discrete Mathematics"]
social_sciences_units = ["Microeconomics", "Macroeconomics", "Psychology I", "History I"]
humanities_units = ["English Composition I", "Introduction to Philosophy"]

#Executions
print("Departments in this University: ", departments)

while True:
    user_input= input("Sellect a department to find the course; (S)stem, (SS)social science or (H)humanities: ")

    if user_input.upper() == "S":
        print("Stem cources offered: ", stem_units)   
        break
    elif user_input.upper() == "SS":
        print("Social Science cources offered: ", social_sciences_units)    
        break
    elif user_input.upper() == "H":
        print("Humanities: ", humanities_units)    
        break
    else:
        print("Value Error! Enter a valid Department")

#B.Loops
#Using while True to find course details using course id

#course with Course ID
courses = [(1, "Introduction to Programming", "Computer Science"), (2, "Calculus I", "Mathematics"), (3, "Data Structures and Algorithms", "Computer Science"), (4, "Linear Algebra", "Mathematics"), (5, "Physics I", "Physics"), (6, "Chemistry I", "Chemistry"), (7, "Biology I", "Biology"), (8, "Microeconomics", "Economics"), (9, "Macroeconomics", "Economics"), (10, "Psychology I", "Psychology"), (11, "History I", "History"), (12, "English Composition I", "English"), (13, "Introduction to Philosophy", "Philosophy"), (14, "Calculus II", "Mathematics"), (15, "Discrete Mathematics", "Computer Science")]

while True:
    user_input = input("Enter course ID to find the course (or type 'quit' or '0' to exit): ")

    if user_input.lower() == 'quit' or user_input == '0':
        print("Exiting the program.")
        break

    try:
        course_id = int(user_input)
        # Check if course_id is in the valid range
        if course_id < 1 or course_id > 15:
            print("Course ID is out of range (1-15), try again.")
            continue

        found = False
#C.Conditional statements   
        for course in courses:
            if course[0] == course_id:
                print(f"Course Name: {course[1]}, Department: {course[2]}")
                found = True
                print("*To find the course details quit the program* or reenter the Course ID to find the course")
            break
        
        if not found:
            print("Course ID not found. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a valid course ID or 'quit'/'0' to exit.")


#2. Creating a Course Information Retrieval System
courses =  [(1, "Introduction to Programming", "Computer Science", "None"), (2, "Calculus I", "Mathematics", "None"), (3, "Data Structures and Algorithms", "Computer Science", "Introduction to Programming"), (4, "Linear Algebra", "Mathematics", "None"), (5, "Physics I", "Physics", "None"), (6, "Chemistry I", "Chemistry", "None"), (7, "Biology I", "Biology", "None"), (8, "Microeconomics", "Economics", "None"), (9, "Macroeconomics", "Economics", "Microeconomics"), (10, "Psychology I", "Psychology", "None"), (11, "History I", "History", "None"), (12, "English Composition I", "English", "None"), (13, "Introduction to Philosophy", "Philosophy", "None"), (14, "Calculus II", "Mathematics", "Calculus I"), (15, "Discrete Mathematics", "Computer Science", "Introduction to Programming")]

while True:

    user_input = input("Enter a Course ID to get the details of the course or ('quit' or '0' to exit): ")
    
    if user_input.lower() == 'quit' or user_input == '0':
        print("Exiting the program.")
        break

    course_id= int(user_input)
    found = False
  
    for course in courses:
        if course[0]== course_id:
            print(f'Course Name: {course[1]}, Department: {course[2]}, Prerequisites: {course[3]}')
            found = True
  
    if not found:
        print("Course id not found. Please enter a valid course id")

#A.Instructions
#Using multi-dimensional list to store course information
courses = [
    [1, "Introduction to Programming", "Computer Science", "None"],
    [2, "Calculus I", "Mathematics", "None"],
    [3, "Data Structures and Algorithms", "Computer Science", "Introduction to Programming"],
    [4, "Linear Algebra", "Mathematics", "None"],
    [5, "Physics I", "Physics", "None"],
    [6, "Chemistry I", "Chemistry", "None"],
    [7, "Biology I", "Biology", "None"],
    [8, "Microeconomics", "Economics", "None"],
    [9, "Macroeconomics", "Economics", "Microeconomics"],
    [10, "Psychology I", "Psychology", "None"],
    [11, "History I", "History", "None"],
    [12, "English Composition I", "English", "None"],
    [13, "Introduction to Philosophy", "Philosophy", "None"],
    [14, "Calculus II", "Mathematics", "Calculus I"],
    [15, "Discrete Mathematics", "Computer Science", "Introduction to Programming"]
]

while True:
    user_input = input("Enter Course ID to get the details of the course or Enter 'quit' or '0' to exit the program: ")
    
    if user_input.lower() == 'quit' or user_input == '0':
        print("Exiting the program")
        break
    try:
        course_id = int(user_input)
        if course_id < 1 or course_id > 15:
            print("Course ID is out of range (1-15), try again.")
            continue 
        found = False

        for course in courses:
            if course[0]== course_id:
                print(f'Course Name: {course[1]}, Department: {course[2]}, Prerequisites: {course[3]}')
                found = True
                break

        if not found:
            print("Course not found. Please try again")
    except ValueError:
        print("Invalid value, Please enter a valid value")

#3. Additional Considerations
#Finale of the Interactive Application

courses = {1: ["Introduction to Programming", "Computer Science", "None"],
    2: ["Calculus I", "Mathematics", "None"],
    3: ["Data Structures and Algorithms", "Computer Science", "Introduction to Programming"],
    4: ["Linear Algebra", "Mathematics", "None"],
    5: ["Physics I", "Physics", "None"],
    6: ["Chemistry I", "Chemistry", "None"],
    7: ["Biology I", "Biology", "None"],
    8: ["Microeconomics", "Economics", "None"],
    9: ["Macroeconomics", "Economics", "Microeconomics"],
    10: ["Psychology I", "Psychology", "None"],
    11: ["History I", "History", "None"],
    12: ["English Composition I", "English", "None"],
    13: ["Introduction to Philosophy", "Philosophy", "None"],
    14: ["Calculus II", "Mathematics", "Calculus I"],
    15: ["Discrete Mathematics", "Computer Science", "Introduction to Programming"]}

while True:
    print("Welcome to the Stanley College Course Finder!")
    user_input= input("Enter a Course ID to get the details or ('quit' or '0' to exit): ")
    
    if user_input.lower()=='quit' or user_input=='0':
        print("Exiting the program. Thank you for the enquiry!")
        break
    try:
        course_id= int(user_input)
        found = False
        if course_id in courses:
            course_info = courses[course_id]
            print(f'Course Name: {course_info[0]}, Department: {course_info[1]}, Prerequisites: {course_info[2]}')
        else:
            print("Error: Course ID not found. Please enter a valid course ID.")
    except ValueError:
        print("Invalid input. Please enter a valid integer(i.e, number)for the Course ID")
