#!/home/staeiou/miniconda3/envs/py3k/bin/python

import textwrap
import tweepy
import twitter_login

with open('vol1.txt') as f:
    txt = f.read()

# Get rid of newlines and "... (" -- this comes into play later

txt_c = txt.replace('\n','')
txt_c = txt_c.replace("... (", "...(")


# Wrap to 105 characters

wrapped = textwrap.fill(txt_c, 105)

# Generate dictionary of tweets based on text

count = 1
split = wrapped.split('\n')
num_tweets = len(split)
tweetdict = {}
for line in split:
    tweet = "@marx_storm ..."
    line = tweet + line + "... (" + str(count) + "/" + str(num_tweets) + ")"
    tweetdict[count] = line
        
    count += 1

# The twitter authentication part

CONSUMER_KEY = twitter_login.CONSUMER_KEY
CONSUMER_SECRET = twitter_login.CONSUMER_SECRET
ACCESS_TOKEN = twitter_login.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = twitter_login.ACCESS_TOKEN_SECRET

# Authenticate

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# Get our last tweet

acct_id = 808407727345123329
last_tweet = api.user_timeline(id = acct_id, count = 1)[0]


# Look for the number in the last tweet

start = last_tweet.text.find("... (") + 5

end = last_tweet.text[start:].find("/") + start
tweet_num = int(last_tweet.text[start:end]) + 1


# And update the status

api.update_status(status=tweetdict[tweet_num], in_reply_to_status_id=last_tweet.id_str)
