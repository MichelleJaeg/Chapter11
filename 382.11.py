import string

# Problem 11

# Write an automated censor program that reads in the text from a file and creates a new file where all of the four-letter
# words have been replaced by "****". You can ignore punctuation, and you may assume that no words in the file are split
# across multiple lines.

def main ():

    # Get input file
    file=input("Please enter the name of the original file. ")
    infile=open(file, 'r')

    # get output file
    otherFile=input("Please enter the name of the file to write to. ")
    outfile=open(otherFile, 'w')

    # Change file
    for line in infile:
        words=line.split( )
        for word in words:
            counter=0
            for letter in word:
                if not letter in string.punctuation:
                    counter+=1
            if counter==4:
                if "." in word:
                    word="****."
                elif "," in word:
                    word="****,"
                elif "?" in word:
                    word="****?"
                elif "!" in word:
                    word="****!"
                else:
                    word="****"


            print (word + " ", file=outfile, end="")

    # close files
    infile.close()
    outfile.close()













if __name__=='__main__':
    main ()
