# Added this file until github issues are resolved - will delete later

# TODO: Move a lot of this stuff to README, and add more detail.
# Author: Evan Standerwick
# This program takes the included formatted email data set and outputs a tsv to be fed into the Stanford classifier.
# Developed on Windows 10 in Python 3.8.1
# Instructions: run using: py dataParser.py <ham/spam> <Input_Folder_Path> <Output_File_Name>
# Run for ham folder first, then again for spam folder, or vice versa.
# Note: Selected output file isn't overwritten, it's just appended to.
# Spellchecking library used from here: https://pypi.org/project/pyspellchecker/


import os
import sys
import string
from pyspellchecker.spellchecker import SpellChecker


# Declaring constants
SUBJMISSPELLINGSCUTOFF = 3
BODYMISSPELLINGSCUTOFF = 0.20


def main():
    # 1. OPEN UP INPUT DATA FOLDER AND OUTPUT TSV FILE
    outputFile = open(sys.argv[3], "a")

    # Opening directory in python code modified from here: https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = sys.argv[2] + "\\"
    directory = os.path.join(script_dir, rel_path)
    
    i = 1
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
        print(f"Completed parsing file {i}")
        i += 1

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
    subj_missellings = getSubjectLineMisspelledWords(subjectLine)
    body_misspellings = getBodyMisspelledWords(body)
    return (hamOrSpam, subj_missellings, body_misspellings)


# Gets a binary feature for the number of misspelled words in the subject line
# Param subjectLine: the message subject line
# Returns: subj_misspellings:low if > SUBJMISSPELLINGSCUTOFF misspellings, or subj_misspellings:high if >= SUBJMISSPELLINGSCUTOFF misspellings
def getSubjectLineMisspelledWords(subjectLine: str):
    filtered = subjectLine.translate(str.maketrans('', '', string.punctuation))

    words = filtered.split(" ")
    numWords = len(words)

    spellchecker = SpellChecker()
    misspelled = spellchecker.unknown(words)
    numMisspelled = len(misspelled)
    #print(misspelled)

    proportion = numMisspelled / numWords
    feature = "subj_misspellings:low"
    #if proportion >= 0.35:
    if (numMisspelled >= SUBJMISSPELLINGSCUTOFF):
        feature = "subj_missellings:high"

    return feature


# Gets a binary feature for the number of misspelled words in the subject line
# Param subjectLine: the message subject line
# Returns: subj_misspellings:low if > SUBJMISSPELLINGSCUTOFF misspellings, or subj_misspellings:high if >= SUBJMISSPELLINGSCUTOFF misspellings
def getBodyMisspelledWords(body: str):
    filtered = body.translate(str.maketrans('', '', string.punctuation))

    words = filtered.split(" ")
    numWords = len(words)

    spellchecker = SpellChecker()
    misspelled = spellchecker.unknown(words)
    numMisspelled = len(misspelled)

    proportion = numMisspelled / numWords
    feature = "body_misspellings:low"
    if proportion >= BODYMISSPELLINGSCUTOFF:
        feature = "body_missellings:high"

    return feature


# Prints an entry tuple into our TSV file
# Param entry: our analyzed data point output by getLabelAndFeatures
# Param outputFile: our output .tsv file
def printToTsv(entry: tuple, outputFile):
    i = 0
    while (i < len(entry) - 1): # iterate over all but the last feature
        outputFile.write(entry[i] + "\t")
        i += 1
    outputFile.write(entry[i] + "\n") # after last feature, we want a new line, not a tab


#Detects whether certain keywords are found in the subject line
def findKeywordsSL(subjectLine)
  {
    slKeys = ['action', 'response', 'urgent'] #add more
    slWords = subjectLine.split()
    cutoff = 0 #update

    #loop through list and count number of spamWords
    count = 0
    for x in slWords:
      for y in slKeys:
        if x == y
          count++ 
    
    #Compare with cutoff
    if count >= cutoff:
      keyWordFeatureSL = "subjectLine_keywords:high"
    else:
      keyWordFeatureSL = "subjectLine_keywords:low"


    #return
    return keyWordFeatureSL;
  }

#Detects whether certain keywords are found in the body
#Returns binary feature
#Need to update with cutoff for amount of words found
def findKeywordsBody(body)
  {
    #define list of keywords
    bodyKeys = ['urgent', 'action', 'account', 'ssn', ] #add more
    stringWords = body.split()
    cutoff = 0 #UPDATE

    #loop through list and count number of spamWords
    count = 0
    for x in stringWords:
      for y in bodyKeys:
        if x == y
          count++ 
    
    #Compare with cutoff
    if count >= cutoff:
      keyWordFeature = "body_keywords:high"
    else:
      keyWordFeature = "body_keywords:low"


    #return
    return keyWordFeature;
  }

#TO DO 
#Detects whether certain keywords are found in the closing (salutation)
def findKeywordsClosing()
{
  #Here we're checking for common closings
    closeKeys = ['greetings', '' ]
    stringWords = body.split()
    cutoff = 0 #UPDATE

    #loop through list and count number of spamWords
    count = 0
    for x in stringWords:
      for y in bodyKeys:
        if x == y
          count++ 
    
    #Compare with cutoff
    if count >= cutoff:
      keyWordFeature = "body_keywords:high"
    else:
      keyWordFeature = "body_keywords:low"


    #return
    return keyWordFeature;
}

#Checks for excessive use of symbols, such as multiple exclamation points, etc and returns a binary feature
def checkSymbolsSL(subjectLine )
{
  #Here we're checking for common closings
   #Here we're checking for common closings
  symbolKeys = ['@', '!', '$']
  stringWords = subjectLine.split()
  cutoff = 0 #UPDATE

    #loop through list and count number of spamWords
    count = 0
    for x in stringWords:
      for y in symbolKeys:
        if x == y
          count++ 
    
    #Compare with cutoff
    if count >= cutoff:
      symbolFeature = "subjectLine_symbols:high"
    else:
      symbolFeature = "subjectLine_symbols:low"


    #return
    return symbolFeature;

}

#Checks for excessive use of symbols, such as multiple exclamation points, etc and returns a binary feature
def checkSymbolsBody(body)
{
  #Here we're checking for common closings
   #Here we're checking for common closings
  symbolKeys = ['@', '!', '$']
  stringWords = body.split()
  cutoff = 0 #UPDATE

    #loop through list and count number of spamWords
    count = 0
    for x in stringWords:
      for y in symbolKeys:
        if x == y
          count++ 
    
    #Compare with cutoff
    if count >= cutoff:
      symbolFeature = "body_symbols:high"
    else:
      symbolFeature = "body_symbols:low"


    #return
    return symbolFeature;

}


#Detect prevalence of symbols in the SL

if __name__ == '__main__':
    main()
