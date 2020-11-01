import tweepy
import os # operating system library
from datetime import date 
born=date(2000, 10, 11)
def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - 
         ((today.month, today.day) < 
         (birthDate.month, birthDate.day)) 
  
    return age
old=calculateAge(born)
def create_api():
  consumer_key = os.getenv('consumer_key')
  consumer_secret = os.getenv('consumer_secret')
  access_token = os.getenv('access_token')
  access_token_secret = os.getenv('access_token_secret')
  
   
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

  uf_split = [int(i) for i in str(old)]# Used to seperate 

  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()]) 
  return emoji_followers 

api = create_api() 

while True:
    user = api.get_user('_BaffledCoder')
    api.update_profile(name=f'Shubham Sharma|{old}')
    print(f'Updating Twitter Name : Shubham Sharma|{old}')
    print('Waiting to refresh')
    time.sleep(60)
