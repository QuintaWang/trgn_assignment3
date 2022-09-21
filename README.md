# trgn_assignment3
# extract_phonenum.py
## Usage
### We use file to open the text file and we use rstrip() to strip the text file in to a list of string
### We then use replace and string manipulation to reformat the phone number
## Description
### import a regular expression
### open a text file and save it to a list of string and saperated by space
### extract numbers from textfile
### apply transformation to each number we extracted 
### remove all the instance of -
### if it is a international number apply the following transformation 
### if we have local number 
### add parantheses at the beginning for the country code
### print result line by line
## Known Issue
### the code will not work for international numbers if the country code is not 2 digits or the area code is not 2 digits
### the code will not work for local numbers if the country code is not 3 digits