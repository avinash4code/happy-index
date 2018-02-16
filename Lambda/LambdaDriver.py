import json
import os
import base64
from processImageLambda import lambda_handler

request = json.load(open('C:\HobbyProjects\happy-index\Lambda\sample-request.json'))

with open("C:\HobbyProjects\happy-index\DSC07957.JPG", "rb") as image_file:
    request['body'] = "{\"image\":\""+ base64.b64encode(image_file.read()) +"\"}" 

response = lambda_handler(request, '')
print response