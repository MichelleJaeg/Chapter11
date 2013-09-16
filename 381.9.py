# Problem 9

# An alternative approach to gpasort

from gpa import makeStudent

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print ("{0}\t{1}\t{2}".
        format(s.getName(), s.getHours(), s.getQPoints()),
            file = outfile)
    outfile.close()

def main ():
    # Introduction
    print ("This program sorts student grade information by GPA\n")

    # Get filename from user
    filename = input ("Enter the name of the data file: \n")

    # Create list of data
    data = readStudents(filename)

    # Let user choose to sort by GPA, name, or credit hours
    sortType = input("Would you like the data sorted by GPA, name, or credits?\n")

    if sortType == "GPA":
        # Create list sorted by GPA using the tuple (gpa, and a student object)
        gpaList = []
        for i in range(len(data)):
            gpa = data[i].gpa()
            student = data[i]
            grade_point = (gpa,student)
            gpaList.append(grade_point)
        gpaList.sort()
        # Create a new list of student objects (based on previous list that is already sorted by GPA)
        newList = []
        for item in gpaList:
            (gpa,student) = item
            newList.append(student)

    elif sortType == "name":
        # Create list sorted by name using the tuple (name(a string), and a student object)
        nameList = []
        for i in range(len(data)):
            name = data[i].getName()
            student = data[i]
            student_name = (name,student)
            nameList.append(student_name)
        nameList.sort()
        # Create a new list of student objects (based on previous list that is already sorted by name)
        newList = []
        for item in nameList:
            (name, student) = item
            newList.append(student)

    else:
        # Create a list sorted by credit hours using the tuple (credits(an int), and a student object)
        creditsList = []
        for i in range(len(data)):
            credits = data[i].getHours()
            student = data[i]
            student_credits = (credits,student)
            creditsList.append(student_credits)
        creditsList.sort()
        # Create a new list of student objects (based on previous list that is already sorted by credit hours)
        newList = []
        for item in creditsList:
            (credits,student) = item
            newList.append(student)

    # Write data to output file
    filename = input("Enter a name for the output file: \n")
    writeStudents(newList, filename)
    print ("The data has been written to", filename)

if __name__== '__main__':
    main ()
