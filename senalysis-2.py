#!/usr/local/bin/python
#coding:utf8

from pyavrophonetic import avro
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

banglish = "ami to shudhu Ilish je Chandpur er eita confirm korechilam... Shorshe r sathe mile je sorshe ilish namok shushadu khabar toiri hobe ami ki jani."
#banglish = "আগামী ২০ থেকে ২৭ জুলাই পর্যন্ত (শুক্রবার ব্যতীত) নগরীর হ্যানে রেলওয়ে মাধ্যমিক স্কুলে সদরের ২১নং ওয়ার্ডের ভোটারদের স্মার্ট কার্ড বিতরণ করা হবে। এছাড়া ৩০ জুলাই"
print banglish

tr_bng = avro.parse(banglish)
print tr_bng

blob = TextBlob(tr_bng)
tr_eng = blob.translate(to="en")
print tr_eng.sentences

analyser = SentimentIntensityAnalyzer()
def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(snt)))

for sentence in tr_eng.sentences:
        #print type(sentence)
        stn =  unicode(sentence)
        print_sentiment_scores(stn)
