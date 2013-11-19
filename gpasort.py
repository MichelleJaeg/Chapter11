# Problem 2
# "Extend the gpasort program so that it allows the user to sort a file of students based on GPA,
# name or credits. Your program should prompt for the input file, the field to sort on, and the output
# file."

#Problem 3
# "Extend your solution to the previous problem by adding an option to sort the list in either
#  ascending or descending order. "

# gpasort.py
# A program to sort student information into GPA order

from gpa import Student, makeStudent

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
    print ("This program sorts student grade information by GPA\n")
    filename = input ("Enter the name of the data file: \n")
    data = readStudents (filename)
    direction = input("Would you like the data sorted in ascending or descending order?\n")
    if direction == "descending":
        reverse = True
    else:
        reverse = False
    sortType = input("Would you like the data sorted by GPA, name, or credits?\n")
    if sortType == "GPA":
        data.sort(key = Student.gpa, reverse=reverse)
    elif sortType == "name":
        data.sort(key = Student.getName, reverse=reverse)
    else:
        data.sort(key = Student.getHours, reverse = reverse)
    filename = input("Enter a name for the output file: \n")
    writeStudents(data, filename)
    print ("The data has been written to", filename)

if __name__ == '__main__':
    main ()
