import boto3

s3 = boto3.resource('s3',
aws_access_key_id='ASIAVCS4GBQG25PEFOF5',
aws_secret_access_key='xXC7VfcZ8lviUhbQg2tfOzuAxjRDLRB5K+dfgq2M',
aws_session_token='FQoGZXIvYXdzECUaDLDXZKboQWjlvsTjkCL7AtCgBQ9wvqEMi/jbJ4PSD8VXT47hQz/rPiTwuyqi9MmgoKEs5H6uj1kt4Edl+kvtb37MG0PILjed7/us6hnW8sTPydjmcOwe+sisiYoZoiJ9n3vjEhpPWxB3Tu1gR+mVSP/Q5AZ4I1I2agCFtgM+NzmViQIHR9oEHS3CPGlRXL4iLzE+fWoyUOPhu/y5hogNfvwXWPDkqZJjWrnq2qNLKveDZWBGoN3RavBvhbNsy7fndeRb9zNzcUZmjS7mM8npBqfD5NyzOd+Svx9bbrkqBnxcEO6CEDidb4kLD55gkLwb+Q6VIpcg+BJF9B062Xm+NqmI7LzYUTGrdx0Dis7D+nfdmzQplrFO86Mxg4KiQv2mO2WYaR6p70uOLIhbge5EvdCDwFvdbU8EaA2NiyDsylQug8jf2ejWEXPT5IKmGrHkJuJSIb+EJx/Tm1yCQdqb/r3ev0QoquyQw3VzuJre/BvVAY0/hVnSEWlTFSybNc2UeJ4FZjTIVCSmrDgonNif6AU=',
)
for bucket in s3.buckets.all():
    print(bucket.name)

data = open('test.jpg', 'rb')
s3.Bucket('bucket-ishan747').put_object(Key='test.jpg', Body=data)
