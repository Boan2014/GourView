import os
import pickle
import numpy as np
from wordcloud import WordCloud
import MeCab
import requests
import json

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#MODEL_DIR = os.path.join(BASE_DIR, "jupyter_notebook")
#MODEL_FILE = os.path.join(MODEL_DIR, "iris.sav")


class PredictionService:
    #model = pickle.load(open(MODEL_FILE, mode="rb"))

    @staticmethod
    def predict(data):

        keyid = "962a4a80cbead6a3722544f4363899fe"
        name = data["name"]
        url_res = "https://api.gnavi.co.jp/RestSearchAPI/v3/?keyid=" + keyid + "&name=" + name

        response = requests.get(url_res)
        jsonData = response.json()

        latitude = jsonData["rest"][0]["latitude"]
        longitude = jsonData["rest"][0]["longitude"]

        url_review = "https://api.gnavi.co.jp/PhotoSearchAPI/v3/?keyid=" + keyid + "&latitude=" + latitude + "&longitude="+ longitude +"&hit_per_page=50"

        response = requests.get(url_review)
        jsonData = response.json()

        text = ""
        total_hit_count = jsonData["response"]['total_hit_count']
        hit_per_page = 50

        if total_hit_count < hit_per_page:
            count = total_hit_count
        else:
            count = hit_per_page
            
        for i in range(count):
            text += (jsonData["response"][str(i)]["photo"]["comment"])
        
        mecab = MeCab.Tagger()

        nodes = mecab.parseToNode(text)
        hcount = {}
        while nodes:
            hinshi = nodes.feature[:2]
            word = nodes.surface
            if hinshi == '名詞':
                if word in hcount.keys():
                    freq = hcount[word]
                    hcount[word] = freq + 1
                else:
                    hcount[word] = 1
            nodes = nodes.next
        res = []
        for key,value in hcount.items():
            res.append({"name":key,"value":value})
        return res