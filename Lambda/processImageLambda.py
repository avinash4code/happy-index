from __future__ import print_function

import json
import boto3
import base64

def lambda_handler(event, context):    
    req = json.loads(event['body'])
    if (not req.has_key('image') or req['image'] == None):
        return {"Error":"Hahahah!!"}
    else:
        session = boto3.Session(profile_name='personal2')
        rekog = session.client('rekognition', region_name='us-east-1')
        
        faces = rekog.detect_faces(
            Image = {
                'Bytes': base64.decodestring(req['image'])
            },
            Attributes = [
                'ALL'
            ]
        )
        return {
            "isBase64Encoded": True,
            "statusCode": 200,
            "headers": { "foo": "what!!!" },
            "body": faces
        }

    
        