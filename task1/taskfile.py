import boto3

client=boto3.client('s3')
kc=input("Enter the name of the bucket: ")

# create bucket
def createBucket(kc):
    try:
        response=client.create_bucket( 
                    Bucket=f"{kc}", 
                    CreateBucketConfiguration={'LocationConstraint':'ap-south-1'}, 
                    ObjectLockEnabledForBucket=False, 
                    ObjectOwnership='BucketOwnerPreferred'
                    )
    except Exception as e:
        print(e)

# upload objects
def uploadFiles(kc):
    try:
        response=client.put_object(
            ACL='public-read',
            Bucket=f'{kc}',
            Body=''' 
<html>
    <body>
        <h1>Welcome</h1>
        <h5>Thanks from aws</h5>
    </body>
</html>
''',
            Key='file',
            ContentType='html'
        )
        print("Object uploaded successfully...")
    except Exception as e:
        print(e)

# make public acl
def acl(kc):
    try:
        response=client.put_bucket_acl(
            Bucket=f"{kc}",
            ACL="public-read"
        )
        print("ACL is set to public...")
        return response
        # print(response)
    except Exception as e:
        print(e)

# unblock public access
def publicAccessBlock(kc):
    try:
        response=client.put_public_access_block(
            Bucket=f"{kc}",
            PublicAccessBlockConfiguration ={
            'BlockPublicAcls': False,
            'IgnorePublicAcls': False,
            'BlockPublicPolicy': False,
            'RestrictPublicBuckets': False
            }
        )
        print("Unblocked BlockPublicAccess...")
    except Exception as e:
        print(e)

# enable static website hosting
def staticHost(kc):
    try:
        response=client.put_bucket_website(
            Bucket=f"{kc}",
            WebsiteConfiguration={
                'ErrorDocument':{
                    'Key':'error.html'
                },
                'IndexDocument':{
                    'Suffix':'index.html'
                }
            }
        )
        print("Static website hosting enabled...")
    except Exception as e:
        print(e)

# List buckets
def listBuckets():
    try:
        response=client.list_buckets()
        return response
    except Exception as e:
        print(e)

def listObject(kc):
    response=client.list_objects(
        Bucket=f"{kc}",
        # MaxKeys=2
    )
    return response

# Delete Buckets
def deleteBucket(kc):
    try:
        response=client.delete_bucket(
            Bucket=f"{kc}"
        )
    except Exception as e:
        print(e)

# empty Buckets
def emptyBucket(kc,key):
    response=client.delete_objects(
        Bucket=f"{kc}",
        Delete={
            'Objects':[
                {
                    'Key':f"{key}"
                },
            ],
        }
    )

# static website hosting
def staticWebHost(kc):
    publicAccessBlock(kc)
    acl(kc)
    staticHost(kc)
    uploadFiles(kc)

# obj=listObject(kc)
# sizeO=0
# for i in obj['Contents']:
#     sizeO+=1
# for i in range(0,sizeO):
#     print(obj['Contents'][i]['Key'])