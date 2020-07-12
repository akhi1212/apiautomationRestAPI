from helpers import crudAPI
from utility import Config

#def importantFunction():
#	print("This is one of the important Function. I have used.")
purl = Config.readConfigData("APIDetails", "get_url")


details = {"name": "morpheus", "job": "leader"}

a = crudAPI.hitpostApi("post", purl, details)