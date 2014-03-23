# Goal: Create a program that prints out an HTML drop down menu for all 50 states

# Step 1: Define your list of states
# These should all be strings, since they're names of places
# Instead of having to type them all out, I really like liststates.com -- you can even customize the format it gives you the states in to make it super easy to copy/paste into your code here

#states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District Of Columbia','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','PALAU','Pennsylvania','PUERTO RICO','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
#state_abbreviations = ['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PW','PA','PR','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

with open('../repo/section_07_(files)/states.csv','r') as states_file:
    states = states_file.read().split('\n')

# Step 2: Create your loop
# Essentially, you're telling Python: for each state in my list: print this HTML code
# A good place to start is by printing the name of the state in the loop; after that you can add the HTML around it

print '<select>' 

for index,state in enumerate(states):
    states[index] = states[index].split(',')

    print '<option value="{0}">{1}</option>'.format(states[index][0],states[index][1])

print '</select>'



# At line 14, we create the drop-down menu
# At line 15, we create one drop-down item.  Each additional <option> that we add will add another item to our drop-down menu
# At line 16, we tell HTML that we're done with the drop-down menu

# Step 4: Test it!
# Have Python print out the HTML code. Copy / paste it into a file, save that file as "states.html" and open that file in a web browser.
# Later, when we learn file handling, we can skip the copy/paste step.
# File handling can also let us create a file with the state names and abbreviations in it so we don't have to add it to our code.

# Your finished project should look something like: https://github.com/shannonturner/python-lessons/blob/master/section_05_(loops)/states.html
