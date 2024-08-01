import openai
import os
from _datetime import date
import requests
import jsonpickle
import json
import time

ai_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = ai_key

class GPT:
    @staticmethod
    def askGPT(str):
        ques = str + " .Is this a positive, not politic related and important news? Answer yes or no and explain in less than 15 words";
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
           
            messages=[
                {"role": "user", "content": ques}
                ],)
        time.sleep(1)
        #print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    @staticmethod
    def askGPT_well_being(str):
        ques = str + " .The corruption surge. How is this news impact well being if reading too much. Explain in less than 15 words";
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": ques}
                ],)
        time.sleep(1)
        #print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    @staticmethod
    def askGPT_badminton():
        r = requests.get("https://news.google.com/rss/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVTFaR2dKTldTZ0FQAQ?hl=en-MY&gl=MY&ceid=MY:en")
        trim_str = r.text[0:2000]
        print ("trim_str-->" + trim_str)
        ques = trim_str + " . Give me sport comments summary in 50 words";
        completion = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": ques}
                ],)
       
        result = completion.choices[0].message.content
        print(result)
       
        #summary = result + " .Provide a score result and some sport comments"
        #completion = openai.chat.completions.create(
        #    model="gpt-4o",
        #    messages=[
        #        {"role": "user", "content": summary}
        #        ],)
        #result = completion.choices[0].message.content
        #print(result)      
        return completion.choices[0].message.content
   
    @staticmethod
    def askGPT_bible(str):
        ques = str + " Map this news to Bible verse in less than 20 words";
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": ques}
                ],)
        time.sleep(1)
        #print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    @staticmethod
    def askGPT_bible_life(str):
        ques = str + " . Give a Bible life example in less than 50 words";
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": ques}
                ],)
        time.sleep(1)
        #print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    @staticmethod
    def askGPT_description(str):
        ques = str + " . Summarize this in less than 50 words";
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            # response_format= {"type": "json_object"},
            messages=[
                {"role": "user", "content": ques}
                ],)
        time.sleep(1)
        print("askGPT_description-->", completion.choices[0].message.content)
        return completion.choices[0].message.content

    @staticmethod
    def askGPT_translate_my(str):
        ques = str + " . Translate this into Bahasa Melayu.";
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            # response_format= {"type": "json_object"},
            messages=[
                {"role": "user", "content": ques}
                ],)
        time.sleep(1)
        print("askGPT_description-->", completion.choices[0].message.content)
        return completion.choices[0].message.content
    
    @staticmethod
    def askGPT_translate(str):
        ques = str + " . Translate this into Chinese and Malay in less than 5 words in JSON string only";
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            response_format= {"type": "json_object"},
            messages=[
                {"role": "user", "content": ques}
                ],)
        time.sleep(1)
        print(completion.choices[0].message.content.encode("utf-8"))
        return completion.choices[0].message.content
           
    @staticmethod
    def askGPTDummyYes(str):
        return "Yes, it highlights the need for attitudes to evolve with new policies for effective implementation."

    @staticmethod
    def askGPTDummyWellBeing(str):
        return "Excessive exposure to corruption news can heighten stress and erode trust in institutions."

    @staticmethod
    def askGPTDummyNo(str):
        return "No, it reflects divisive rhetoric, which can intensify political tensions."      
   
    @staticmethod
    def process_cn_malay(news_src_json):
        return "No, it reflects divisive rhetoric, which can intensify political tensions."
   
    #GPT.askGPT("Over 142,000 individuals released from bankruptcy under Second Chance Policy, says PM.")

    @staticmethod
    def translateUTF8(str):
        #answer = GPT.askGPT_badminton()
        answer = "what is this"
        news_src_list=[]
        malay_chinese = GPT.askGPT_translate(answer)
        malay_chinese = malay_chinese.encode('utf-8')
        #print ('malay_chinese encode-->' , malay_chinese)
        #print (malay_chinese.decode('utf-8'))
# String containing the escape sequence
        news_src_list.append(malay_chinese.decode('utf-8'))
        news_src_json = jsonpickle.encode(news_src_list)
        redis_file = open("malay_chinese.txt", "w", encoding="utf-8")
        redis_file.write(news_src_json)
        redis_file.close()

        redis_file = open("malay_chinese.txt", "r+", encoding="utf-8")
        news_redis_json = redis_file.read()

        json_obj = jsonpickle.decode(news_redis_json)
        #json_obj = jsonpickle.encode(json_obj)
        print ("json_obj==>" , json_obj)
        #data = json.loads(json_obj[0])
        json_str = json_obj[0].strip()

# Load the JSON-like string as JSON data
        data = json.loads(json_str)

# Print the value associated with the "Malay" key
        malay_value = data["Malay"]
        print(malay_value)

        redis_file.close()  
        return json_obj

    @staticmethod
    def readDummyEncoded():

        redis_file = open("2024-07-31_redis_news.txt", "r+", encoding="utf-8")
        news_redis_json = redis_file.read()
        redis_file.close()  
        return news_redis_json

if __name__ == '__main__':
    print (GPT.readDummyEncoded())
    print (GPT.translateUTF8('test'))
