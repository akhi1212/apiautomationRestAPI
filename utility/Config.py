import os
import configparser

def readConfigData(section, key):
    config = configparser.ConfigParser()
    ##G:\framework_setup\locators_testdata\locator.cfg
    data = os.path.relpath('../configurations/Config.cfg')
    config.read(data)
    return config.get(section, key)


print(readConfigData('APIDetails', 'application_url'))