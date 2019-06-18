import boto3
from awskeys import *

session = boto3.Session(
aws_access_key_id=aws_access_key_id,
aws_secret_access_key=aws_secret_access_key,
aws_session_token=aws_session_token,
)

s3 = session.resource('s3')

userinput = input('Enter your username: ')
f = open('username.txt', 'w+')
f.write(userinput)
f.close()

data = open('username.txt','rb')
s3.Bucket('bucket-ishan747').put_object(Key='username.txt', Body=data)

s3.Bucket('bucket-ishan747').download_file('username.txt', 's3downloadusername.txt')

output = open('s3downloadusername.txt', 'r')
print(output.read())

s3.Object('bucket-ishan747', 'username.txt').delete()

