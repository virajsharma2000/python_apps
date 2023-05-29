import requests
import datetime

topic = input('Enter your news topic: ')

date = datetime.datetime.now().strftime('%Y-%B-%d')

r = requests.get('https://newsapi.org/v2/everything?q={}&from={}&apiKey=13ca860d6e8d43c583d7813692176071'.format(date,topic))

data = r.json()['articles'][0]

headline = data['title']
description = data['description']

print('\n\n')


print("today's date - {}".format(date))

print('\n\n')

print('headline - {}\n\ndescription - {}'.format(headline,description))
