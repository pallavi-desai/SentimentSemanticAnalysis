import csv
import json
import re
import math
import nltk

from prettytable import PrettyTable

# reading original file and writing the required fields i.e title, description, content
with open('data1.json','r+') as json_file:
    data = json.load(json_file)
    for i in range(len(data)):
        data[i] = {'title': data[i]['title'], 'description': data[i]['description'], 'content': data[i]['content']}
    json_file.seek(0)
    json.dump(data, json_file, indent=4)
    json_file.truncate()

searchKey = {"canada":0, "university":0, "dalhousie":0, "halifax":0, "business":0}
canadaFrequency = {}
x = PrettyTable()
y = PrettyTable()
with open('data1.json') as f:
    data = json.load(f)
    totalDocs = len(data)
    largest = -1
    article = 0
    for i in range(len(data)):
        tokens = nltk.word_tokenize(re.sub("[^A-Za-z0-9]+", " ", data[i]['title'].lower()))
        tokens.extend(nltk.word_tokenize(re.sub("[^A-Za-z0-9]+", " ", data[i]['description'].lower())))
        tokens.extend(nltk.word_tokenize(re.sub("[^A-Za-z0-9]+", " ", data[i]['content'].lower())))
        # Calculating number of articles matching search query
        for key in searchKey.keys():
            if(key in data[i]['title'].lower() or key in data[i]['description'].lower() or key in data[i]['content'].lower()):
                searchKey[key] +=1

        # calculating the frequency of term Canada in news articles
        if 'canada' in tokens:
            total = len(tokens)
            freq = tokens.count('canada')
            relFreq = freq/total
            if relFreq > largest:
                largest = relFreq
                article = i
            canadaFrequency[i] = [total, freq, tokens.count('canada')/len(tokens)]

# Creating and printing result tables
x.field_names = ["Search Query", "Document containing term df", "Total documents(N)/ Number of documents term appeared df", "log10(N/df)"]
with open('Table1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Search Query", "Document containing term df", "Total documents(N)/ Number of documents term appeared df", "log10(N/df)"])
    for key in searchKey:
        writer.writerow([key, searchKey[key], totalDocs/(searchKey[key] if searchKey[key]!= 0  else 1), math.log(totalDocs/(searchKey[key] if searchKey[key]!= 0  else 1),10)])
        x.add_row([key, searchKey[key], totalDocs/(searchKey[key] if searchKey[key]!= 0  else 1), math.log(totalDocs/(searchKey[key] if searchKey[key]!= 0  else 1),10)])

print("Total Documents:", totalDocs)
print(x)

y.field_names = ["Canada appeared in "+str(searchKey['canada'])+" documents", "Total words (m)", "Frequency(f)"]

with open('Table2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Canada appeared in "+str(searchKey['canada'])+" documents", "Total words (m)", "Frequency(f)"])
    for key in canadaFrequency:
        writer.writerow(["Article #"+str(key), canadaFrequency[key][0], canadaFrequency[key][1]])
        y.add_row(["Article #"+str(key), canadaFrequency[key][0], canadaFrequency[key][1]])

print("Term : Canada")
print(y)

print("Article with maximum relative frequency :", largest)
print(data[article])