## Twitter API streaming 

## Meg Schwenzfeier - mjschwenzfeier@gmail.com, 11/25/16

## Purpose: Streams data from Twitter's API

## Importing the modules we need
## NOTE: If you get "ImportError: No module named twython" you need to install the twython module
from twython import TwythonStreamer
import json
import sys

## Here we create a class called TwitterStreamer that takes the API keys from your Twitter account
class TwitterStreamer(TwythonStreamer):
        def __init__(self, appkey, appsecret, oathtoken, oathsecret, file_n):
                TwythonStreamer.__init__(self, appkey, appsecret, oathtoken, oathsecret)
                self.file_n = file_n

        def on_success(self, data):
                f = open(self.file_n, 'a')
                print(data['text'])
                f.writelines(str(data) + "\n")
                
        def on_error(self, status_code, data):
                print status_code

# These should be filled in using the API keys from your application at apps.twitter.com
APP_KEY = ''
APP_SECRET = ''
OATH_TOKEN = ''
OATH_TOKEN_SECRET = ''


## Here's how we run it from the command line!
## From the command line type: python twitterstream.py filter OR sample filter_words
## Example to stream a random sample of all tweets:
##      python twitterstream.py sample
## To stream all tweets that have william AND mary in them:
##      python twitterstream.py sample 'william mary'
## To stream all tweets that have 'willia' OR 'mary' in them:
##      python twitterstream.py sample 'william, mary'


if __name__ == '__main__':
        
        ## These are the arguments you passed through the command line
        args = len(sys.argv)

        ## Throw an error if you passed in an incorrect number of arguments
        if args != 3 and args != 4:
                print '\n\n\nERROR'
                print 'Usage: python twitterstream.py [file_name.json] [sample OR filter] [filter_words]'
                print "If you're having issues, email Meg (mjschwenzfeier@gmail.com)\n\n\n"
        
        ## If you put in the correct number of arguments
        else:
                file_name = sys.argv[1] ## File name is the first argument

                ## Initialize the tweet streamer
                stream = TwitterStreamer(appkey=APP_KEY, appsecret=APP_SECRET, oathtoken=OATH_TOKEN, oathsecret=OATH_TOKEN_SECRET, file_n=file_name)
                

                ## If you're filtering:
                if sys.argv[2] == 'filter':
                        ## Print that you're filtering
                        print "\n\nStreaming tweets with {0}... Hit Ctrl-c to stop.".format(filter_words)
                        
                        ## Loop endlessly, unless you hit an error, then print the error and stop
                        while True:
                                filter_words = sys.argv[3] ## The search words we passed in
                                
                                ## Try to do this
                                try:
                                       stream.statuses.filter(track=filter_words)
                                
                                ## Except when you hit an error, then do this
                                except: 
                                        e = sys.exc_info()[0] ## Assign the error to "e"
                                        if e == KeyboardInterrupt: ## If the user hits Control-C, break (stop the program)
                                                break
                                        print "Error: " + str(e) ## Print the error

                ## If you're sampling:
                elif sys.argv[2] == 'sample':
                        ## Print that your sampling
                        print "\n\nSampling all tweets... Hit Ctrl-c to stop."
                        
                        ## Loop endlessly, unless you hit an error, then print the error and stop
                        while True:

                                ## Try to do this
                                try:
                                        stream.statuses.sample()

                                ## Except when you hit an error, then do this
                                except:
                                        e = sys.exc_info()[0] ## Assign the error to "e"
                                        if e == KeyboardInterrupt: ## If the user hits Control-C, break (stop the program)
                                                break       
                                        print "Error: " + str(e) ## Print the error
                
                ## If you try to do anything else, it'll throw an error
                else:
                        print '\n\n\nERROR'
                        print "Select either 'sample' or 'filter' for your Twitter stream."
                        print "Usage: python twitterstream.py [file_name.json] [sample OR filter] [filter_words]"
                        
