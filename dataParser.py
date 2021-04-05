# Author: Evan Standerwick
# This program takes an input data set (TODO figure out data set file format) and outputs a tsv to be fed into the Stanford classifier.
# Developed on Windows 10 using Python 3.8.1
# Instructions: run using ./python dataParser.py <Input_Data_File>.(TODO figure out data set file type) <Output_File_Name>.tsv


def main():
    # 1. OPEN UP INPUT DATA FILE
    
    # 2. BEGIN PARSING

    # 3. GET LABEL AND BINARY FEATURES FOR CURRENT ENTRY

    # 4. PRINT CURRENT ENTRY DATA TO OUTPUT .TSV FILE

    # 5. REPEAT STEPS 3-4 UNTIL END OF FILE

    # 6. CLOSE IO STREAMS AND EXIT

    print("main")


# Returns a tuple of (label, binary_feature_1, binary_feature_2, binary_feature_3, ...)
# Param entry: our data point in string format
# Returns: (label, binary_feature_1, binary_feature_2, ...)
def getLabelAndFeatures(entry: str):
    print("getLabelAndFeatures")


# Prints an entry tuple into our TSV file
# Param entry: our analyzed data point output by getLabelAndFeatures
# Param outputFile: our output .tsv file
def printToTsv(entry: tuple, outputFile):
    print("printToTsv")


# Gets the label for a data entry
# Param entry: our data point in string format
# Returns: data entry label
def getLabel(entry: str):
    print("getFeature1")


# Gets a value for (TODO decide on what feature1 will be)
# Param entry: our data point in string format
# Returns: binary_feature_1
def getFeature1(entry: str):
    print("getFeature1")


# Gets a value for (TODO decide on what feature2 will be)
# Param entry: our data point in string format
# Returns: binary_feature_2
def getFeature2(entry: str):
    print("getFeature2")


if __name__ == '__main__':
    main()