#!/usr/bin/python3


import os
import json

def GetModuleInfo():
	#Obteniendo la lista de directorios de la carpeta de modulos 
	ModuleList=os.listdir("/opt/karmios-cli/modules")
	data = {}

	for module in ModuleList:

		ModulePath="/opt/karmios-cli/modules/" + str(module) + "/module.json" 
		

		if os.path.isfile(ModulePath):

			with open(ModulePath) as json_file:

				tmp = json.load(json_file)

				data[module] = { 'description' : tmp['description'] }
	 
	return data			


if __name__ == "__main__":
	data=GetModuleInfo()
	print(json.dumps(data, indent=4))



