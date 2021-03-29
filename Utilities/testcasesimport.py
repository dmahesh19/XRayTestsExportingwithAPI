import requests
import json
import zipfile
from zipfile import ZipFile
import shutil
import os

authheaderList = {"content-type":"application/json"}

tokenUrl = "https://xray.cloud.xpand-it.com/api/v2/authenticate"

featureUrl = "https://xray.cloud.xpand-it.com/api/v2/export/cucumber?keys=GF-11"

file = open("..\creds.json",'r')
json_input = file.read()
#req_json = json.loads(json_input)

print(json_input)

response = requests.post(tokenUrl,json_input,headers=authheaderList)

print(response.text)

token = response.text[1:-1]

print(token)

token = "Bearer "+token

featureHeaderList={"Authorization":token}

reponse1 = requests.get(featureUrl,headers=featureHeaderList,stream=True)

print(reponse1.content)

filename = "downloads\d.zip"

dirname = os.path.dirname(filename)

if not os.path.exists(dirname):
    os.makedirs(dirname)

with open(filename,"wb") as f:
    f.write(reponse1.content)

with ZipFile(filename,'r') as zip:
    zip.extractall("..\features")



