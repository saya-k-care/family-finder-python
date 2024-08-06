from _datetime import date
import json

import jsonpickle
import redis
import requests

import string
import traceback
import os
from news.gpt import GPT
from news.news_redis import News
from rss_google import RSSGoogle
import logging
from news.get_news import GetNews

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
            if value.is_duplicate == True:
                print ("skip process_negative_news,", value.isPositive)
        #answer = GPT.askGPTDummyYes('Important?' + value.title)
            else:
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
            if value.is_duplicate == True:
                print ("skip process_bible_news,", value.isPositive)
            else:
                answer = GPT.askGPT_bible(value.title)
                value.bible_life = GPT.askGPT_bible_life(answer)
                value.bible_ai = answer
        
        except Exception as error:
            print("An exception occurred," , error)
            print(traceback.format_exc())
    return news_redis_obj

def translate_my_desc(news_redis_obj):
    for value in news_redis_obj:
        try:
        # print(value.title)
            if value.is_duplicate == True:
                print ("skip translate_my_desc,", value.description_my)
            else:
                answer = GPT.askGPT_translate_my(value.description)
                value.description_my = answer
        
        except Exception as error:
            print("An exception occurred," , error)
            print(traceback.format_exc())
    return news_redis_obj

def process_cn(news_redis_obj):
    try:
        for value in news_redis_obj:
            try:
                if value.is_duplicate == True:
                    print ("skip process_cn,", value.description)
                else:
                    news_prepare_cn = News()
                    news_prepare_cn.description = value.description
                    news_prepare_cn.bible_life = value.bible_life

                #json_string = news_prepare_cn.toJSON()
                    json_string = 'description_cn:' + str(news_prepare_cn.description) + '  + bible_life_cn:' + str(news_prepare_cn.bible_life)
                    data = GPT.askGPT_translate_cn(json_string)

                    print ("news_cn_json-->" + str(data))
                    json_dict = json.loads(data)
                    value.description_cn = json_dict["description_cn"]
                    value.bible_life_cn = json_dict["bible_life_cn"]
                    value.pinyin = json_dict["bible_life_pinyin"]
            except Exception as error:
                print("An exception occurred:", error)
                print(traceback.format_exc())
    except Exception as error:
        print("An exception occurred:", error)
        print(traceback.format_exc())
    return news_redis_obj

def newsdata(news_src_list):
    r = requests.get("https://newsdata.io/api/1/latest?apikey=pub_49037ebd46b4a3fd58ca99decfb2cd2e52794&q=malaysia&country=my")
#r = requests.get("http://localhost:8080/examples/news.txt")

    new_str = str(r.text)
    new_str = new_str.replace("b'", "")
    new_str = new_str.replace("\r\n", "")

    jsonObject = json.loads(new_str)

    results = jsonObject["results"]

    for object in results:
        try:
            print ("pubDate-->", object['pubDate'] )  
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
        return news_src_list

logging.basicConfig(filename='storenews.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logger = logging.getLogger('urbanGUI')

logging.info("Starting process news")

def process_google_news(news_src_list, old_news_redis_obj):
    try:
        news_src_list = RSSGoogle.processGoogleNews(news_src_list, old_news_redis_obj)
        print ('Total Length->', len(news_src_list), ' json_data raw -->' , news_src_list)
        news_src_json = jsonpickle.encode(news_src_list)
        
    except Exception as error:
            print("An exception occurred," , error)
            print(traceback.format_exc())
    return news_src_json

def make_news_temp_file(news_src_list,file_name):
    try:
# r = redis.Redis(host='bayi', port=8150, db=0)

        redis_file = open(file_name + "_temp", "w", encoding="utf-8")
        redis_file.write(news_src_json)
        redis_file.close()

        redis_file = open(file_name + "_temp", "r+", encoding="utf-8")
        news_redis_json = redis_file.read()
        redis_file.close()
        
    except Exception as error:
            print("An exception occurred," , error)
            print(traceback.format_exc())
    return news_src_json

def process_news_ai_is_positive(news_redis_obj):
    try:
        logging.info('length news_redis_obj after save -->')
        for value in news_redis_obj:
            try:
        # print(value.title)
        #answer = GPT.askGPTDummyYes('Important?' + value.title)
                if value.is_duplicate == True:
                    print ("skip process_news_ai_is_positive,", value.isPositive)
                else:
                    answer = GPT.askGPT('Important?' + value.title)
                    yes_or_no = is_yes(answer)
                    answer = remove_yes_or_no(answer)
                    value.isPositive = yes_or_no
                    value.news_ai = answer
                    print ("processed new answer-->" , yes_or_no , "." + answer)
        #logging.info("processed answer-->" , yes_or_no , "." + answer)
            except Exception as error:
                print("An exception occurred," , error)
                print(traceback.format_exc())
        
    except Exception as error:
        print("An exception occurred," , error)
        print(traceback.format_exc())
        
    return news_redis_obj

news_src_list=[]
old_news_redis_obj = GetNews.get_today_all_news()
news_src_json = process_google_news(news_src_list, old_news_redis_obj)
news_dir = os.environ.get('NEWS_DIR')
file_name = str(news_dir) + str(date.today()) + "_redis_news.txt"

news_redis_json = make_news_temp_file(news_src_list, file_name)
# r.set(today_date, news_src_json)

#news_redis_json = r.get(today_date);

print ('file news -->' + news_redis_json)
news_redis_obj = jsonpickle.decode(news_redis_json)
print ('length news_redis_obj after save -->' , len(news_redis_obj))
news_redis_obj = process_news_ai_is_positive(news_redis_obj)
logging.info("processed negative news")
news_redis_obj = process_negative_news(news_redis_obj)
logging.info("processed bible news")
news_redis_obj = process_bible_news(news_redis_obj)

news_redis_obj = translate_my_desc(news_redis_obj)
news_redis_obj = process_cn(news_redis_obj)
logging.info("processed bahasa")
redis_file = open(file_name, "w", encoding="utf-8")
        
news_src_json = jsonpickle.encode(news_redis_obj)
news_redis_obj = list(dict.fromkeys(news_redis_obj))
redis_file.write(news_src_json)
redis_file.close()
logging.info("processing done")
#return "Yes, it highlights the need for attitudes to evolve with new policies for effective implementation."
