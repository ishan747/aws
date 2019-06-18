import os
import boto3
from awskeys import keyID, secretKey, token

session = boto3.Session(
aws_access_key_id='ASIAVCS4GBQG6GZINNHC',
aws_secret_access_key='s8xHn40ztunw/80JROvdBFvbepLZ6GQgDtCB7w0B',
aws_session_token='FQoGZXIvYXdzEDsaDAevx5sG2Wf7+REO7CL7AhgSWcUmLX9Kx0UFnTiitLkDuj0htKx/3y72i86Leyxo4w+z3jRhWdfiKIwRbuDQS1hK0wuc0TeUSfn1wf1/6pknIxpJNG/8VUwbu81VnzAhaaK2YTFJHGnTN0ve/5cQaKkDTwmltNo9pgJ3IAvdxjD/zQOtG4w22mVDU+IU6lxYrye87clgvZQpspX1/+HG6/vetnH3La5UQCERQYO+cLXK2S+Cegh3VOmqNSgBxU8gsI7KGm1PGxMJg06tEaxO7iW45eQ56ZNjriOiDD11NplF0YZbSgwHcH1zXG8yc4aNgf0oM2z8zzZ/9WRC4468UXcRanHn1f++85Vewl0qCOXjWz5XZfPPZlZXxF+7ef0oFrxZ3V7Y2DlPCkKAHRuYPF8T/b+ZX5dlj/KzfvjcD4lRA+nOdCvZPDdZJ1agiFVjq2rHQsZ5zKHTGEWk3FKUnDHwxFC4XwiXNjX5E2qjseUVavabFOQAorQ+F8zUbjYmg6FlWOASaMn+zy4oyLSk6AU=',
)

s3 = session.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

def createUserNameFile(userName):
    userinput = input('Enter your username ')
    f = open('username.txt', 'w')
    f.write(userinput)
    f.close()


s3.Bucket('bucket-ishan747').put_object(Key='username.txt')
