import tweepy 

consumer_key = '5cx9dQAsH6kRytnSkKo94lr9s'
consumer_secret = 'GDrNkfkexLcPK63rGccvnzcEMKnjR5bSVKm9v4buMKPy4Y3kXn'
access_token = '3193851775-ymak09P7b0Vz5GxEk6UKy2nuu2QzmpVRvMcFo5f'
access_token_secret = 'EuYeGiPLaEDrpem16prBz6W9x7jtadfkudKKigoP2eRk7'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


public_tweets = api.home_timeline()

for tweet in public_tweets:
	print(tweet.text)
