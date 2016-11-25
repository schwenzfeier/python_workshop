#####################################################
### Converting streamed JSON tweets into a CSV file
#####################################################

import json ## Package for parsing JSON into a python dictionary

## Currently the tweets are saved in a .json file, one tweet per line

## Open the JSON file
with open('trump_twets.json') as f:
	lines = f.readlines()

f.close() ## close the file

## Translate our list of lines to JSON
for line in lines:
	try:
		json.load(line)
	except:
		print(line)
		print(type(line))
		break







