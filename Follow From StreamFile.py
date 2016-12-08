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


# Create Function that opens handles list and follows each target
def follow_targ():
    global read_file
    read_file = open('STREAM.json', 'r')
    handle_list = read_file.readlines()
    for each_handle in handle_list:
        print(each_handle)
        #twitter.create_friendship(screen_name=each_handle, follow="true")
        print('\nNow Following... ' + each_handle +'!\n')
follow_targ()    
read_file.close()

# Write another Function that Cross References symbols with those from Friend's List
