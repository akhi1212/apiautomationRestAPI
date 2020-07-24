import sys
sys.path.append('G:\\framework_practicsse\\apiautomation')
print(sys.path)
from helpers import crudAPI
from utility import Config
import json
import jsonpath
import logging



def  test_verifyUser():
	gurl = Config.readConfigData("APIDetails", "get_url")
	logging.basicConfig(level=logging.DEBUG)
	a = crudAPI.hitgetApi("get", gurl)
	logger = logging.getLogger(__name__)
	logger.info('Start api tests')
	json_response = json.loads(a)
	print(json_response)
	x = jsonpath.jsonpath(json_response, 'total')
	print(x)
	assert x[0] == 121
	logger.debug('Records: %s', input)