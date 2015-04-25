################################################################################
#
# Author: Diego Montufar
# Date: Apr/2015
# Name: classifier.py
# Description: Performs Sentiment analysis for a given text.
#			   It uses text tokenization and normalization and the TexBlob
#              library. Emojis defined in sentiments.json will be considered as well
#			   in order to improve accuracy. 
#
# Import as:   import tweet_classifier as classifier
# Execute it:  print(classifier.doSentimentAnalysis("I'm happy to be here!"))
#
################################################################################
import re #Parsisng
from ttp import ttp #For extracting usernames and hashtags
from textblob import TextBlob #Parsing and Sentiment analysis
import json #Working with sentiments
import time
import os
# __file__ refers to the root directory 
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


#Open the sentiment.json file where emojis and other characters are defined
with open(APP_ROOT + '/sentiments.json') as sentiments_json:    
    sentiments = json.load(sentiments_json)

#Regex for detecting emails
email = "([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"
#Html wntities which must be removed
html_entities = {
			'&nbsp;':' ',
			'&lt;':'<',
			'&gt;':'>',
			'&amp;':'&'
}

#Regex to detect emails
email_regex = re.compile(email)

# Remove usernames, hashtags and urls
def extractUsernamesHashtagsURLS(ttp_obj,text):
	for username in ttp_obj.users:
		text = text.replace('@'+username,'')

	for tag in ttp_obj.tags:
		text = text.replace('#'+tag,'')

	for url in ttp_obj.urls:
		text = text.replace(url,'')
	return text

# Twitter text comes HTML-escaped, so unescape it.
# We also first unescape &amp;'s, in case the text has been buggily double-escaped.
def normalizeTextForTagger(text):
	for key, value in list(html_entities.items()):
		text = text.replace(key, value)
	return text

#Remove emails
def removeEmails(text):
	text = email_regex.sub('', text) #remove URL
	return text

#Remove line breaks helper
def removeLineBreaks(text):
	return text.replace('\n',' ')

#Parse Text:
#	1. Parse usernames, hashtags and urls and store then in ttp_result
#	2. Remove them from the text
#	3. Normalize HTML characters
#	4. Remove emails
#	5. Remove line breaks
#	6. Extract emojis and replace them with the sentiments defined in json file
#   7. Return clean version of the text ready to be analysed by TextBlob
def parseText(text):

	p = ttp.Parser()
	ttp_result = p.parse(text)
	text = extractUsernamesHashtagsURLS(ttp_result,text)
	text = normalizeTextForTagger(text)
	text = removeEmails(text)
	text = removeLineBreaks(text)

	# Loop over each character finding strange characters
	emojis = {}
	i = 1
	for character in text:
		if(ord(character)>128):
			#emojis[code] = span -> {code:span} pairs
			emojis[i] = str(ord(character)) 
		i+=1

	temp_text = list(text)
	for emoji in emojis:
		index = int(emoji) - 1
		if emojis[emoji] in sentiments["sentiments"]["emojis"]:
			temp_text[index] = str(sentiments["sentiments"]["emojis"][emojis[emoji]]) + " "
		else:
			temp_text[index] = "" 
	text = "".join(temp_text)

	return text #Return parsed/cleaned tweet

#Perform sentiment analysis
def getSentiment(tweet):
	# determine if sentiment is positive, negative, or neutral
	if tweet.sentiment.polarity < 0:
	    sentiment = "negative"
	elif tweet.sentiment.polarity == 0:
	    sentiment = "neutral"
	else:
	    sentiment = "positive"
	return sentiment


#Get the analysed text. This is the main method which perfomrs sentiment analysis
#The polarity score is a float within the range [-1.0, 1.0]. The subjectivity is a 
#float within the range [0.0%, 100.0%] where 0.0 is very objective and 100.0 is very subjective.
def doSentimentAnalysis(text):
	text = parseText(text)
	tweet = TextBlob(text)
	sentiment = getSentiment(tweet)
		
	return { 'text': text, 
		'sentiment': sentiment, 
		'subjectivity': tweet.subjectivity* 100.0,
		'polarity': tweet.polarity }

