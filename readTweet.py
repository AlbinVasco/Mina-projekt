import requests
from bs4 import BeautifulSoup
import time
import smtplib
import tweepy
import random 
import webbrowser
import os 


#Scannar en twitter sida som jag kontrollerar och om ett visst kommando skrivs ska olika typer av webbläsare öppnas 
#Tíll exempel och jag tweetar mat ska detta script öppa Youtube och spela upp en matvideo  

consumer_key        = 'G0xahwGqCx9qtckPFs5ZuCaAg'
consumer_secret     = 'BE8aQ9HXk7QZ8PcBAKnDuGbxuAdhikavSko5qDr8JCGZp55seg'
access_token        = '1025068184-LYoov9ogM06iA8MW9VkrqY2GTVFFNbLuoF0Vlac'
access_token_secret = 't2PdE6D4tgUDtisCP6UVBAPWeEn3zUYKslIbAPWrknX3P'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

userID = 'AlbinKAllner'

# Funktion hämtar en random url från en .txt fil och öppnar den i Chrome
def openBrowser(fileName):
	lines = open(fileName).read().splitlines()
	url =random.choice(lines)
	webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
	webbrowser.get('chrome').open(url)

while (True):
	tweets = api.user_timeline(screen_name=userID, count=1, include_rts = False, tweet_mode = 'extended')
	
	for info in tweets:
		tweet = info.full_text
		tweet_id = info.id
		print(tweet)

	if tweet == 'mat':
		openBrowser('mat.txt') #Öppnar en webbläsare från mat.txt 
		time.sleep(2)
		api.destroy_status(tweet_id) #Tar bort tweeten 

	elif tweet == 'musik':
		openBrowser('musik.txt')
		time.sleep(2)
		api.destroy_status(tweet_id)

	elif tweet == 'film':
		openBrowser('film.txt')
		time.sleep(2)
		api.destroy_status(tweet_id)

	elif tweet == 'ny film':
		os.system("taskkill /im chrome.exe /f")
		time.sleep(2)
		openBrowser('film.txt')
		api.destroy_status(tweet_id)

	elif tweet == 'stäng av dator':
		os.system("taskkill /im chrome.exe /f") #Stänger ner Chrome
		time.sleep(2)
		api.destroy_status(tweet_id) 
		time.sleep(5)
		#os.system('shutdown -s') #Stänger av datorn 

	time.sleep(3)



