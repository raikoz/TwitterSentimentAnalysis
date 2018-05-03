import tweepy
from textblob import TextBlob

#4 variables for authenticating Twitter

consumer_key = 'dWyZGyWwbzZo1WERZfkQh09rs'
consumer_secret = 'ulQyEXg9W9AzZOsbrHSwbXrQt5VadeIeyQtrMKWolYc4jLlBYJ'

access_token = '265401815-FNFGKK8frlSCNYse151DtkV5fC7MwCJXNrz9brAP'
access_token_secret = 'gP6ARwKjBapadP3UbVzxNp9mJFBghpDXby4LmQHjGEu16'

#login via code, method inside tweepy library

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#main variable for the twitter magic

api = tweepy.API(auth)

#collect tweets that contain a certain keyword

public_tweets = api.search('Zuckerberg')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print("    ")
	print("    ")
	print("    ")
	print("    ")

#polarity- +ve or -ve some text is
#subjectivity- opinion or factual some text is
