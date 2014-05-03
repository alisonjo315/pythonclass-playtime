# Challenge level: Beginner

# Scenario: You have two files containing a list of email addresses of people who attended your events.
#       File 1: People who attended your Film Screening event
#       ../../repo/section_09_(functions)/film_screening_attendees.txt
#
#       File 2: People who attended your Happy hour
#       ../../repo/section_09_(functions)/happy_hour_attendees.txt
#

# Note: You should create functions to accomplish your goals.

#Function to open/read a text file!
def textfile_stringify(filename):
    'Returns contents of text file as string.'
    with open(filename, 'r') as text_file:
        text = text_file.read()
    return text

# Goal 1: You want to get a de-duplicated list of all of the people who have come to your events.

#Function to create a list from a string!
def string_listify(the_string, delimiter=','):
    'Splits a string into a list, and returns the list.'
    the_list = the_string.split(delimiter)
    return the_list

#Function to combine two lists!
def twolists_listify(list1,list2):
    'Returns a list with list2 items appended to list1.'
    return list1+list2

#Function to deduplicate!
def list_deduplicafy(the_list):
    'Creates a list from a set created from a list.\nIn other words, returns the list back with only unique list items.'
    return list(set(the_list))

#Introducing, the attendee text files.
film_attendees_file = '../../repo/section_09_(functions)/film_screening_attendees.txt'
hh_attendees_file = '../../repo/section_09_(functions)/happy_hour_attendees.txt'

#Make a string of each attendees file.
#nah, all at once! see further down...
#film_attendees_str = textfile_stringify(film_attendees_file)
#hh_attendees_str = textfile_stringify(hh_attendees_file)

#Make a list of each attendees string.
#nah, all at once! see further down...
#film_attendees_ls = string_listify(film_attendees_str,'\n')
#hh_attendees_ls = string_listify(hh_attendees_str,'\n')

#Make lists of each event's attendees "all at once"
film_attendees = string_listify(textfile_stringify(film_attendees_file),'\n')
hh_attendees = string_listify(textfile_stringify(hh_attendees_file),'\n')

#Combine the two attendees lists into one.
#aggregated_attendees = twolists_listify(film_attendees_ls,hh_attendees_ls)
aggregated_attendees = twolists_listify(film_attendees,hh_attendees)
#print len(aggregated_attendees) #24

#Deduplicate the combined list.
unique_attendees = list_deduplicafy(aggregated_attendees)
#print len(unique_attendees) #19

print 'Unique attendees: ({1})\n{0}\n'.format('\n'.join(unique_attendees),len(unique_attendees))

# Goal 2: Who came to *both* your Film Screening and your Happy hour?

#Function to find who's in both lists!
def match_findify(list1,list2):
    'Returns a list of items found in both lists.'
    #https://docs.python.org/2/library/stdtypes.html#set.intersection
    return list(set.intersection(set(list1), set(list2)))
    #Note: Alternatively, could loop through one list and test like,
    #if __item__ in __other-list__: add to in_both list.

#Make a list of people who are in both lists.
in_both = match_findify(film_attendees,hh_attendees)
#print len(in_both) #5 -- matches 24-19, which is nice
print 'Matching attendees: ({1})\n{0}'.format('\n'.join(in_both),len(in_both))
