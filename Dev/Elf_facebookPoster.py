import random
from facepy import GraphAPI
import datetime
import ConfigParser

config = ConfigParser.RawConfigParser()

start = ["Goedenavond", "Het is weer van da", "Een goede avond", "Beste lab genoten", "Beste mensen", "603D3N4V0ND", "01000111 01101111 01100101 01100100 01100101 01101110 01100001 01110110 01101111 01101110 01100100", "67 6f 65 64 65 6e 61 76 6f 6e 64", "dnovanedeoG"]
mid = ["morgen is het lab terug open", "dinsdag avond lab avond", "dinsdag (nu morgen, morgen vandaag) is het lab terug open", "morgen zijn we open", "we zijn morgen weer open", "morgen is iedereen welkom", "het lab zal terug open zijn morgen", "morgen (dinsdag), opnieuw open", "morgen is het lab terug open"]
end = ["Wie komt er morgen avond naar het lab?", "Wie komt er morgen?", "Wie is er morgen van de partij?", "Wie komt er af?", "Kom je morgen geef dan een seintje!", "Wie komt er?", "Iedereen is welkom, maar laat gerust hier weten dat je komt.", "Laat van je horen als je komt.", "Geef een seintje als je komt.", "Laat iets weten als je morgen komt.", "Kom je af?", "Spring gerust binnen.", "Kom je langs? Geef een seintje!"]
extra = [" ", "Wat zijn je plannen?", "Waarmee ben je bezig?"]
today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)

config.read('FBPconfig.cfg')
access_token = config.getfloat('login', 'fb_ac_token')

if access_token:
	if access_token = 1:
		print "Error - No access token"
		fb_ac_token = input("Please enter a valid access_token: ")

		config.set('login', 'fb_ac_token', fb_ac_token)
		with open('FBPconfig.cfg', 'wb') as configfile:
    		config.write(configfile)
	else:
		t = "niets"
		t = random.choice(start)+", "+random.choice(mid)+" ("+tomorrow.strftime('%d/%m')+"). "+random.choice(end)+" "+random.choice(extra)
		apiConnection = GraphAPI(access_token)
		apiConnection.post(path='me/feed',
	                        message=t)
else:
	fb_ac_token = 1
	fb_ac_token = input("Please enter a valid access_token:")
	fb_app_sec = 1
	fb_app_sec = input("Please enter a your app secret:")
	fb_app_id = 1
	fb_app_id = input("Please enter a your app id:")

	config.add_section('login')
	config.set('login', 'fb_ac_token', fb_ac_token)
	config.set('login', 'fb_app_id', fb_app_id)
	config.set('login', 'fb_app_secret', fb_app_sec)

	with open('FBPconfig.cfg', 'wb') as configfile:
    	config.write(configfile)
