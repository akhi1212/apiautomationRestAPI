import sys
sys.path.append('G:\\framework_practicsse\\apiautomation')
print(sys.path)
from helpers import crudAPI
from utility import Config
import json
import jsonpath


gurl = Config.readConfigData("APIDetails", "get_url")

a = crudAPI.hitgetApi("get", gurl)
#print(a)

json_response = json.loads(a)
print(json_response)
x = jsonpath.jsonpath(json_response, 'total')
print(x)
assert x[0] == 12