from services import WordCloudService


class WordCloudResource:

    @staticmethod
    async def on_post(req, resp):
        data = await req.media()
        WordCloud = WordCloudService(data)
        res = WordCloud.nlp()
        #res = "wocaole"
        resp.media = {
            "status": True,
            "result": res
        }