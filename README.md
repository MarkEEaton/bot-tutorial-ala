# Twitter bot tutorial: ALA 2018 edition

This tutorial and its materials are put together by Robin Davis (@robincamille) and Mark Eaton (github.com/MarkEEaton) for the [Python for Beginners: A Gentle and Fun Introduction](https://www.eventscribe.com/2018/ALA-Annual/fsPopup.asp?Mode=presInfo&PresentationID=379935) LITA pre-conference workshop at [ALA 2018](https://2018.alaannual.org/). 

See also: Davis, Robin, and Mark Eaton. [Make a Twitter Bot in Python: Iterative Code Examples](http://jitp.commons.gc.cuny.edu/make-a-twitter-bot-in-python-iterative-code-examples/). *Journal of Interactive Technology and Pedagogy* (Blueprints section).  April 2016. (Verbose write-up featuring [code from a previous version](https://github.com/robincamille/bot-tutorial) of this workshop.)

---

See original repo: https://github.com/robincamille/bot-tutorial

Written in Python 3.

**Required libraries:** tweepy 3.5, requests, time, os, random, csv

---

## Create an account on PythonAnywhere

If you're participating in this in-person workshop:

1. Go to https://pythonanywhere.com and create an account by clicking on `Start running Python online in less than a minute`
 - Select `Create a beginner account` and fill out your details
 - Select `Account` on the top right
 - Select `Teacher` and enter `b7jl` so that we can add the sample code to your account

Bots left running on PythonAnywhere will keep running for a day or so (if the script you're using, like `mybot2.py`, is programmed to keep iterating through tweets) even if you close PythonAnywhere.

Not part of the in-person workshop? Download these files to your local machine or use this command: `git clone https://github.com/MarkEEaton/bot-tutorial-ala.git`

## Create a Twitter account for your bot

1. Go to http://twitter.com and sign up for a new account of your choosing
 - Be sure to include your mobile number (required for using the API) 
 - Email address must be unique to Twitter users; try adding random periods in your Gmail address, if you have one

2. Go to http://apps.twitter.com and create a new app
 - This info isn't public so it can be messy 
 - Go to `Keys and Access Tokens`
 - `Create my access token`

3. Copy Consumer Key/Secret and Access Key/Secret to **credentials.template** and save as a new file named **credentials.py**

4. (Optional) Follow @litabots, which will follow & retweet bots made in this workshop

## Basic bot: mybot1.py

This isn't really a bot yet, but it is a script that sends out one tweet using the Twitter API. Our code is tweeting!

1. Go to the bot-tutorial-ala folder. Click on `mybot1.py` to see the code
2. Clicking `Run` will run the bot. A console (output area) will appear at the bottom of the screen

## Basic bot: mybot2.py

This script is a basic Twitter bot. It will tweet three things from a **list** inside the script.

1. Go to the bot-tutorial-ala folder. Click on `mybot2.py` to see the code

2. Take a look at the script; Robin and Mark will talk about what it's doing

3. `Run` the bot!

*Change it up!*
- In `tweetlist`, add new things for your bot to tweet
- Increase/decrease time between tweets in `time.sleep(15)` (15 is the number of seconds) 

## Intermediate bot: mybot3.py

This script sends out five tweets from the first five lines of an external .txt file

1. Go to the bot-tutorial-ala folder. Click on `mybot3.py`

2. Also look at `twain.txt` to see the text

3. Take a look at both files; Robin and Mark will talk about what the script is doing

4. Select `Run`

*Change it up!*
 - Go to http://gutenberg.org and choose a different text for your bot to tweet. Pick the "Plain Text UTF-8" option when selecting a text format.
   - On PythonAnywhere, you can select `New Empty File`. This will only work if you've entered a filename. Copy and paste your gutenberg.org text (or any text of your choosing) into this blank file
   - Remove junk at the beginning (and the end) of the file. Save the file
   - Replace double linebreaks with single linebreaks. If your file is very short you can maybe do this manually.
   - For longer files you can click on `Open bash console here` and type: `cd bot-tutorial-ala` then `grep . filename > newfilename`. Open up the new file to make sure that it worked.
   - In mybot3.py, replace `twain.txt` with the `newfilename` 
 - Make the bot send more or fewer tweets, or change which lines, by editing the numbers in `for line in tweettext[0:5]`. 
   - `[0:5]` means from the first thing up to (but not including) the fifth thing

## Intermediate bot: mybot4.py

This script sends out tweets based on randomly selected titles (and their descriptions) from a CSV file

1. Go to the bot-tutorial-ala folder. Click on `mybot4.py`

2. Also take a look at `az_database_list.csv` to see the data file. This file is a list of electronic products at Kingsborough Community College. It was exported from LibGuides. Before sharing this, we removed a couple of columns that had internal library data. CSV, or comma separated values, is a great data format to work on in both Python and in Excel. 
 
3. Take a look at both files; Robin and Mark will talk about what the script is doing

4. Try running it!

## Advanced bot: advanced_plumpoem.py

This script treats the poem *This Is Just To Say* (William Carlos Williams) as a mad-lib, filling in four blanks from four data sources: JSON files from @dariusk's [collection of corpora](https://github.com/dariusk/corpora). 

*Change it up!*
- Choose different [word lists](https://github.com/dariusk/corpora). Make sure to change the URLs in lines ``16-19`` and the list name in lines ``22-25``.
- Choose a different piece of text to make into a mad lib. 


## Advanced bot: advanced_listeningbot.py

This script tweets a random line from a `.txt` file whenever @ocertat (Mark) tweets.

*Change it up!*
- Change what the bot tweets whenever it "hears" a new tweet from @ocertat.
- Change who the bot listens to from @ocertat to someone else. (Please don't make a spam bot!)


## Advanced bot: advanced\_mashup_markov/

This script (`advanced_mashup_markov/markovmaker.py`) uses a Markov chain to create a new file full of nonsense sentences from another text. `twain.txt` is included as the default source text.

This script doesn't tweet, it just makes a new text file. Point `mybot3.py` to the new `.txt` file you created to tweet out lines. (Note that the new filename is `advanced_mashup_markov/twain_markov.txt` or the filename of your choosing.)

*Change it up!*
- Download or create a new `.txt` file that `markovmaker.py` will use to generate nonsensical text. Library conference abstracts, perhaps? 

## Advanced bot: advanced_ala-talk-generator.py

This bot mixes up talk titles from ALA Annual Conferences 2016, 2017, and 2018. The mash-up titles are composed of two halves, each from a real ALA program talk.

The script chooses a random beginning and ending from `data/ala_beginners.txt` and `data/ala_enders.txt` each time it tweets. (These data files have been pre-prepared and cleaned; talk titles were split in half at `:`, `?`, `at`, `of`, `for`, `on`, and `and`, sometimes generating multiple beginning and ending halves.) 

*Change it up!*
- Create a new data file, `enders.txt`, and populate it with new language data, like song titles. Each potential title ender should be on its own line in the `.txt` file.

