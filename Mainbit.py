import tweepy
import os # operating system library

def create_api():
  consumer_key = 'anstrhmbNUSYs0CkBaX6V38XO'
  consumer_secret = 'yyR7Mh6HbVtAXUx98ow1waxNsfX9jgr8aGAC8HpkjGLFYVm8kk'
  access_token = '1272434796241793025-r6ziaox30d3DJRjFM9MRRqrfTQyGjN'
  access_token_secret = 'FjV8XPCx7vsVrzRvvuYxpxnO4EhRG72k8IAcZi6aOUYue'

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  print('API Created')
  return api
  
# Complete code
import time

def follower_count(user):
  emoji_numbers =  {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                      4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}

  uf_split = [int(i) for i in str(user.followers_count)]# Used to seperate 

  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()]) 
  return emoji_followers

api = create_api()

while True:
    user = api.get_user('_BaffledCoder') #Twitter username
    api.update_profile(name=f'Shubham Sharma|{follower_count(user)} Followers')
    print(f'Updating Twitter Name : Shubham Sharma|{follower_count(user)} Followers')
    print('Waiting to refresh')
    time.sleep(60)
