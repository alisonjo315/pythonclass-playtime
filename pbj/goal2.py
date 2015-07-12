# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make

bread = 9
pb = 5
jam = 7

full_sandwiches = bread / 2

if (full_sandwiches < pb) and (full_sandwiches < jam):
    least_ingr = "bread"
    least_num = full_sandwiches
elif (pb < full_sandwiches) and (pb < jam):
    least_ingr = "pb"
    least_num = pb
else:
    least_ingr = "jam"
    least_num = jam

if (full_sandwiches >= 1) and (pb >= 1) and (jam >= 1):
	print 'There\'s enough bread, peanut butter, and jam to make a sandwich!'
        print 'You can make {0} sandwich(es)!'.format(least_num)	
else:
        print 'There\'s not enough bread and/or PB and/or jam to make a sandwich :('
