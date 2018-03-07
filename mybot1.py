#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Bot 1

# This is the most basic bot. It sends out a tweet!

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
tweet = 'Hello ALA!'

# Send out the tweet and print it to the console 
api.update_status(status=tweet)
print(tweet)

print("All done!")
