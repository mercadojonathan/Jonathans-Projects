#|---------------------------------------------------------|
#| IMPORT                                                                      |
#|---------------------------------------------------------|
from twython import Twython, TwythonError, TwythonStreamer
import sys
import time
import datetime as dt
from textblob import TextBlob
from yahoo_finance import Share
#|--------------------------------------------------------|
#| OATH KEYS                                                               |
#|--------------------------------------------------------|
APP_KEY= '********'
APP_SECRET= '********'
OAUTH_TOKEN= '********'
OAUTH_TOKEN_SECRET= '********'
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#|-------------------------------------------------------|
#| STOCK LISTS                                                           |
#|-------------------------------------------------------|
stock_list = '$FB,$BAC,$TWTR,$X,$MU,$SBUX,$WLL,$AMD,$TWLO,$HPQ,$OAS,$ECA,$TCK,$WFM,$P,$JCP,$FIT,$JBLU,$CNX,$GPRO,$SCTY,$SQ,$SHOP,$ETSY,$MPEL,$REN'
#|--------------------------------------------------------|
#| STRING VARIABLES                                                 |
#|--------------------------------------------------------|
keyword = "What would you like to Stream?\n"
#|-------------------------------------------------------|
#| STREAM & SAVE FUNCTION                                |
#|-------------------------------------------------------|
handles = []
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            try:
                #print(data['text'])     #.encode('utf-8'))
                global name
                name = data['user']['screen_name']
                print(name)
                #date = str(dt.datetime.now())
                save_data = name#date + '\n' + data['text'] + '\n' + name #.encode('utf-8')
                saveFile = open('STREAM.json', 'a') #a = apphend the data
                saveFile.write(save_data)
                saveFile.write('\n')
                saveFile.close()
                print('Task Complete\n')
                return True
            
            except BaseException:
                print('Failed on Data\n')
                time.sleep(2)
            
    def on_error(self, status_code, data):
        print(status_code, data)

stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def stream_filter(): # define streaming function
    key_word= input(keyword)
    
    if(key_word == 'stock list'):
        status = stream.statuses.filter(track=stock_list)
    else:
        status = stream.statuses.filter(track=key_word)

# Create Function that opens handles list and follows each target
def follow_targ():
    read_file = open('STREAM.json', 'r')
    read_file.read()
    follow_target = input(request_target)
    twitter.create_friendship(screen_name=follow_target, follow="true")
    print('\nNow Following... ' + follow_target +'!\n')
    

stream_filter()
#print(handles)
# stream.user()
# Read the authenticated users home timeline
# (what they see on Twitter) in real-time
# stream.site(follow='twitter')
