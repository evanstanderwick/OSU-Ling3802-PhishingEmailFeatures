# Author: Evan Standerwick
# This program takes an input data set (TODO figure out data set file format) and outputs a tsv to be fed into the Stanford classifier.
# Developed on Windows 10 using Python 3.8.1
# Instructions: run using ./python dataParser.py <Input_Folder_Name> <Output_File_Name>.tsv
# Input folder must have ham subdirectory named "ham" and spam subdirectory named "spam"


import os
import sys


def main():
    # 1. OPEN UP INPUT DATA FILE
    # Opening directory in python code modified from here: https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = sys.argv[1] + "\\"
    directory = os.path.join(script_dir, rel_path)

    for filename in os.listdir(directory):
        currentFile = open(rel_path + filename, "r")
        # 2. BEGIN PARSING
        subjectLine = getSubjectLine(currentFile)
        body = getBody(currentFile)
        currentFile.close()

        # 3. GET LABEL AND BINARY FEATURES FOR CURRENT ENTRY

        # 4. PRINT CURRENT ENTRY DATA TO OUTPUT .TSV FILE

    # 5. REPEAT STEPS 1-4 UNTIL END OF FOLDER

    # 6. CLOSE IO STREAMS AND EXIT


# Returns the subject line of an input email file as a string
# Param inputFile: the input email file
# Returns: subject line as a string
def getSubjectLine(inputFile):
    # In our corpus, the first line is always the subject, and it always begins with "Subject: " and ends with a \n
    line = inputFile.readline()
    line = line[9:len(line) - 1] # parse out "Subject: " and the final \n character
    inputFile.seek(0) # reset file pointer
    return line


# Returns the message body of an input email file as a string
# Param inputFile: the input email file
# Returns: message body as a string
def getBody(inputFile):
    lines = inputFile.readlines()
    separator = " "
    body = separator.join(lines[1:]) # parse out subject line
    inputFile.seek(0) # reset file pointer
    return body


# Returns a tuple of (label, binary_feature_1, binary_feature_2, binary_feature_3, ...)
# Param isSpam: true if inputFile is spam, false if ham
# Param subjectLine: the message subject line
# Param body: the message body
# Returns: (label, binary_feature_1, binary_feature_2, ...)
def getLabelAndFeatures(isSpam: bool, subjectLine: str, body: str):
    print("getLabelAndFeatures")


# Gets a value for (TODO decide on what feature1 will be)
# Param subjectLine: the message subject line
# Param body: the message body
# Returns: binary_feature_1
def getFeature1(subjectLine: str, body: str):
    print("getFeature1")


# Prints an entry tuple into our TSV file
# Param entry: our analyzed data point output by getLabelAndFeatures
# Param outputFile: our output .tsv file
def printToTsv(entry: tuple, outputFile):
    print("printToTsv")


if __name__ == '__main__':
    main()