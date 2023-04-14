import json
import yaml

with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)

print("Su token de aceso es: {}".format(ourjson['access_token']))
print("Su token expira en: {} segundos.".format(ourjson['expires_in']))

