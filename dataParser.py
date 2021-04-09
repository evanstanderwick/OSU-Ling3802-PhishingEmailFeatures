# Author: Evan Standerwick
# This program takes an input data set (TODO figure out data set file format) and outputs a tsv to be fed into the Stanford classifier.
# Developed on Windows 10 using Python 3.8.1
# Instructions: run using: py dataParser.py <ham/spam> <Input_Folder_Path> <Output_File_Name>
# Run for ham folder first, then again for spam folder, or vice versa.
# Note: Selected output file isn't overwritten, it's just appended to.


import os
import sys


def main():
    # 1. OPEN UP INPUT DATA FOLDER AND OUTPUT TSV FILE
    outputFile = open(sys.argv[3], "a")

    # Opening directory in python code modified from here: https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = sys.argv[2] + "\\"
    directory = os.path.join(script_dir, rel_path)

    for filename in os.listdir(directory):
        currentFile = open(rel_path + filename, "r")
        # 2. BEGIN PARSING
        subjectLine = getSubjectLine(currentFile)
        body = getBody(currentFile)
        currentFile.close()

        # 3. GET LABEL AND BINARY FEATURES FOR CURRENT ENTRY
        isSpam = False
        hamOrSpam = sys.argv[1]
        if (hamOrSpam == "spam"):
            isSpam = True
        labelAndFeatures = getLabelAndFeatures(isSpam, subjectLine, body)

        # 4. PRINT CURRENT ENTRY DATA TO OUTPUT .TSV FILE
        printToTsv(labelAndFeatures, outputFile)
        # 5. REPEAT STEPS 1-4 UNTIL END OF FOLDER

    # 6. CLOSE IO STREAMS AND EXIT
    outputFile.close()


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


# TODO
# Returns a tuple of (label, binary_feature_1, binary_feature_2, binary_feature_3, ...)
# Param isSpam: true if inputFile is spam, false if ham
# Param subjectLine: the message subject line
# Param body: the message body
# Returns: (label, binary_feature_1, binary_feature_2, ...)
def getLabelAndFeatures(isSpam: bool, subjectLine: str, body: str):
    hamOrSpam = "ham"
    if isSpam:
        hamOrSpam = "spam"
    return (hamOrSpam, "firstFeature:1", "secondFeature:2")


# TODO
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
    i = 0
    while (i < len(entry) - 1): # iterate over all but the last feature
        outputFile.write(entry[i] + "\t")
        i += 1
    outputFile.write(entry[i] + "\n") # after last feature, we want a new line, not a tab


if __name__ == '__main__':
    main()