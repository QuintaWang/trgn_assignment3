import re

with open('example1.txt', 'r') as file:
    data = file.read().rstrip()

numbers = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', data) #extract numbers from textfile 
print(numbers)
for number in numbers:#apply transformation to each number we extracted 
    number = number.replace("-", "")#remove all the instance of -
    if number[0] == '+':#if it is a international number apply the following transformation 
        number = number[0:3] + '(' + number[3:5] + ')' + number[5:]
    else:#if we have local number 
        number = '(' + number[0:3] + ')' + number[4:]#add parantheses at the beginning for the country code
    print(number)#print result line by line