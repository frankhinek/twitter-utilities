# Get Twitter Followers
Uses the Twitter API to get the list of followers for a given user and
stores the ID, Screen Name, and Name as a row in a time-stamped CSV file.

## Requirements
- Python 3
- python-twitter (3.2.1)
  - `pip install python-twitter`
- Twitter API keys

## Getting Twitter API Keys
- Sign up for a developer account here: https://dev.twitter.com/
- Get your keys here: https://apps.twitter.com/
- Put your keys into the `sample_api_keys.json` file
- Change the name of `sample_api_keys.json` to `api_keys.json`

## Running This Program
- Open up `get_followers.py` and edit the user variable (and save the file)
- Run `python get_followers.py`
- A list of followers will be retrieved
- A new time-stamped CSV file will be created that includes the ID, Screen Name,
and Name of each follower
  - `username-followers-YYYYMMDD-HHMMSS.json` (csv file with follower data)
