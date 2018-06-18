# -*- coding: utf-8 -*-
# ALA Talk generator

# From several data files of programs from ALA Annual Conference
# 2016-18, which have been split into potential beginnings and endings,
# creates a new talk mashup and tweets it.

# I'm making a function called main and calling it at the 
# bottom of the page (this is something you might see a lot). This script
# is designed to run fully on a regular basis, rather than going to sleep on itself.

import random, string
import tweepy
from alacredentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def main():

    infile = open('data/ala_beginners.txt','r')
    bdata = infile.readlines()
    infile.close()

    infile = open('data/ala_enders.txt','r')
    edata = infile.readlines()
    infile.close()

    beginners = [line[:-1] for line in bdata]
    enders = [line[:-1] for line in edata]

    lenb = len(beginners)
    lene = len(enders)

    first= beginners[random.randrange(1, lenb)]
    second = enders[random.randrange(1, lene)]

    line = first + ' ' + second
    print(line)
        
    api.update_status(line)

main()
