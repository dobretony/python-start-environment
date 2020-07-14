# Racial bias detection in a sub reddit

This project aims to determine the racial bias in a Reddit subreddit that is filled with selfies and face pics,
by determining the skin color of people represented in the selfies and creating a data structure that takes into
account upvotes and number of comments.

At the moment it can only detect white skin tones, and the detected number out of 1000 selfies of white skin toned characters
is 784.

It uses PRAW in order to connect with the Reddit API, where it gathers the following data from top submissions of the /r/gaybrosgonemild
subreddit:

```bash
author # the author of the post
skinColor # 1 for white and 0 for non-white ( at least in it's current state )
score # number of current upvotes
upvote_ratio # the percentage of upvotes from the total upvotes/downvotes
comments # the number of top level comments
created # the date the submission was created in "%Y-%m-%d %H:%M:%S" format
created_utc # the date the submission was created in UTC format
```

In order to determine if a picture contains a certain skin tone, it will first detect a face through the OpenCV library dataset in [haarcascade_frontalface_default.xml](haarcascade_frontalface_default.xml).

Once a face has been detected, it takes the image of just the face and applies a skin color mask determined by HSV colors in order to detect
white skin tone.

If any white skin tone has been detected, it will mark it down into a CSV file with the data mentioned above.

## Next steps

Implement skin tone detection algorithm: https://arxiv.org/ftp/arxiv/papers/1708/1708.02694.pdf

## How to install

First off, you should start with [installing python3 on your machine](https://realpython.com/installing-python/). With Python3 installed the package virtualenv should already be available.

In order to start the project:

```bash
virtualenv -p python3 venv #creates environment venv inside working directory
source venv/bin/activate #activates venv environment
```

To deactivate the project:

```bash
deactivate
```

When first activating the virtual environment, run:

```bash
make init
```

Make sure to have a praw.ini file that resembles the following structure, in order to connect to REDDIT API.

```ini
[DEFAULT]
# A boolean to indicate whether or not to check for package updates.
check_for_updates=True

# Object to kind mappings
comment_kind=t1
message_kind=t4
redditor_kind=t2
submission_kind=t3
subreddit_kind=t5
trophy_kind=t6

# The URL prefix for OAuth-related requests.
oauth_url=https://oauth.reddit.com

# The amount of seconds to ratelimit
ratelimit_seconds=5

# The URL prefix for regular requests.
reddit_url=https://www.reddit.com

# The URL prefix for short URLs.
short_url=https://redd.it

# The timeout for requests to Reddit in number of seconds
timeout=16

[bot1]
client_id=######################
client_secret=######################
bot_name=RacialBiasGayBrosGoneMild
bot_version=0.9
bot_author=######
user_agent=script:%(bot_name)s:v%(bot_version)s (by /u/%(bot_author)s)
```

How to run:

```bash
make run
```

## Project structure


```bash
README.md # This file.
LICENSE # MIT License
setup.py # Sets up path variables.
requirements.txt # Contains lists of packages for Python
app/__init__.py # initial app entry point
docs/conf.py # configuration for PyDoc
docs/index.md # index file for documentation
tests/test_basic.py # basic tests script
tests/test_advanced.py # advanced tests script
```
