#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Responding Bot

# This bot listens to the account @ocertat, and when that account
# tweets, it responds with a line of Twain

# Download a Project Gutenberg "Plain Text UTF-8" file,
# open it in Notepad, remove junk at beginning,
# and replace all double-linebreaks with single linebreaks.


# Housekeeping: do not edit
import tweepy
import time
from credentials import *
from random import randint
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# initially, the script will assume that the last tweet was a null value
last_tweet = None

# What the bot will tweet
filename = open('twain.txt', 'r')
tweet_text = filename.readlines()
filename.close()


# a function that picks a random line
def line_number():
    return randint(0, len(tweet_text))


# this is the function that does most of the work of the bot
def compare_tweets():

    # uses the global lasttweet variable, rather than the local one.
    # (it's probably best practice not to use a global variable for
    # this purpose, but we've shown this approach for its readability.
    # We'll also show an alternate way to accomplish this without
    # using a global variable).
    global last_tweet

    # gets the most recent tweet by @ocertat and prints its id
    most_recent_tweet = api.user_timeline('ocertat')[0]
    print(most_recent_tweet.id)

    # compares the two tweets, and tweets a line of Twain
    # if there is a new tweet from @ocertat
    if most_recent_tweet != last_tweet:
        line = tweet_text[line_number()]
        api.update_status(status=line)
        print(line)

    # updates lasttweet to the most recent tweet
    last_tweet = most_recent_tweet

# runs the compare_tweets function every 5 seconds
while True:
    compare_tweets()
    print("sleeping")
    time.sleep(5)  # Sleep for 5 seconds


# To quit early: CTRL+C and wait a few seconds
