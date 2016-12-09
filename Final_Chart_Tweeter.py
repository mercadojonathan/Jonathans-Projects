from twython import Twython, TwythonError, TwythonStreamer
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc
from matplotlib import style
import datetime

APP_KEY= 'SJVvysQTPqZxrFVZ82ivzSKEy'
APP_SECRET= 'WqgVoayIknJyiJ7JQ3WnFdSV6uHIdJgHP6BhHBSETgtaiTSiop'
OAUTH_TOKEN= '723310937176838146-R0lezdpCXgs5362D3UhvAj1p2xz76nz'
OAUTH_TOKEN_SECRET= 'atactBZ48vAJals9XhQWTOy7J7wmc1VevZ9BockvBimgF'
api = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


def tweet_chart_image():
    photo = open('/Users\merca\Desktop/stock_chart_image.png', 'rb')
    response = api.upload_media(media=photo)
    api.update_status(status='$' + str.upper(stock) + ' Chart', media_ids=[response['media_id']])


while True:
    stock = input('Enter Stock\n')
    # (Year, month, day) tuples suffice as args for quotes_historical_yahoo
    date1 = (2016, 9, 6)
    date2 = datetime.date.today()

    mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
    alldays = DayLocator()              # minor ticks on the days
    weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
    dayFormatter = DateFormatter('%d')      # e.g., 12

    quotes = quotes_historical_yahoo_ohlc(stock, date1, date2)
    if len(quotes) == 0:
        raise SystemExit
    
    style.use('fivethirtyeight')
    #style.use('dark_background')

    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    ax.xaxis.set_major_locator(mondays)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(weekFormatter)
    #ax.xaxis.set_minor_formatter(dayFormatter)

    #plot_day_summary(ax, quotes, ticksize=3)
    candlestick_ohlc(ax, quotes, width=0.7, colorup='#19caf7', colordown='#6c6c6c')
    ax.xaxis_date()
    ax.autoscale_view()
    ax.yaxis.tick_right()
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.grid(color = '#4c4c4c', linewidth=.25)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(str.upper(stock))

    #manager = plt.get_current_fig_manager()
    #manager.window.state('zoomed') # for auto full screen
    
    #plt.tight_layout()
    fig.set_size_inches(19.5, 10.5, forward=True)
    
    plt.savefig('stock_chart_image.png')
    print('File Saved')
    #plt.show()
    tweet_chart_image()
    print('Stock Chart Tweeted')
