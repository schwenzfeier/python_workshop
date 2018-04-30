#####################################################
### Converting streamed JSON tweets into a CSV file
#####################################################

import json ## Package for parsing JSON into a python dictionary
import csv ## Package for writing CSVs

## What you want the resulting CSV file to be called
INFILE = 'trump_tweets.json'
OUTFILE = 'trump_tweets2.csv'

## Currently the tweets are saved in a .json file, one tweet per line
## We want to open the JSON file and read a tweet, process it, and write it out
## one at a time

## First, open the CSV file
with open(OUTFILE, 'w') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter = ",")

	# Writing a header so our CSV has column labels
	# Note that we only want to do this once, not for every tweet, so it's
	# up here outside of where we loop through tweets
	header = ['user_name', 'user_id','tweet_text','tweet_id']
	csvwriter.writerow(header)

	## Now let's open the JSON file and read, process, and write the tweets
	# one at a time

	for line in open(INFILE, 'r'):
		t = json.loads(line)
		user_name = t['user']['screen_name']
		user_id = t['user']['id_str']
		tweet_text = t['text']
		tweet_id = t['id_str']

		## Now, let's strip out all of the delimiter characters (commas in this case)
		usr_name = user_name.replace(",", "") 
		tweet_text = tweet_text.replace(",", "")

		## Writing to CSV
		row = [user_name, user_id, tweet_text, tweet_id]
		row = [item.encode('utf-8') for item in row] ## Encoding in UTF-8 so we can keep special characters
		print(row)
		csvwriter.writerow(row)


csvfile.close()
