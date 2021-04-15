# OSU SP21 Ling 3802 Final Project

## Phishing Email Feature Design

Authors: Evan Standerwick and Diya Adengada

Course Information: Linguistics 3802 (Language and Computers) at The Ohio State University, Spring 2021. Section 29082. Taught by Willy Cheung.

## About

This project takes a selection of 500 spam and 500 ham emails from the Enron1 formatted email data set found at <http://nlp.cs.aueb.gr/software_and_datasets/Enron-Spam/index.html> and parses them for certain linguistic features that may be useful to discriminate between phishing and legitimate emails.

These features are as follows:
* Number of misspelled words in the email subject line
    * subj_misspellings:low if < 3 misspellings
    * subj_misspellings:high if >= 3 misspellings
* Proportion of misspelled words in the email body
    * body_misspellings:low if (num misspellings / num words) < 0.2
    * body_misspellings:high if (num misspellings / num words) >= 0.2
* Amount of certain keywords in email subject line
    * subjectLine_keywords:low if < 1 keywords found
    * subjectLine_keywords:high if >= 1 keywords found
* Amount of certain keywords in email body
    * body_keywords:low if < 2 keywords from list found
    * body_keywords:high if >= 2 keywords from list found
* Amount of eye-catching symbols in the email subject line
    * subjectLine_symbols:low if < 1 symbols from list found
    * subjectLine_symbols:high if >= 1 symbols from list found
* Amount of eye-catching symbols in the email body
    * body_symbols:low if < 1 symbols from list found  
    * body_symbols:high if >= 1 symbols from list found

- Add lists for keywords and symbols

The parsed features are output into a .tsv file which can be used by the Stanford Classifier <https://nlp.stanford.edu/software/classifier.shtml> to train and test a classifier.

Spellchecking library source: <https://pypi.org/project/pyspellchecker/>

Developed on Windows 10 in Python 3.8.1

## Instructions
To parse a ham folder: `py dataParser.py ham <Input_Folder_Path> <Output_File_Name>`

To parse a spam folder: `py dataParser.py spam <Input_Folder_Path> <Output_File_Name>`

Run for ham folder first, then again for spam folder, or vice versa. Make sure they both output into the same .tsv file.

Do this for the train data and for the test data, getting two separate .tsv files which the Stanford Classifier can use.

Example: 
`py dataParser.py ham data\train\ham trainFeatures.tsv`

`py dataParser.py spam data\train\spam trainFeatures.tsv`

`py dataParser.py ham data\test\ham testFeatures.tsv`

`py dataParser.py spam data\test\spam testFeatures.tsv`

Note: Selected output file is never overwritten, just appended to.

After obtaining test and train .tsv files, configure and run the Stanford Classifier on them to see results.
