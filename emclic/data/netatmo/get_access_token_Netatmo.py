import requests as re
from requests.structures import CaseInsensitiveDict
import json

# So far unsuccessful attempt at retrieving access token from netatmo

get_access_url = "https://api.netatmo.com/oauth2/token"  # OK

with open("netatmo_client_id.txt", "r") as f:
    client_id = f.readlines()
    
client_id = client_id[0].rstrip("\n") # Not checked

print("client_id: \n", client_id, "\n")

with open("netatmo_client_secret.txt", "r") as f:
    client_secret = f.readlines()

client_secret = client_secret[0].rstrip("\n") # Not checked

print("client secret: \n", client_secret, "\n")

headers_json = CaseInsensitiveDict()
headers_url = CaseInsensitiveDict()
headers_url["content-type"] = "application/x-www-form-urlencoded"
headers_url["Authorization"] = "bearer"
headers_json["content-type"] = "application/json"  # not checked

# note, the code as of now will not run, since the username and  password fields are not filled in
data = {'grant_type' : 'password', 'client_id' : '6221fa3fa7afb20de310c20c', 'client_secret' :'yXf8j8sJMdVZ0TiU7yQH7N6iRuoQyoNgP', 'username' : "<INSERT USERNAME>", 'password' : '<INSERT PASSWORD>'}
print("\n data: \n", data, "\n")
data_json =  json.dumps(data)
print("Json.dumps(data): \n", data_json, "\n")
print("headers json: \n", headers_json, "\n")
print("url: \n", get_access_url, "\n")

# changed from scope : "none_required"

print(data)

#resp = re.post(get_access_url, json = data, allow_redirects = True)
resp = re.post(get_access_url, data = data, headers = headers_url)
#resp = re.post(full_url, allow_redirects = True)
print(resp)
print(resp.content)
