# Challenge level: Beginner

# Goal: Using the code from Lesson 3: File handling and dictionaries,
# create a function that will open a CSV file and return the result as
# a nested list.


def csv_to_list(the_csv, mode='r'):
    'Returns contents of CSV file as nested list.'
    with open(the_csv,mode) as the_openedcsv:
        the_csvrows = the_openedcsv.read().split('\n')

    for index,csvrow in enumerate(the_csvrows):
        the_csvrows[index] = the_csvrows[index].split(',')
        #print "the_csvrows[index] after splitting on comma:"
        #print the_csvrows[index]
    #print the_csvrows
    return the_csvrows


print csv_to_list('../../repo/section_07_(files)/states.csv')
    
