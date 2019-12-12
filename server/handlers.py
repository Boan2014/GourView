from services import PredictionService


class PredictionResource:

    @staticmethod
    async def on_post(req, resp):
        data = await req.media()
        res = PredictionService.predict(data)
        #res = "wocaole"
        resp.media = {
            "status": True,
            "result": res
        }