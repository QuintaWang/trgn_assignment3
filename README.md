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
# histogram.py
## Usage
 We use argument to define the column and we open file to plot histogram with data from a column
## Description
### add argumment-f which is used for define the column if its not defined the default value is 2
### open population_analysis.tsv file
### plot histogram with data from a specific column
### Save the histogram as png
### Display the plot
## Known Issue
### population_analysis.tsv is appear to be unrecognized arguments
