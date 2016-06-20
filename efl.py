import random
from facepy import GraphAPI
import datetime

start = ["Goedenavond", "Het is weer van da", "Een goede avond", "Beste lab genoten", "Beste mensen", "603D3N4V0ND", "01000111 01101111 01100101 01100100 01100101 01101110 01100001 01110110 01101111 01101110 01100100", "67 6f 65 64 65 6e 61 76 6f 6e 64", "dnovanedeoG"]
mid = ["morgen is het lab terug open", "dinsdag avond lab avond", "dinsdag (nu morgen, morgen vandaag) is het lab terug open", "morgen zijn we open", "we zijn morgen weer open", "morgen is iedereen welkom", "het lab zal terug open zijn morgen", "morgen (dinsdag), opnieuw open", "morgen is het lab terug open"]
end = ["Wie komt er morgen avond naar het lab?", "Wie komt er morgen?", "Wie is er morgen van de partij?", "Wie komt er af?", "Kom je morgen geef dan een seintje!", "Wie komt er?", "Iedereen is welkom, maar laat gerust hier weten dat je komt.", "Laat van je horen als je komt.", "Geef een seintje als je komt.", "Laat iets weten als je morgen komt.", "Kom je af?", "Spring gerust binnen.", "Kom je langs? Geef een seintje!"]
extra = [" ", "Wat zijn je plannen?", "Waarmee ben je bezig?"]


today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)

t = "niets"
t = random.choice(start)+", "+random.choice(mid)+" ("+tomorrow.strftime('%d/%m')+"). "+random.choice(end)+" "+random.choice(extra)
#access_token = facebookat["Accestoken"]
access_token = "ADD YOU ACCESTOKEN HERE"
apiConnection = GraphAPI(access_token)
apiConnection.post(path='me/feed',
                        message=t)
