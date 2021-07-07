import os
import csv
from collections import Counter

adSoyad = []
content = []
report_date = []
Submitted_Date = []
User_Name = []
User_Email = []
meeting_ID = []
# format all text
for filename in os.listdir('CSE4062'):
    inputfile = csv.reader(open('CSE4062/' + filename, 'r', encoding='utf-8'))
    for row in inputfile:
        content.append(row[1])
        with open('Formated/'+ filename, 'w', encoding='utf-8') as file:
            for line in content:
                file.write(line + '\n')
    content = []

#extract usefull data
for filename in os.listdir('Formated'):
    with open('Formated/' + filename, 'r', encoding='utf-8') as f:
        d = {}
        outputfile = f.readlines()
        report_date.append(outputfile[1:2])
        date = outputfile[1:2]
        name = outputfile[6:]
        meeting_ID.append(outputfile[3:4])
        adSoyad.append(outputfile[6:])
        if date in d:
            d[date].append(name)
        else:
            d[date] = [name]

print(d)
#count the attendance
def word_count(fname):
    with open(fname, encoding='utf-8') as f:
        return Counter(f.readlines())
