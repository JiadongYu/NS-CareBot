import praw
import random
from replied import repliedIds


# Set up reddit ids for the reddit API
client_id = "l7VgXH4PFEUhz4Dqw-LG7A"

secret_key = "d4AzMZNbDt100uUTVWKfYZkTFx72FQ"

# Create a list of words that indicate the poster has poor mental health
trigger_words = ["depression", "anxiety", "suicide", "breakdown", "panic attack",
                 "insomnia", "self-harm", "cannot take it", "drained"]

# Create a string of helpful contacts
helplines = "Do reach out if you need help:\n\n National Care Hotline: 1800-202-6868\n\nSamaritans of Singapore: " \
            "1800-221-4444\n\nInstitute of Mental " \
            "Health’s Mental Health Helpline: 6389-2222 "

# create a list of possible quotes
with open('Quotes.txt', 'r') as file:
    quotes = file.readlines()

# Create a reddit object
reddit = praw.Reddit(client_id=client_id,
                     client_secret=secret_key,
                     username="NS_CareBot",
                     password="Superman333!",
                     user_agent="<console: care_bot: 1.0>")

# Choose a subreddit to access
subreddit = reddit.subreddit("NationalServiceSG")

# Fetch the twenty latest posts and analyse them
for submission in subreddit.new(limit=20):
    for word in trigger_words:
        if word.lower() in submission.selftext.lower():
            # Check if the bot has already replied to that post
            # If yes: pass
            # If no, reply the post and add id to the dictionary in replied.py
            if str(submission.id) not in repliedIds:
                # if not, reply and add the id of the post to replied.py
                random_quote = random.choice(quotes)
                submission.reply(body=random_quote + "\n" + helplines)
                repliedIds[str(submission.id)] = True

