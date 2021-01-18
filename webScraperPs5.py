import requests
from bs4 import BeautifulSoup
import time
import smtplib
import tweepy

consumer_key        = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret     = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token        = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Ger access till hemsidorna 
elgiganten = requests.get("https://www.elgiganten.se/product/gaming/spelkonsol/playstation-konsol/220276/playstation-5-ps5")
srcElgiganten = elgiganten.content
soupElgiganten = BeautifulSoup(srcElgiganten, 'lxml')

mediaMarkt = requests.get("https://www.mediamarkt.se/sv/product/_sony-playstation-5-ps5-1328021.html")
srcMediaMarkt = mediaMarkt.content
soupMediaMarkt = BeautifulSoup(srcMediaMarkt, 'lxml')

netOnNet = requests.get("https://www.netonnet.se/art/gaming/spel-och-konsol/playstation/playstation-konsol/sony-playstation-5/1012886.14413/")
srcNetonNet = netOnNet.content
soupNetonNet = BeautifulSoup(srcNetonNet, 'lxml')

#Hämtar data från HTML-koden 
dataElgiganten = soupElgiganten.find('span',attrs={'class':'product-price-text'})
dataMediaMarkt = soupMediaMarkt.find('li', attrs={'class': 'false online-nostock'})
dataNetonNet = soupNetonNet.find('div', attrs={'class': 'deliveryInfoText'})

#Kollar ifall texten stämmer på hemsidorna, ifall de inte stämmer skickas en tweet ut som säger att Ps5 går att köpa 
while (True):
	if 'Ej köpbar' in dataElgiganten.text: 
		print ('Ps5 ej tillgängligt Elgiganten')
	else:
		api.update_status('Ps5 är tillgängligt på Elgiganten')
		break

	if 'Ej i webblager' in dataMediaMarkt.text:
		print ('Ps5 ej tillgängligt MediaMarkt')
	else:
		api.update_status('Ps5 är tillgängligt på MediaMarkt')
		break

	if 'Lev.tid ej bekräftad' in dataNetonNet.text:
		print('Ps5 ej tillgängligt NetOnNet')
	else: 
		api.update_status('Ps5 är tillgängligt på NetOnNet')
		break
	time.sleep(10)