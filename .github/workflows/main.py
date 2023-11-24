import os
import tweepy

# Load environment variables
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Ensure all keys are available
if not all([CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
    raise ValueError("One or more required environment variables are missing.")

# Authentication with Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Initialize Tweepy Client
client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Profile update function
def update_profile_info(params):
    api.update_profile(**params)

# Update profile information
profile_info = {
    'name': 'Bot (?)',
    'url': 'https://twitter.com/Bot1631973',
    'location': 'Salvador, Brasil',
    'description': 'Eu ainda não tenho propósito.'
}
update_profile_info(profile_info)

# Function to post a tweet
def post_tweet(text):
    client.create_tweet(text=text)

# Function to upload media and post a tweet
def upload_media(text, filename):
    media = api.media_upload(filename)
    api.update_status(text, media_ids=[media.media_id_string])

# Example usage (uncomment to use)
 post_tweet("Fred é V4D14!")
# upload_media("Hello with media!", "path/to/your/image.jpg")   
