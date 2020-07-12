from helpers import crudAPI
import json
import jsonpath

def verifySamplejson(verifyValue):
    a = crudAPI.hitgetApi()
    json_response = json.loads(a)
    print(json_response)
    x = jsonpath.jsonpath(json_response, verifyValue)
    print(x)
