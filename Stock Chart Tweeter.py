from twython import Twython, TwythonError, TwythonStreamer
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc
from matplotlib import style
import datetime

APP_KEY= '********'
APP_SECRET= '********'
OAUTH_TOKEN= '********'
OAUTH_TOKEN_SECRET= '********'
api = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def tweet_chart_image():
    photo = open('/Users\merca\Desktop/stock_chart_image.png', 'rb')
    response = api.upload_media(media=photo)
    api.update_status(status='$' + str.upper(stock) + ' Chart', media_ids=[response['media_id']])
    
while True:
    stock = input('Enter Stock\n')
    date1 = (2016, 9, 1)
    date2 = datetime.date.today()

    mondays = WeekdayLocator(MONDAY)      
    alldays = DayLocator()             
    weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
    dayFormatter = DateFormatter('%d')      # e.g., 12

    quotes = quotes_historical_yahoo_ohlc(stock, date1, date2)
    if len(quotes) == 0:
        raise SystemExit
    
    style.use('fivethirtyeight')
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    ax.xaxis.set_major_locator(mondays)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(weekFormatter)
    
    candlestick_ohlc(ax, quotes, width=0.7, colorup='#19caf7', colordown='#6c6c6c')
    ax.xaxis_date()
    ax.autoscale_view()
    ax.yaxis.tick_right()
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.grid(color = '#4c4c4c', linewidth=.25)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(str.upper(stock))
    fig.set_size_inches(19.5, 10.5, forward=True)
    plt.savefig('stock_chart_image.png')
    
    print('File Saved')
    tweet_chart_image()
    print('Stock Chart Tweeted')
    #plt.show()
