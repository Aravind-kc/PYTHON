import boto3
ec2 = boto3.client('ec2', region_name = 'ap-south-1')
# create_instance = ec2.run_instances(
#     InstanceType = 't2.micro',
#     ImageId = 'ami-05295b6e6c790593e',
#     KeyName = 'ara1',
#     MaxCount = 1,
#     MinCount = 1)
# print(create_instance)
    
    #stop instance

# list_instances = ec2.stop_instances(InstanceIds=['i-09e377f18fdeb814f'])
# print(list_instances)

  #terminate insatnce

# list_instances = ec2.terminate_instances(InstanceIds=['i-09e377f18fdeb814f'])
# print(list_instances)
