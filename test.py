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
        payload2 = {"price": 12.99, "genus_id": "Chamaedorea", "quantity": 10}
        r = requests.put(url + "plant/" + word, data=json.dumps(payload2), headers=auth_header)#, headers=headers)
        print(r.headers)
        print(r.status_code)
        print(r.text)
        print(r.url)

def create_user():
    payload = {'username': 'testacc2', 'password': 'asdf'}
    headers = {'content-type': 'application/json'}
    r = requests.post(url+"register", data=json.dumps(payload), headers=headers)
    print(r.text)





#create_user()
headers = {'content-type': 'application/json'}
payload = {'username': 'testacc2', 'password': 'asdf'}
auth = requests.post(url+"auth", data=json.dumps(payload), headers=headers)

auth_enc = json.loads(auth.text)
auth_token = "JWT %s" % auth_enc['access_token']
#print(str(auth_token))
auth_header = {'Authorization': auth_token, 'content-type': 'application/json'}

populate_db()
