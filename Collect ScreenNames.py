# Collect tweets from users tweeting about stock in Stock List
# Save Twitter handles to S

from twython import Twython, TwythonError, TwythonStreamer

APP_KEY= '********'
APP_SECRET= '********'
OAUTH_TOKEN= '********'
OAUTH_TOKEN_SECRET= '********'
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

stock_list = '$FB,$BAC,$TWTR,$X,$MU,$SBUX,$WLL,$AMD,$TWLO,$HPQ,$OAS,$ECA,$TCK,$P,$JCP,$FIT,$JBLU,$CNX,$GPRO,$SCTY,$SQ,$SHOP,$ETSY,$MPEL'
keyword = "What would you like to Stream?\n"

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            try:
                global name
                name = data['user']['screen_name']
                save_data = name
                saveFile = open('STREAM.json', 'a')
                saveFile.write(save_data)
                saveFile.write('\n')
                saveFile.close()
                print('Task Complete\n')
                return True
            
            except BaseException:
                print('Write Data Failed\n')
            
    def on_error(self, status_code, data):
        print(status_code, data)

stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
def stream_filter():
    key_word= input(keyword)
    if(key_word == 'stock list'):
        status = stream.statuses.filter(track=stock_list)
    else:
        status = stream.statuses.filter(track=key_word)

# Create Function that opens handles list and follows each target
def follow_from_file():
    global read_file
    read_file = open('STREAM.json', 'r')
    handle_list = read_file.readlines()
    for each_handle in handle_list:
        twitter.create_friendship(screen_name=each_handle, follow="true")
        print('\nNow Following... ' + each_handle +'!\n')
    

stream_filter()
stream.user()
follow_from_file()

