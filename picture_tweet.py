import json
from requests_oauthlib import OAuth1Session
from api import *

#APIの投稿専用URL
url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

twitter = OAuth1Session(Consumer_Key, Consumer_Secret, Access_Token, Access_Token_Secret)

#本文
text = input("本文を入力:")

#画像枚数(0-4)
pic_count = 1
#画像パス
prefix = "images/xxx"
formattype = ".png"
#画像投稿　
media_ids = ""
if pic_count > 2:
    for i in range(pic_count):
        # 画像アップ
        files = {"media" : open(prefix + str(i+1) + formattype, 'rb')}
        req_media = twitter.post(url_media, files = files)

        # レスポンスを確認
        if req_media.status_code != 200:
            print ("picture update failed: %s", req_media.text)
            exit()

        # Media ID を取得
        media_id = json.loads(req_media.text)['media_id']
        media_id_string = json.loads(req_media.text)['media_id_string']
        print ("Media ID: {} ".format(media_id))
        # メディアIDの文字列をカンマ","で結合
        if media_ids == "":
            media_ids += media_id_string
        else:
            media_ids = media_ids + "," + media_id_string
else:
    files = {"media" : open(prefix + formattype, 'rb')}
    req_media = twitter.post(url_media, files = files)
    # レスポンスを確認
    if req_media.status_code != 200:
        print ("picture update failed: %s", req_media.text)
        exit()
    # Media ID を取得
    media_id = json.loads(req_media.text)['media_id']
    media_id_string = json.loads(req_media.text)['media_id_string']
    print ("Media ID: {} ".format(media_id))
    media_ids += media_id_string

# Media ID を付加してテキストを投稿
params = {"status": text, "media_ids": [media_ids]}
req_media = twitter.post(url_text, params = params)

# 再びレスポンスを確認
if req_media.status_code != 200:
    print ("text update failed: %s", req_text.text)
    exit()

print ("Succeded")
