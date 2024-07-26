from _datetime import date
import json

import jsonpickle
import redis
import requests

from news.news_redis import News
from news.gpt import GPT
import string
import traceback

def is_yes(text):
    if "Yes," in text:
        return True
    else:
        return False

def remove_yes_or_no(text):
    text = text.replace("No, ", "")
    text = text.replace("Yes, ", "")
    text = string.capwords(text)
    return text
    
r = requests.get("http://localhost:8080/examples/news.txt")

new_str = str(r.text)
new_str = new_str.replace("b'", "")
new_str = new_str.replace("\r\n", "")

jsonObject = json.loads(new_str)

results = jsonObject["results"]
news_src_list=[]
for object in results:
    try:
        # print ("pubDate-->", object['pubDate'] )  
        # print ("title-->", object['title'])
        # print ("link-->", object['link'])
        # print ("image_url-->", object['image_url'])   
        newsObject = News()
        newsObject.pubDate = object['pubDate'];
        newsObject.title = object['title'];
        newsObject.link = object['link'];
        newsObject.image_url = object['image_url'];
        news_src_list.append(newsObject)
    except Exception as error:
        print("An exception occurred," , error)

print ('Total Length->', len(news_src_list), ' json_data raw -->' , news_src_list)

news_src_json = jsonpickle.encode(news_src_list)

r = redis.Redis(host='bayi', port=8150, db=0)
today_date = str(date.today()) + "_redis_news"

redisFile = open(today_date + "_redis.txt", "r+")
redisFile.write(news_src_json)
redisFile.close()

redisFile = open(today_date + "_redis.txt", "r+")
news_redis_json = redisFile.read()
redisFile.close()
# r.set(today_date, news_src_json)

#news_redis_json = r.get(today_date);

print ('file news -->' + news_redis_json)
news_redis_obj = jsonpickle.decode(news_redis_json)
print ('length news_redis_obj after save -->' , len(news_redis_obj))

for value in news_redis_obj:
    try:
        # print(value.title)
        answer = GPT.askGPTDummyYes('Important?' + value.title)
        print ("raw answer-->" , answer)
        yes_or_no = is_yes(answer)
        answer = remove_yes_or_no(answer)
        value.isPositive = yes_or_no
        value.news_ai = answer
        print ("processed answer-->" , yes_or_no , "." + answer)
        
    except Exception as error:
        print("An exception occurred," , error)
        print(traceback.format_exc())

redisFile = open(today_date + "_redis.txt", "r+")
news_src_json = jsonpickle.encode(news_redis_obj)
redisFile.write(news_src_json)
redisFile.close()
#return "Yes, it highlights the need for attitudes to evolve with new policies for effective implementation."
