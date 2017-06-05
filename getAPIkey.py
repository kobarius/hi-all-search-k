# -*- coding: utf-8 -*-

import ConfigParser
import os

def getAPIkey(API_KEY,DefStr,EnvName) :
	if API_KEY == DefStr :
		API_KEY = os.getenv(EnvName, '')

	if API_KEY == "":
		API_KEY = 'API_KEY_ERROR'

	return API_KEY


if __name__ == '__main__':
	inifile = ConfigParser.SafeConfigParser()
	inifile.read('./config.ini')

	API_KEY = inifile.get('settings', 'GOOGLE_API_KEY')
	DefStr = 'Set_Your_Google_API_KEY'
	EnvName = 'GOOGLE_API_KEY'

	API_KEY = getAPIkey(API_KEY,DefStr,EnvName)

	print( API_KEY )

