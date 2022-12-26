import requests
from pprint import pprint
from yadisk import YaDisk


token = '***'
class YaUploader:
    host = 'https://cloud-api.yandex.net:443'
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'}

    def get_files_list(self):
        url = f'{self.host}/v1/disk/resources/files/'
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        # return pprint(h['name'] for h in response.json())
        return pprint(response.json())

    def get_upload_link(self, path):
        url_up = f'{self.host}/v1/disk/resources/upload/'
        headers = self.get_headers()
        params = {'path': path, 'overwrite': True}
        response = requests.get(url_up, headers=headers, params=params)
        return response.json().get('href')

    def upload(self, file_path, filename):
        upload_link = self.get_upload_link(file_path)
        headers = self.get_headers()
        response = requests.put(upload_link, data=open(filename), headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '/1/FileForUP'
    uploader = YaUploader(token)
    uploader.get_files_list()
    result = uploader.upload(path_to_file, 'FileForUP')


