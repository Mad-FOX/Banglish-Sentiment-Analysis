#!/usr/local/bin/python

from pyavrophonetic import avro
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import sys

b = input("Enter Banglish :")

textBlobTrans = TextBlob(avro.parse(b))

c = str(textBlobTrans.translate(to='en'))
print(c)

analyze = TextBlob(c)
print('By TextBlob Sentiment analysis')
print(analyze.sentiment)

print('By vaderSentiment analyzer')
analyzer = SentimentIntensityAnalyzer()
vs = analyzer.polarity_scores(c)

print(str(vs))
