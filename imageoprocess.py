import boto3
import json

session = boto3.Session(profile_name='personal2')
client = session.client('rekognition', region_name='us-east-1')

in_file = open("DSC07957.jpg", "rb") # opening for [r]eading as [b]inary
data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
in_file.close()

# response = client.detect_faces(
#     Image={
#         'Bytes': data
#     },
#     Attributes=[
#         'ALL'
#     ]
# )
response = client.detect_labels(
    Image={
        'Bytes': data
    }
)

# happy = next(f for f in response["FaceDetails"][1]["Emotions"] if f["Type"] == "HAPPY")
# print(happy["Confidence"])

print (json.dumps(response, indent=4, sort_keys=True))

