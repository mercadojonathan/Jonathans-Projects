# Collect tweets from users tweeting about stock in Stock List
# Save Twitter handles to S

from twython import Twython, TwythonError, TwythonStreamer
import time

APP_KEY= 'SJVvysQTPqZxrFVZ82ivzSKEy'
APP_SECRET= 'WqgVoayIknJyiJ7JQ3WnFdSV6uHIdJgHP6BhHBSETgtaiTSiop'
OAUTH_TOKEN= '723310937176838146-R0lezdpCXgs5362D3UhvAj1p2xz76nz'
OAUTH_TOKEN_SECRET= 'atactBZ48vAJals9XhQWTOy7J7wmc1VevZ9BockvBimgF'
api = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

stock_list = '$BAC,$TWTR,$X,$MU,$AMD,$HPQ,$P,$JCP,$FIT,$JBLU,$GPRO,$SCTY,$SQ,$SHOP,$ETSY'
keyword = "What would you like to Stream?\n"
list_options = 'Would you like to Stream of Follow?\n'

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            try:
                name = data['user']['screen_name']
                save_data = name
                saveFile = open('Twitter Handles.json', 'a')
                saveFile.write(save_data)
                saveFile.write('\n')
                saveFile.close()
                print(name + '\n')
                return True
            
            except BaseException:
                print('Write Data Failed\n')
            
    def on_error(self, status_code, data):
        print(status_code, data)

stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)       
def stream_tweets():
    key_word= input(keyword)
    if(key_word == 'stock list'):
        status = stream.statuses.filter(track=stock_list)
    else:
        status = stream.statuses.filter(track=key_word)
        
def follow_from_file():
    global read_file
    read_file = open('Twitter Handles.json', 'r')
    handle_list = read_file.readlines()
    for each_handle in handle_list:
        api.create_friendship(screen_name=each_handle, follow="true")
        print('\nNow Following... ' + each_handle +'!\n')
        time.sleep(1)
        
def options(selection) :   
    if(selection == 'stream'):
        return 1
    elif(selection == 'follow'):
        return 2
    
def main():
    ask_order = input(list_options)
    global choice
    choice = options(ask_order)
    
try:
    while True:
        main()
        if(choice == 1):
            stream_tweets()
        elif(choice == 2):
            follow_from_file()
except TwythonError as e:
    print(e)

