import csv
import sys

# Store the filename arguments passed in from the command line
# The files should be passed in order of oldest to newest
csv_file1 = sys.argv[1] # earlier timestamp
csv_file2 = sys.argv[2] # later timestamp

# Initialize two lists to store the two sets of followers
followers1, followers2 = [], []

# Read in the first CSV file container the first list of followers
with open(csv_file1, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        followers1.append(row['screen_name'])

# Read in the second CSV file container the first list of followers
with open(csv_file2, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        followers2.append(row['screen_name'])

# Store each list as a set
followers1_set = set(followers1)
followers2_set = set(followers2)

# Determine the retained, lost, and new followers
retained_followers = followers1_set.intersection(followers2_set)
lost_followers = followers1_set.difference(followers2_set)
new_followers = followers2_set.difference(followers1_set)

# Print the new followers, if any, and lost followers, if any
if new_followers:
    print('New Followers:')
    print(", ".join(str(follower) for follower in new_followers))
elif lost_followers:
    print('Lost Followers:')
    print(", ".join(str(follower) for follower in lost_followers))
