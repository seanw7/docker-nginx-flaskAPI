import requests
import json


class APIConnect():
    url = "http://192.168.99.100:80/"
    auth_token = ""
    auth_header = {}


    def __init__(self, username, password, **kwargs):
        self.username = username
        self.password = password
        self.kwargs = kwargs

    def create_user(self):
        payload = {'username': self.username, 'password': self.password}
        headers = {'content-type': 'application/json'}
        r = requests.post(self.url + "register", data=json.dumps(payload), headers=headers)
        return r.text

    def authenticate(self):
        payload = {'username': self.username, 'password': self.password}
        headers = {'content-type': 'application/json'}
        r = requests.post(self.url + 'auth', data=json.dumps(payload), headers=headers)
        auth_json = json.loads(r.text)
        self.auth_token = "JWT %s" % auth_json['access_token']
        self.auth_header = {'authorization': self.auth_token, 'content-type': 'application/json'}
        return self.auth_token

    def add_plant_list(self, entry_list):
        #payload = {'price': self.}
        for word in entry_list:
            payload = {'price': 15.99, 'genus_id': 'Chamaedorea', 'quantity': 10}
            req = requests.put(self.url + 'plant/' + word, data=json.dumps(payload), headers=self.auth_header)
            if req.status_code != 200:
                return "error occurred while adding {} to database".format(word)
            return "{} added to database".format(word)

conn = APIConnect('sean', 'abc')

conn.create_user()

conn.authenticate()

name_list = ["radicalis", "tepilajote", "metallica"]

conn.add_plant_list(name_list)
