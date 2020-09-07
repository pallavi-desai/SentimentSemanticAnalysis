import omdb
import json

omdb.set_default('apikey', 'f7d0f49f')

movieData = omdb.search('Canada') + omdb.search('University') + omdb.search('University') + omdb.search('Moncton') + omdb.search('Halifax') + omdb.search('Toronto') + omdb.search('Vancouver') + omdb.search('Alberta') + omdb.search('Niagara')

titles = []
length = len(movieData)
for i in range(length):
    titles.append(movieData[i]['title'])

finalData = []
for j in range(length):
    finalData.append(omdb.get(title=titles[j]))

with open('MovieData.json', 'w') as outputFinal:
    json.dump(finalData, outputFinal)
