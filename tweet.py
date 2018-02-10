from requests_oauthlib import OAuth1Session
import * from api

#APIの投稿専用URL
url = "https://api.twitter.com/1.1/statuses/update.json"

params  = {
    "status":"Hello, Twitter!"
}

twitter = OAuth1Session(Consumer_Key, Consumer_Secret, Access_Token, Access_Token_Secret)
req = twitter.post(url, params = params)

if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
