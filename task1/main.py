import taskfile as tf

kc=tf.kc

list=tf.listBuckets()
# print(list['Buckets'][0]['Name'])
size=0
flag=0
for i in list['Buckets']:
    size+=1
# print(size)
for i in range(0,size):
    if kc==list['Buckets'][i]['Name']:
        flag=1
        # deleteBucket(kc)
        # print("deleting...")
    # else:
        # flag=1
        # createBucket(kc)
        # print("creating...")
print(flag)
if flag==1:
    obj=tf.listObject(kc)
    sizeO=0
    for i in obj['Contents']:
        sizeO+=1
    for i in range(0,sizeO):
        key=obj['Contents'][i]['Key']
        tf.emptyBucket(kc,key)
    print("Emptying Bucket...")
    print("deleting bucket....")
    tf.deleteBucket(kc)
    print("creating bucket....")
    tf.createBucket(kc)
    tf.staticWebHost(kc)
else:
    print("creating bucket....")
    tf.createBucket(kc)
    tf.staticWebHost(kc)