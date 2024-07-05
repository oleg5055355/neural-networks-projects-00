import tweepy
import time

consumer_key='znluCfr86FwwzNrI8OgzK49uz'
consumer_secret='sjdDSmYytuwhxm35PreaeJNrHT1YBI3U6e7PR6Zx8v56RzSk8G'
key='1447444563925225473-gQPzvpCBqIrZU7cvrlBeBvW1tDAz2B'
secret='PYteNajjza9VgisOhmGoaDjlYu7EU6piLy5FW6k9Ex15J'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Ok")
except:
    print("Error during exception")

def read_seen(file):
    file_read=open(file,'r')
    last_seen_id=int(file_read.read().strip())
    file_read.close()
    return (last_seen_id)

def store_seen(file,last_seen_id):
    file_write=open(file,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

file='seen.txt'




def reply():
    tweets=api.mentions_timeline(since_id=read_seen(file),tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#hello' in tweet.full_text:
            api.update_status(status="@"+tweet.user.screen_name+"  All the best",in_reply_to_status_id=tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            print("replied-"+str(tweet.id))
            store_seen(file,tweet.id)    
    

while True:
    reply()
    time.sleep(15)
    print("ReLoad.....")

