from helpers import crudAPI
from utility import Config
import json
import jsonpath
import time


#def importantFunction():
#	print("This is one of the important Function. I have used.")
purl = Config.readConfigData("APIDetails", "get_url")


details = {"name": "morpheus", "job": "leader"}

a = crudAPI.hitpostApi("post", purl, details)
json_response = json.loads(a)
print(json_response)
x = jsonpath.jsonpath(json_response, 'name')
y = jsonpath.jsonpath(json_response, 'job')
z = jsonpath.jsonpath(json_response, 'createdAt')
print(x, y, z)
a_time = time.time()
assert x[0] == "morpheus"
assert y[0] == "leader"
#assert z[0] == a_time[0]
#createdAt