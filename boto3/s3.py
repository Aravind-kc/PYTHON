import boto3

client = boto3.client("s3")

def listBucket():
    response = client.list_buckets()
    print(response["Buckets"])
    return response

def createBucket():
    response = client.create_bucket( Bucket ='devops-bucks12345',
    CreateBucketConfiguration={
    "LocationConstraint" : "ap-south-1"
    })

    print(response)
    return response

def uploadFileS3():
    filename = "D:/PYTHON/boto3/linux_cmd.pdf"
    response = client.upload_file(filename,'devops-bucks12345', "linux_cmd.pdf" )
    print(response)

uploadFileS3()

