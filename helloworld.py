## Basic intro to Python

print "Hello world!"


## Data types
s = 'Hark upon the gale'
i = 100
i2 = 3
f = 3.0
f2 = 2.5783940
l = ['meg', 24, 'Virginia']

## You can format strings like so:
print "This is a string: {0}".format(s)
print '\n\n'
print "These are integers: {0}, {1}".format(i, i2)
print '\n\n'
print "These are floating point numbers: {0}, {1}".format(f, f2)
print '\n\n'
print "This is a list: {0}".format(l)
print '\n\n'

print "You can multiply strings like this:"
print s*3
print '\n\n'

print "An integer * an integer is an integer: {0}"
print i * i2
print '\n\n'

print "An integer * a rounded float is a float:"
print f * f2
print '\n\n'

## You can interact with Python too
name = raw_input("What is your name? Enter name: ")
print "Hello {0}, nice to meet you.".format(name)

food = raw_input('What is your favorite food? ')
print "{0} is delicious!".format(food)


##################################
######### CONDITIONALS ###########
##################################
## You can also do conditionals (if else statements)
## Here is a surly bartending robot

age = raw_input('What is your age? ')
age = int(age) ## Convert age from the input string to an integer
drink = raw_input('What is your favorite drink? ')

bad_drinks = ['tequila', 'pepsi', 'cider'] ## This robot really hates tequila, pepsi, and cider

if age < 18:
	print "Are you in high school?"

if age < 21: 
	print "Get out of my bar. No {0} for you.".format(drink)

elif age == 21: ## If age is exactly 21
	print "You look barely 21. Can I see your ID?"

## If here evaluates for everyone, even the 21 year old above
if age >= 21: 
	print "I guess you can stay in my bar..."

	if drink in bad_drinks:
		print "Sorry I don't serve {0} here".format(drink)
	else:
		print "Here's a {0}".format(drink)

## If evaluates for everyone
if age > 35:
	print "Isn't it past your bedtime?"


#########################
## Dictionary
#########################
## dictionaries in Python have keys that correspond to information, just like an actual dictionary
## they can have multiple levels and different types of data in them

directory = {
	'Schwenzfeier': {'last_name': 'Schwenzfeier',
		'first_name': 'Meg',
		'age': 24,
		'city': 'Brooklyn',
		'state': 'NY',
		'favorite_foods': ['pizza','watermelon','jello']
		},
	'Settle': {'last_name': 'Settle',
	    'first_name': 'Jaime',
	    'age': 31,
	    'city': 'Williamsburg',
	    'state': 'VA',
	    'favorite_foods': ['frozen waffles']}

}

## Here are the keys
print directory.keys()

## You can look up info
print directory['Schwenzfeier']['age']
print directory['Settle']['favorite_foods']



