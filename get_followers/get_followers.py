import twitter
import json
import csv
import time

# CHANGE THIS TO THE USER YOU WANT TO GET FOLLOWERS FOR
user = 'frankhinek'

# Open the API keys file and read in the keys and secrets
with open('api_keys.json') as f:
    keys = json.load(f)

# Set the Twitter API keys and secrets to use
api = twitter.Api(consumer_key=keys['consumer_key'],
                  consumer_secret=keys['consumer_secret'],
                  access_token_key=keys['access_token_key'],
                  access_token_secret=keys['access_token_secret'])

# Get the current date and time to user in the CSV filename
timestr = time.strftime('%Y%m%d-%H%M%S')

# Specify the name of the CSV file and include a date/time stamp so that each
# program run results in a unique CSV file.  This can later be used to compare
# for new or lost followers.
csv_filename = user + '-followers-' + timestr + '.csv'

# Get list of all followers
followers = api.GetFollowers(screen_name=user)

# OPTIONAL Print list of followers by Screen Name
#print([f.screen_name for f in followers])

# Open a new CSV file for writing and insert every follower as a row
with open(csv_filename, 'w') as csvfile:

    # Define the columns to be used in the CSV file
    fieldnames = ['id', 'screen_name', 'name']

    # Initialize the CSV dictionary writer with the field names defined earlier
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the fiel dnames as a header row in the CSV file
    writer.writeheader()

    # Loop through the list of followers and write the Twitter ID, Screen Name,
    # and Name as a new row
    for follower in followers:
        writer.writerow({'id': follower.id, 'screen_name': follower.screen_name, 'name': follower.name})

# Print the number of followers back to the individual that executed the program
print("You have " + str(len(followers)) + " followers")
