# Banglish-Sentiment-Analysis
## Sentiment analysis for phonetic Bengali sentences.
---------------------------------------------------

### Our steps are:

Module 1: Bengali Phonetic/Banglish -> Bengali. Ex: “ami valo achi” to “আমি ভাল আছি”

Module 2: Bangla -> English. Ex: “আমি ভাল আছি” to “I am fine”

Module 3: English -> Sentimental Analysis: Ex: “I am fine” to “positive: 100% negative 0%”

### Module 1 (Bengali Phonetic/Banglish -> Bengali):

At first, we used avro for python that was in pyavrophonetics library,sourced from github.
https://github.com/omicronlab/pyAvroPhonetic/
PyAvroPhonetic is a implementation of popular avro keyboard’s bangla phonetic in Python.
We installed this package and used in our tool development. We have seen that this tool can work well
with it and we can find Banglish to Bangla very efficiently.
In order to get Bangla text from a Banglish Text, first we need to import the avro module from
pyavrophonetic package. Then we can parse any text using avro.parse() method.
Example: avro.parse(‘ami banglay gan gai’)

### Module 2 (Bengali -> English):

For this module, we undertook two approaches that we thought will be efficient to get English
Translation.
1. Web Scrapping using Python.
2. Using API.
English Translation Sentiment Input Banglish Bangla Text

Vader Library TextBlob Library PyAvroPhonetic

In terms of WebScrapping using python (bs4 + request module), it was seen that getting translation
takes substantially longer time and the text range of the translation is not much. i.e It can’t translate a
bangla text that is a bit large.

Then, we used Textblob package source from https://textblob.readthedocs.io/en/dev.
Textblob is a python package primarily used for analyzing text and find different features like Noun
phrase detection, Parts of Speech tagging, Sentiment analysis etc. But playing with this package, we’ve
found a method that calls google translate api and gives translation to any intended language. It is this
package that we’ve got substantially better result while translation Bangla to English. Also the
translation procedure takes much less time.
sample code: TextBlob(avro.parse(‘ami valo achi’)).translate(to='en’)

### Module 3 (English -> Sentiment Analysis):

Packages Used:
1. TextBlob
2. Vader
This is the last category of our working procedures. First, we used “textblob” again for sentimental
analysis. It gives three outputs that are: positive, negative, neutral of a desired input. The TextBlob
library uses Naïve-Bayes algorithm, a statistical algorithm, that gives poor result in sentiment analysis.
Next we had used vader sentiment package from https://pypi.python.org/pypi/vaderSentiment. Vader is
a lexicon and rule based sentiment analysis tool especially designed to analyse the social media feed.
Installing this package and using it, we have found that this package gives very precise analysis of
sentiment. There are four sentiment outputs that are: positive, negative, neutral, compound. We can
also manually provide a threshold for a text to be positive and negative.
Now, we want to improve this prototype for better performance in an effective way with accuracy.

### Key Findings in our Analysis:

1. Although Avro is the dominant bangla phonetic generator, it cant parse banglish text with 100%
efficiency. i.e ‘ korte’ ‘করতে’ ‘ekta’’একতা’
2. Translating through webscrapping is a slow and error-prone process.
3. TextBlob’s main purpose was to analyse the input text to extract the sentiment. But it is poor in
analyzing sentiment.
4. TextBlob’s built in translate method that uses google api, gives a better and faster translation of
Bengali to English.
5. Lexicon and Rule-Based Method is better than Naïve-Bayes algorithm in SA.
6. We can change vander compound threshold to determine positive and negative sentiment.
7. In order to improve SA, we must pay attention to banglishbangla conversion module. Maybe
normalize the input text or improve the avro phonetic library.

--------------------------------------------------------------
Initial expermentation conducted by:
Avijit Bhattacharjee (KU-140212), Imran Hossain (KU-140231), Subrato Sarker (KU-140236)
