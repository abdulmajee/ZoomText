from collections import Counter
import os
import csv
import pandas as pd
import _pickle as pickle
import json


content = []
for filename in os.listdir('CSE4062'):
    inputfile = csv.reader(open('CSE4062/' + filename, 'r', encoding='utf-8'))
    for row in inputfile:
        # adSoyad.append(row[1])
        content.append(row[1])

with open('Formated/rapor.txt', 'w', encoding='utf-8') as file:
    for adSoyad in content:
        file.write(adSoyad + '\n')

def word_count(fname):
        with open(fname, encoding='utf-8') as f:

            return Counter(f.readlines())

# print(word_count("Formated/rapor.txt").items())
# majeed = word_count("Formated/rapor.txt")
# with open('file.txt', 'w') as file:
#     file.write(str(pickle.dumps(majeed)))  # use `json.loads` to do the reverse
# # print(majeed.items())

for item in word_count("Formated/rapor.txt").items():
    name = item[0]
    count = item[1]
    # df = pd.DataFrame({name, item})
    data = {'name':name, 'count' : count}
    df = pd.DataFrame(data, index=[0])
    # print(count)
    print((name,count))
    # with open('Formated/exellfile.csv', 'w', encoding= 'UTF8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(df)
