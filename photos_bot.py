from twitter import *
import glob
import time

token = ""
token_secret = ""
consumer_key = ""
consumer_secret = ""

LIMIT = 10
SLEEP = 144


t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

# Send images along with your tweets:
# - first just read images from the web or from files the regular way:
images = []
for img in glob.glob("imgs/*.jpeg"):
    with open(img, "rb") as imagefile:
        imagedata = imagefile.read()
        # - then upload medias one by one on Twitter's dedicated server
        #   and collect each one's id:
        t_upload = Twitter(domain='upload.twitter.com',
            auth=OAuth(token, token_secret, consumer_key, consumer_secret))
        id_img = t_upload.media.upload(media=imagedata)["media_id_string"]
        images.append(id_img)

for i in range(LIMIT):
    index = i + 1
    template = f"""Este es un tweet multi linea

La segunda línea esta vacía

En la quinta hay una var {index}."""
    print(i)
    t.statuses.update(status=template, media_ids=",".join([images[i % len(images)]]))
    time.sleep(SLEEP)
