import os
#import pickle
#import numpy as np
#from wordcloud import WordCloud
import MeCab
import requests
import json

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#MODEL_DIR = os.path.join(BASE_DIR, "jupyter_notebook")
#MODEL_FILE = os.path.join(MODEL_DIR, "iris.sav")


class WordCloudService:
    #model = pickle.load(open(MODEL_FILE, mode="rb"))

    def __init__(self,data):
        self.data = data
     
    def YahooReview(self,name):
        res = {}
        name = name
        YResUrl = "https://map.yahooapis.jp/search/local/V1/localSearch?appid="+ YKeyId+"&query="+name + "&output=json"

        #only 10 shop 
        YResResponse = requests.get(YResUrl)
        YResJsonData = YResResponse.json()

        if "Feature" in YResJsonData.keys():
            YShopId = YResJsonData["Feature"][0]["Property"]["Uid"]
            YReviewUrl = "https://map.yahooapis.jp/olp/v1/review/" + YShopId + "?appid=" + YKeyId +"&output=json"
            
            YReviewResponse = requests.get(YReviewUrl)
            YReviewJsonData = YReviewResponse.json()

            
            if YReviewJsonData["ResultInfo"]["Count"] != 0:
                for i in range(YReviewJsonData["ResultInfo"]["Count"]):
                    res[i] = YReviewJsonData["Feature"][i]["Property"]['Comment']['Body']
                return res
            else:
                return res
        else:
            return res
        
    def GoogleReview(self, name):
        res = {}
        name = name
        GResUrl = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="+ name+"&fileds=place_id&inputtype=textquery&key="+GKeyId
        
        GResResponse = requests.get(GResUrl)
        GResJsonData = GResResponse.json()

        if GResJsonData["status"] == "OK":
            GShopId = GResJsonData["candidates"][0]["place_id"]
            GReviewUrl = "https://maps.googleapis.com/maps/api/place/details/json?place_id=" + GShopId + "&language=ja&fields=reviews&key=" + GKeyId
            
            GReviewResponse = requests.get(GReviewUrl)
            GReviewJsonData = GReviewResponse.json()
            
            for i in range(len(GReviewJsonData["result"]["reviews"])):
                if GReviewJsonData["result"]["reviews"][i]["language"] == "ja":
                    res[i] = GReviewJsonData["result"]["reviews"][i]["text"]
            return res
        else:
            return res

    def GurunabiReview(self, name):
        res = {}
        name = name
        GuResUrl = "https://api.gnavi.co.jp/RestSearchAPI/v3/?keyid=" + GuKeyId + "&name=" + name
  
        GuResResponse = requests.get(GuResUrl)
        GuResJsonData = GuResResponse.json()

        if "error" not in GuResJsonData.keys():
            GuShopId = GuResJsonData["rest"][0]["id"]
            #latitude = GuResJsonData["rest"][0]["latitude"]
            #longitude = GuResJsonData["rest"][0]["longitude"]

            #url_review = "https://api.gnavi.co.jp/PhotoSearchAPI/v3/?keyid=" + GuKeyId + "&latitude=" + latitude + "&longitude="+ longitude +"&hit_per_page=50"
            GuReviewUrl = "https://api.gnavi.co.jp/PhotoSearchAPI/v3/?keyid=" + GuKeyId + "&shop_id=" + GuShopId +"&hit_per_page=50"

            GuReviewResponse = requests.get(GuReviewUrl)
            GuReviewJsonData = GuReviewResponse.json()
            
            if "gnavi" in GuReviewJsonData.keys():
                return res    
            else:
                total_hit_count = GuReviewJsonData["response"]['total_hit_count']
                hit_per_page = 50

                if total_hit_count < hit_per_page:
                    count = total_hit_count
                else:
                    count = hit_per_page
                    
                for i in range(count):
                    res[i] = (GuReviewJsonData["response"][str(i)]["photo"]["comment"])
                return res
        else:
            return res
            
    def worldcloud(self,text):
        if text == "":
            return [{"name":"no reslue", "value":100}]
        else:
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
    
    def emotion(self,allReview):
        #APIキーを入力
        posScore = 0
        negScore = 0
        posRev = {"score" : 0.0, "review" : ""}
        negRev = {"score" : 0.0, "review" : ""}
        posCount = 1
        negCount = 1

        url = 'https://language.googleapis.com/v1/documents:analyzeSentiment?key=' + key

        #感情分析したいテキスト
        for api in allReview.keys():
            for i in allReview[api].keys():
                text = allReview[api][i]

                #基本情報の設定 JAをENにすれば英語のテキストを解析可能
                header = {'Content-Type': 'application/json'}
                body = {
                    "document": {
                        "type": "PLAIN_TEXT",
                        "language": "JA",
                        "content": text
                    },
                    "encodingType": "UTF8"
                }

                response = requests.post(url, headers=header, json=body).json()
                score = response["documentSentiment"]["score"]

                if score > 0:
                    posCount += 1
                    posScore += score
                    if score > posRev["score"]:
                        posRev["score"] = score
                        posRev["review"] = text
                else:
                    negCount += 1
                    negScore += score
                    if score < negRev["score"]:
                        negRev["score"] = score
                        negRev["review"] = text
                
        #res = {"posScore":posScore,"negScore":negScore, "posRev":posRev,"negRev":negRev}
        res = [posScore/posCount,negScore/negCount, posRev["review"],negRev["review"]]
        return res
        
    def nlp(self):
        allReview = {}
        name = self.data["name"]

        allReview["Yahoo"] = self.YahooReview(name)
        allReview["Google"] = self.GoogleReview(name)
        allReview["Gurunabi"] = self.GurunabiReview(name)
        
        #return allReview
        
        text = ""
        for api in allReview:
            for i in allReview[api]:
                text += allReview[api][i]
        
        res = [self.worldcloud(text),self.emotion(allReview)]
        return res
        #return [[{"name":"haha", "value":3}],[0.4,0.6, "review","review"]]