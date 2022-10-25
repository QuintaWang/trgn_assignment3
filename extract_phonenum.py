import re
import sys

filename=sys.argv[1]
with open(filename, 'r') as file:
    data = file.read().rstrip()

numbers = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', data) 
for number in numbers:
    number = number.replace("-", "")
    if number[0] == '+':
        number = number[0:3] + '(' + number[3:5] + ')' + number[5:]
    else:
        number = '(' + number[0:3] + ')' + number[4:]
    print(number)
