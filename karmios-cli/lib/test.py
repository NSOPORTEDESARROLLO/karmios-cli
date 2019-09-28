#!/usr/bin/python3


import subprocess 
import json

result = subprocess.run(['/opt/karmios-cli/lib/docker_functions.sh', 'dockers'], stdout=subprocess.PIPE)
dockers =  json.loads((str(result.stdout, 'utf-8')))

print(dockers['cloudnode']['status'])
