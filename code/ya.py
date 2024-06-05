import requests
import tqdm

from pprint import pprint
from urllib.parse import urlencode

class YaKlient:
    API_BASE_URL = 'https://cloud-api.yandex.net'

    def __init__(self, token):
        self.headers = {'Authorization': f'OAuth {token}'}

    def upload_file (self, url, path):
        params = {'url': url, 'path': path}
        r = requests.post(
            f'{self.API_BASE_URL}/v1/disk/resources/upload', params=params, headers=self.headers)
        if r.status_code != 202:
            raise Exception(r.text)
        return r.json()

    def create_folder (self, path):
        params = {'path': path}
        r = requests.put(
            f'{self.API_BASE_URL}/v1/disk/resources',
            params=params,
            headers=self.headers)
        answer = r.json()

        if r.status_code == 201:
            return True, r.status_code, ''
        return False, r.status_code, answer['message']

# if __name__ == '__main__':
#     ya_client = YaKlient(token_yadisk)
#     ya_client.create_folder('disk:/NewFolder')


