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

dfilename = "..\downloads\d.zip"

ddirname = os.path.dirname(dfilename)

zfilename = "..\\features"

if not os.path.exists(ddirname):
    os.makedirs(ddirname)

with open(dfilename,"wb") as f:
    f.write(reponse1.content)

with ZipFile(dfilename,'r') as zip:
    zip.extractall(zfilename)



