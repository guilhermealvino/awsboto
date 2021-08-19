import boto3

#region = "us-west-2", , region_name=region
ec2_client = boto3.client('ec2')

#print(a)
def list_gp2_volume():
    filterVolum = ec2_client.describe_volumes(Filters=[{"Name": "volume-type", "Values": ["gp2"]}])
    ebslist = []

    for volume in filterVolum["Volumes"]:
        #print("Id dos ebs: " +volume['VolumeId'])
        ebslist.append(volume["VolumeId"])
        print("Tipo de disco: " +volume['VolumeType'] + " com volumeId " +volume['VolumeId'])

    return ebslist
print("\n")

#Alterar de gp2 para gp3
def modify_volume(ebsList):
    print("#"*5)
    try:
        for volume in ebsList:
              ec2_client.modify_volume(VolumeId = volume, VolumeType="gp3")
              print("Volume modificado: {}".format(volume))
    except boto3.exceptions.botocore.client.ClientError as e:
        print(e.response["Error"]["Message"].strip("\""))


if __name__ == "__main__":
    volumes = list_gp2_volume()
    modify_volume(volumes)