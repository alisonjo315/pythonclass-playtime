# Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich.

bread = 9
pb = 5
jam = 7

if (bread >= 2) and (pb >= 1) and (jam >= 1):
	print 'There\'s enough bread, peanut butter, and jam to make a sandwich!'

#sandwiches_bread = bread / 2

#print 'Based on how much bread I have, I can make {numsw} sandwiches.'.format(numsw=sandwiches_bread)

if ((bread % 2) == 1):
        print 'I will make {numsw} open-faced sandwiches.'.format(numsw=bread)
