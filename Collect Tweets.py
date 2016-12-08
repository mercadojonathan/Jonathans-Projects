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
APP_KEY= 'SJVvysQTPqZxrFVZ82ivzSKEy'
APP_SECRET= 'WqgVoayIknJyiJ7JQ3WnFdSV6uHIdJgHP6BhHBSETgtaiTSiop'
OAUTH_TOKEN= '723310937176838146-R0lezdpCXgs5362D3UhvAj1p2xz76nz'
OAUTH_TOKEN_SECRET= 'atactBZ48vAJals9XhQWTOy7J7wmc1VevZ9BockvBimgF'
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#|-------------------------------------------------------|
#| STOCK LISTS                                                           |
#|-------------------------------------------------------|
stock_list = '$FB,$BAC,$TWTR,$X,$MU,$SBUX,$WLL,$AMD,$TWLO,$HPQ,$OAS,$ECA,$TCK,$WFM,$P,$JCP,$FIT,$JBLU,$CNX,$GPRO,$SCTY,$SQ,$SHOP,$ETSY,$MPEL,$REN'
#|--------------------------------------------------------|
#| STRING VARIABLES                                                 |
#|--------------------------------------------------------|
select_criteria  = 'Please select from the following ctiteria\n'
list_options = '\n1 for Tweet\n2 for Follow\n3 for Stream\n4 for Search\n5 For Stock Data \n'
request_tweet = 'What would you like to tweet?\n'
request_verification= 'Are you sure you would like to send this tweet? y/n\n'
fol_unfol = 'Follow Or Unfollow? f/u\n'
request_target = 'Who would you like to follow?\n'
unfollow_target = "Who would you like to Unfollow?\n"
next_target = 'Who would you like to follow next?\n'
keyword = "What would you like to Stream?\n"
search_str = 'What would you like to Search for?\n'

#|-------------------------------------------------------|
#| STREAM & SAVE FUNCTION                                |
#|-------------------------------------------------------|           
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            try:
                print(data['text'])     #.encode('utf-8'))
                stream_data = TextBlob(data['text'])
                sent_pol = stream_data.sentiment
                print(sent_pol)
                save_data = str(dt.datetime.now()) + '::' + data['text'] #.encode('utf-8')
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
        for each_status in status:
            name = each_status['screen_name']
            print(name)
    else:
        status = stream.statuses.filter(track=key_word)
        
stream_filter()
# stream.user()
# Read the authenticated users home timeline
# (what they see on Twitter) in real-time
# stream.site(follow='twitter')
#|---------------------------------------------------------|
#| APP FUNCTIONS                                                       |
#|---------------------------------------------------------|


def options(selection): # Define User Options Function 
    if(selection == '1'):
        return 1
    elif(selection == '2'):
        return  2
    elif(selection == '3'):
        return 3
    elif(selection == '4'):
        return 4
    elif(selection == '5'):
        return 5
                                
def send_tweet(yon): # Define Tweet Send Verification
    if(yon == 'y' ):
        return 3
    elif(yon == 'n' ):
        return 4
    
def fol_opt(opt): # Define follow or unfollow otions
    if(opt == 'f'):
        return 5
    elif(opt == 'u'):
        return 6
    
def  main_menu():
    ask_order = input(list_options)
    global choice
    choice = options(ask_order)

def tweet_func():
        message = input(request_tweet)
        if(message != 0):
            send = input(request_verification + '"' + message + '"' +'\n')
            verify_tweet = send_tweet(send)
        if(verify_tweet == 3):
            twitter.update_status(status = message)
            print('Tweet Sent')
        if(verify_tweet == 4):
            print('Tweet Not Sent')

def follow_opts():
    follow_options = input(fol_unfol)
    global fol_dec
    fol_dec = fol_opt(follow_options)

def follow_targ():
    follow_target = input(request_target)
    twitter.create_friendship(screen_name=follow_target, follow="true")
    print('\nNow Following... ' + follow_target +'!\n')
    
def unfollow_targ():
    global unfollow_target
    unfollow_target = input(unfollow_target)
    twitter.destroy_friendship(screen_name=unfollow_target)
    print('""'+ unfollow_target +'""'+ ' is no longer being followed')


#   take this and make it stop looping the same tweets
        #   Code currently Rate Limiting 
def search_func():
    search_keys = input(search_str)
    count = input('How many results would you like returned?\n')
    results = twitter.cursor(twitter.search, q=search_keys, count = count)
    
    for tweet in results:
        try:
            print(tweet['text'])
            data = TextBlob(tweet['text'])
            print(data.sentiment)
            
        except:
            print('something broke while pulling data')
            time.sleep(3)


#Calculate Dollar Volume
#Calculate Avg Daily Range
#Calculate Avg Daily Overnight Range
0
def stock_data():
    ticker = input('Enter Stock Ticker\n')
    symbol = Share(ticker)
    price = float(symbol.get_price())
    volume = float(symbol.get_volume())
    million = (price)*(volume)
    print(price)
    print(volume)
    print(million)
    
     
     
#|---------------------------------------------------------|
#| MAIN PROGRAM LOGIC                                          |
#|---------------------------------------------------------|
try:
   while True:
        main_menu()
        if(choice == 1):
            tweet_func()
            
        elif(choice == 2):
            follow_opts()
            
            if(fol_dec == 5):
                follow_targ()
                
            elif(fol_dec == 6):
                unfollow_targ()

        elif(choice == 3):      
            stream_filter()

        elif(choice == 4):
            search_func()

        elif(choice == 5):
            stock_data()
                

except TwythonError as e:
    print(e)

