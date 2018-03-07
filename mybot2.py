#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Bot 2

# This bot tweets three times, waiting 15 seconds between tweets.

# If you haven't yet created credentials.py, modify credentials.template 
# to include your own Twitter account settings. This script will then tweet
# using your bot's account 

# Housekeeping: do not edit
import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# What the bot will tweet
tweet_list = ['Test tweet one!', 'Test tweet two!', 'Test tweet three!']

# loop through the tweet_list and tweet each item
for line in tweet_list: 
    api.update_status(status=line)
    print(line)
    print('...')
    time.sleep(15) # Sleep for 15 seconds

print("All done!")
