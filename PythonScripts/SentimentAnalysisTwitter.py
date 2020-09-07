import csv
import nltk
from nltk.corpus import stopwords
from prettytable import PrettyTable
from nltk.stem.wordnet import WordNetLemmatizer

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

trainData ={}
positiveWords = {}
negativeWords = {}
x = PrettyTable()
outtweets =[]
lem = WordNetLemmatizer()
x.field_names = ["Tweet", "Message/tweets", "Match", "polarity", "polarity score"]
with open('sentiWords.csv') as train_file:
    lines=0
    csv_reader1 = csv.reader(train_file, delimiter=',')
    next(csv_reader1)
    trainData = {rows[0]: float(rows[2]) for rows in csv_reader1}

with open('all_tweets.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    next(csv_reader)
    stop_words = set(stopwords.words('english'))
    for row in csv_reader:
        wordfreq = {}
        pos = []
        neg = []
        posWords = {}
        negWords = {}
        neutralWords = []
        neutral = []
        line_count += 1
        tokens = nltk.word_tokenize(row[0])

        # Creating bag of words and lemmanitizing for semantic comparison
        for token in tokens:
            if token not in stop_words:
                if token not in wordfreq.keys():
                    wordfreq[lem.lemmatize(token)] = 1
                else:
                    wordfreq[lem.lemmatize(token)] += 1

        # Tagging train data against testdata
        for key in wordfreq:
            if key in trainData:
                if trainData[key]>0:
                    pos.append(wordfreq[key]*trainData[key])
                    posWords[key] = wordfreq[key]
                elif trainData[key]<0:
                    neg.append(wordfreq[key]*trainData[key])
                    negWords[key] = wordfreq[key]
                else:
                    neutral.append(wordfreq[key]*trainData[key])
                    neutralWords.append(key)

        # Calculating total polarity by performing summation
        polarity = sum(pos)+sum(neg)+sum(neutral)
        polVal = "Positive" if polarity>0 else "Negative" if polarity<0 else "Neutral"
        matched_words = list(posWords.keys())
        matched_words.extend(list(negWords.keys()))
        matched_words.extend(neutralWords)
        x.add_row([line_count, row[0], ', '.join(matched_words), polVal, polarity])
        outtweets.append([line_count, row[0], ', '.join(matched_words), polVal, polarity])
        if polarity >0:
            for key in posWords:
                positiveWords[key] = posWords[key] if key not in positiveWords.keys() else positiveWords[key]+posWords[key]
        elif polarity<0:
            for key in negWords:
                negativeWords[key] = negWords[key] if key not in negativeWords.keys() else negativeWords[key]+negWords[key]

print(x)

with open('outTweets.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Tweet", "Message/tweets", "Match", "polarity", "polarity score"])
    writer.writerows(outtweets)

with open('positiveWords.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Positive words", "frequency"])
    for key, value in positiveWords.items():
        writer.writerow([key, value])

with open('negativeWords.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Negative words","frequency"])
    for key, value in negativeWords.items():
        writer.writerow([key, value])

pass
print(f'Processed {line_count} lines.')