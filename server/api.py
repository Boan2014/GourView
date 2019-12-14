import responder
from handlers import WordCloudResource

api = responder.API(
    cors=True,
    allowed_hosts=["*"],
    cors_params={"allow_origins": "*",
                 "allow_methods": "*",
                 "allow_headers": "*"
                 })

api.add_route('/api/predict', WordCloudResource)


if __name__ == '__main__':
    api.run(address="localhost", port=5045, debug=True)