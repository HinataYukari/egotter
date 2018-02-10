import json
from requests_oauthlib import OAuth1Session
from api import *

#APIの投稿専用URL
url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

twitter = OAuth1Session(Consumer_Key, Consumer_Secret, Access_Token, Access_Token_Secret)

#画像枚数(1-4)
pic_count = 4
#画像パス
prefix = "images/glt/ic"
formattype = ".png"
#本文
text = "GirlsLastTour"

#画像投稿　
media_ids = []
for i in range(pic_count):
    # 画像アップ
    files = {"media" : open(prefix + str(i+1) + formattype, 'rb')}
    req_media = twitter.post(url_media, files = files)

    # レスポンスを確認
    if req_media.status_code != 200:
        print ("画像アップデート失敗: %s", req_media.text)
        exit()

    # Media ID を取得
    media_ids.append(json.loads(req_media.text)['media_id'])
    print ("Media ID: %d" % media_ids[i])

# Media ID を付加してテキストを投稿
params = {"status": text, "media_ids": media_ids}
req_media = twitter.post(url_text, params = params)

# 再びレスポンスを確認
if req_media.status_code != 200:
    print ("テキストアップデート失敗: %s", req_text.text)
    exit()

print ("OK")
