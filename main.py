import boto3
import cv2
import credentials

# create AWS Reko Client
reko_client = boto3.client('rekognition', aws_access_key_id= credentials.access_key, aws_secret_access_key=credentials.secret_key, region_name='us-east-1')
# blabla
# set the target class
target_class = 'Zebra'

# load video
cap = cv2.VideoCapture('./zebras.mp4')

frame_nmr = -1

# read frames 
ret = True
while ret:
    ret, frame = cap.read()
    H, W, _ = frame.shape

# convert frames to jpg
_, buffer = cv2.imencode('.jpg', frame)

# convert buffer to bytes
image_bytes = buffer.tobytes()

# detect objects
response = reko_client.detect_labels(Image={'Bytes': image_bytes}, MinConfidence = 70)

for label in response['labels']:
    if label['Name'] == target_class:
        for instance_nmr in range (len(label['Instances'])):
            bbox = label['instances'][instance_nmr]['BoundingBox']
            x1 = (bbox['left']) * W
            y1 = (bbox['Top']) * H
            width = bbox['Width'] * W
            height = bbox['Height'] * H
            print(x1, y1, width, height)
    break

# write detections

