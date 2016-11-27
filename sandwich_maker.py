## Example sandwich maker script
## Adapted from: https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson01_pbj.py

## Inputs
bread = raw_input('How many slices of bread do you have? ')
pb = raw_input('How many servings of peanut butter do you have? ')
jelly = raw_input('How many servings of jelly do you have? ')

## Raw inputs are always strings! Need to convert to numbers
bread = int(bread)
pb = int(pb)
jelly = int(jelly)


## Test to see if we can make a sandwich?
if bread >= 2 and pb >= 1 and jelly >= 1:
	print('Yes, you can make a sandwich.')
else:
	print('Bummer, you cannot make a sandwich')

## BONUS: Test to see how many sandwiches we can make 
sandwiches_worth_of_bread = bread // 2  ## The // operator is integer division: how many times 2 goes into our # of slices evenly
max_num_sandwiches = min(sandwiches_worth_of_bread, pb, jelly) ## You can make as many sandwiches as the ingredient you have the least of! 

if max_num_sandwiches > 0:
	print('You can make {0} sandwiches.').format(max_num_sandwiches)

