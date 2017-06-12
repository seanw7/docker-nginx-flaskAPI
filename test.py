import requests
#rom requests_jwt import JWTAuth
import json
#import requests_oauthlib



#r = requests.get("http://192.168.99.100:80/genera")
#response = r.json()

#print(response['genera'][0]['species'])


#print(r.headers)
#print(r)

url = "http://192.168.99.100:80/"
#url = "http://172.17.0.2"
#endpoints = "plant"


def populate_db():
    name_list = ["radicalis", "tepilajote", "metallica"]
    for word in name_list:
        #headers = {"Authorization": "JWT %s" % auth_token}
        #headers = {"Authorization": "JWT {}".format(auth_token)}
        payload2 = {"price": 25.99, "genus_id": "Chamaedorea", "quantity": 10}
        r = requests.put(url + "plant/" + word, data=json.dumps(payload2), headers=auth_header)#, headers=headers)
        #print(r.headers)
        print(r.status_code)
        #print(r.text)
        print(r.url)

def create_user():
    payload = {'username': 'testacc2', 'password': 'asdf'}
    headers = {'content-type': 'application/json'}
    r = requests.post(url+"register", data=json.dumps(payload), headers=headers)
    print(r.text)


#create_user()
headers = {'content-type': 'application/json'}
payload = {'username': 'testacc2', 'password': 'asdf'}
# attempts to authenticate the specified user data
auth = requests.post(url+"auth", data=json.dumps(payload), headers=headers)
# use json.loads() to turn auth.text into dict format
auth_enc = json.loads(auth.text)
auth_token = "JWT %s" % auth_enc['access_token']
#print(str(auth_token))
auth_header = {'authorization': auth_token, 'content-type': 'application/json'}

populate_db()


class APIConnect():
    url = "http://192.168.99.100:80/"
    auth_token = ""

    def __init__(self, username, password, **kwargs):
        self.username = username
        self.password = password
        self.kwargs = kwargs

    def create_user2(self):
        payload = {'username': self.username, 'password': self.password}
        headers = {'content-type': 'application/json'}
        r = requests.post(url + "register", data=json.dumps(payload), headers=headers)
        self.auth_token = r.text
        return r.text

    def add_plants(self, entry_list):
        #payload = {'price': self.}
        for word in entry_list:
            payload = {'price': 15.99, 'genus_id': 'Chamaedorea', 'quantity': 10}
            auth_header = {'authorization': self.auth_token, 'content-type': 'application/json'}
            req = requests.put(self.url + 'plant' + word, data=json.dumps(payload), headers=self.)
            return word
