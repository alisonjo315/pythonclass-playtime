# Difficulty Level: Beginner
# Exercise: Tweet length calculator

# Part one:
# Create a variable called tweet and put some text in it
#   maybe something like "Learning to code was so much fun today! #python #sssssss"
print "PART ONE"

# comment out each of these three to test under/over the 140 and 280 limits.
tweet = "Learning to code was so much fun today! #python #sssssss"
#tweet = "Learning to code was so much fun today! #python #sssssss Lorem ipsum dolor sit amet, consectetur adipiscing elit. Primum non saepe, deinde quae est ista relaxatio."
#tweet = "Learning to code was so much fun today! #python #sssssss Lorem ipsum dolor sit amet, consectetur adipiscing elit. Primum non saepe, deinde quae est ista relaxatio, cum et praeteriti doloris memoria recens est et futuri atque inpendentis torquet timor? At quicum ioca seria, ut dicitur."
print tweet

# Measure the length of that tweet.
tweet_length = len(tweet)
print tweet_length

# Was that tweet more than 140 characters?
#   If so, tell the user it was too long!
# Was that tweet 140 or fewer characters?
#   If so, tell the user how witty they are!
if tweet_length > 140:
    print "\nYour tweet is too long! #SAD! Max length is 140 characters."
else:
    print "\nNice work with the not-too-long tweet! #winning #nofilter #blessed"


# Part two:
# Adjust the program to say how many characters you have remaining to use, or how many you need to trim by in order to meet the 140 character limit
print "\nPART TWO"
if tweet_length > 140:
    print "Your tweet is too long! #SAD! Max length is 140 characters. You need to trim {0} to post your tweet.".format(tweet_length-140)
else:
    print "Nice work with the not-too-long tweet! You may add up to {0} more characters, but why mess with a good thing? #winning #nofilter #blessed".format(140 - tweet_length)


# Part three:
# Twitter announced they are changing their character limit to 280, but they might change it again.
# Can you make your code flexible enough so that you don't have to replace the character limit in multiple places in your code?
print "\nPART THREE"
max_length = 280 # Modify the character limit just once, right here.
if tweet_length > max_length:
    print "Your tweet is too long! #SAD! Max length is {0} characters. You need to trim {1} to post your tweet.".format(max_length, tweet_length - max_length)
else:
    print "Nice work with the not-too-long tweet! You may add up to {0} more characters, but why mess with a good thing? #winning #nofilter #blessed".format(max_length - tweet_length)

