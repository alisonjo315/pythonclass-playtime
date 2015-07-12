# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches

bread = 9
pb = 0
jam = 7

full_sandwiches = bread / 2

if (full_sandwiches >= 1) and (pb >= 1) and (jam >= 1):
    print 'There\'s enough bread, peanut butter, and jam to make a sandwich!'
else:
    print 'There\'s not enough bread and/or PB and/or jam to make a sandwich :('
    if full_sandwiches < 1:
        print 'You don\'t have enough bread to make a whole PBJ.'

    if pb < 1:
        print 'You don\'t have enough PB to make a whole PBJ.'

    if jam < 1:
        print 'You don\'t have enough jam to make a whole PBJ.'
