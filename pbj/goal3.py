bread = 9
pb = 5
jam = 7

full_sandwiches = bread / 2

#print 'Based on how much bread I have, I can make {0} sandwiches.'.format(full_sandwiches)

if ((bread % 2) == 1):
    print 'Based on how much bread I have, I can make {0} full sandwiches and 1 open-faced sandwich -- or I can just make {1} open-faced sandwiches.'.format(full_sandwiches, bread)
    #print 'I will make {0} open-faced sandwiches.'.format(bread)
