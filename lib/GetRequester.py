import requests
import json


class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        data_list = []
        json_data_res = json.loads(self.get_response_body())
        for some_data in json_data_res:
            data_list.append(some_data)
        return data_list
