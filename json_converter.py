#####################################################
### Converting streamed JSON tweets into a CSV file
#####################################################

import json ## Package for parsing JSON into a python dictionary
import csv ## Package for writing CSVs

## What you want the resulting CSV file to be called
OUTFILE = 'trump_tweets.csv'

## Currently the tweets are saved in a .json file, one tweet per line
## Open the JSON file and read each tweet into a list
tweets = []
for line in open('trump_tweets.json', 'r'):
    tweets.append(json.loads(line))

## Open the CSV file and get ready to write!
with open(OUTFILE, 'w') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter = ",")

	# Writing a header so our CSV has column labels
	header = ['user_name', 'user_id','tweet_text','tweet_id']
	csvwriter.writerow(header)

	## A JSON object in Python is just like a dictionary
	# Let's say we want to write just the user and tweet content and associated ID numbers
	for t in tweets:
		user_name = t['user']['screen_name']
		user_id = t['user']['id_str']
		tweet_text = t['text']
		tweet_id = t['id_str']

		## Now, let's strip out all of the delimiter characters (commas in this case)
		user_name = user_name.replace(",", "")
		tweet_text = tweet_text.replace(",", "")

		## Writing to CSV
		row = [user_name, user_id, tweet_text, tweet_id]
		row = [item.encode('utf-8') for item in row] ## Encoding in UTF-8 so we can keep special characters
		print(row)
		csvwriter.writerow(row)

csvfile.close()







