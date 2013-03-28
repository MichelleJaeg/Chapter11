import string

# Problem 12

# Extend the program from the previous exercise to accept a file of censored words as another input. The words in the
# original file that appear in the censored words file are replaced by an appropriate number of "*"s.

def main ():

    # Get input files
    file=input("Please enter the name of the original file. ")
    censoredFile=input("Please enter the name of the file containing the censored words. ")

    # get output file
    otherFile=input("Please enter the name of the file to write to. ")
    outfile=open(otherFile, 'w')

    # open files
    infile=open(file,'r')
    infile2=open(censoredFile,'r')
    # Create lists of words from files
    for line in infile:
        words=line.split()
    for line in infile2:
        words2=line.split()

    for word in words:
        # strip punctuation
        wordNoPunc=word.strip(string.punctuation)
        # Change censored words to *
        if wordNoPunc in words2:
            newword=""
            for letter in word:
                if not letter in string.punctuation:
                    newword+="*"
                if letter in string.punctuation:
                    newword+=letter
                word=newword

        # print text to outfile
        print (word + " ", file=outfile, end="")

    # close files
    infile.close()
    outfile.close()













if __name__=='__main__':
    main ()
