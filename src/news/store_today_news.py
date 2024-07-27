from _datetime import date
import json

import jsonpickle
import redis
import requests

from news.gpt import GPT
import string
import traceback
import os
from finder.news.news_redis import News

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

def process_negative_news(news_redis_obj):
    for value in news_redis_obj:
        try:
        # print(value.title)
        #answer = GPT.askGPTDummyYes('Important?' + value.title)
            if value.isPositive == False: 
                #answer = GPT.askGPTDummyWellBeing(value.news_ai)
                answer = GPT.askGPT_well_being(value.news_ai)
                print ("well being raw answer-->" , answer)
                value.well_being_ai = answer
        
        except Exception as error:
            print("An exception occurred," , error)
            print(traceback.format_exc())
    return news_redis_obj

def process_bible_news(news_redis_obj):
    for value in news_redis_obj:
        try:
        # print(value.title)
        #answer = GPT.askGPTDummyYes('Important?' + value.title)
            answer = GPT.askGPT_bible(value.title)
            value.bible_ai = answer
        
        except Exception as error:
            print("An exception occurred," , error)
            print(traceback.format_exc())
    return news_redis_obj

r = requests.get("https://newsdata.io/api/1/news?apikey=pub_49037ebd46b4a3fd58ca99decfb2cd2e52794&q=malaysia&country=my")
#r = requests.get("http://localhost:8080/examples/news.txt")

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

# r = redis.Redis(host='bayi', port=8150, db=0)
news_dir = os.environ.get('NEWS_DIR')
file_name = str(news_dir) + str(date.today()) + "_redis_news.txt"

redis_file = open(file_name, "w")
redis_file.write(news_src_json)
redis_file.close()

redis_file = open(file_name, "r+")
news_redis_json = redis_file.read()
redis_file.close()
# r.set(today_date, news_src_json)

#news_redis_json = r.get(today_date);

print ('file news -->' + news_redis_json)
news_redis_obj = jsonpickle.decode(news_redis_json)
print ('length news_redis_obj after save -->' , len(news_redis_obj))

for value in news_redis_obj:
    try:
        # print(value.title)
        #answer = GPT.askGPTDummyYes('Important?' + value.title)
        answer = GPT.askGPT('Important?' + value.title)
        print ("raw answer-->" , answer)
        yes_or_no = is_yes(answer)
        answer = remove_yes_or_no(answer)
        value.isPositive = yes_or_no
        value.news_ai = answer
        print ("processed answer-->" , yes_or_no , "." + answer)
        
    except Exception as error:
        print("An exception occurred," , error)
        print(traceback.format_exc())

news_redis_obj = process_negative_news(news_redis_obj)
news_redis_obj = process_bible_news(news_redis_obj)
news_dir = os.environ.get('NEWS_DIR') 
redis_file = open(file_name, "w")
        
news_src_json = jsonpickle.encode(news_redis_obj)
redis_file.write(news_src_json)
redis_file.close()
#return "Yes, it highlights the need for attitudes to evolve with new policies for effective implementation."
