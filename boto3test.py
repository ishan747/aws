import os
import boto3
# from awskeys import keyID, secretKey, token

session = boto3.Session(
aws_access_key_id='ASIAVCS4GBQG4G3YSPNN',
aws_secret_access_key='JBc1IxGs6xEmO6VK/hQZS2vHM6qIYF0uH5Xp33qF',
aws_session_token='FQoGZXIvYXdzEDwaDOxevpsVUeqtSVnJkSL7AkDgB0tG3di+Vpozzv/evLNf13bQaralhW6kMS/K9cx3fQl6Yc3/D8dndAXFh+Ko0Skx7ddmtSCHGpzlegLgIUAXHkGehgbzh4inE/l0TBsZLjWUosaIJasciffjRWOY3UizWfxVawTnry7jws0/z+3mT5O64fSicvZ9qYo7HSssaKpCxU1wy9Q5NsW4lnAkS24xUq34m2u13aepxSE4pfxCDql5Mw1t41s+dqlTFvdHHgnwD0+a535ADkHhalSGfeGI0zELA1bs4KghgBWNH9HiNdbUZ9j6/+pO/CVrM3VjIBPm6+ppSncZXojufqpBT6e2pIxmC5XfznbQ9vAlkdISf0A1QAZx6K+5v/GTkVjRDNF15DuGlCKAhr2G7AqiTuLQ1LnRlZ1jh8SO0YkUcBADmvsOc729yOwxZS0lwkG/xZCqS4BqKxjxurT4vTiyDUCOZotu0Ui+VrgYvJL07fyqhRrisWCycCX3eOWaJpDf+WmX4BvnI2rcZKgooNmk6AU=',
)

s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)


    userinput = input('Enter your username ')
    f = open('username.txt', 'w+')
    f.write(userinput)
    f.close()
    
data = open('username.txt','rb')
s3.Bucket('bucket-ishan747').put_object(Key='username.txt', Body=data)

