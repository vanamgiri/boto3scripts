#!/usr/bin/env python
import sys
import boto3
ec2 = boto3.resource('ec2')
# get a list of all instances
all_instances = [i for i in ec2.instances.all()]
# get instances with filter of running + with tag `Name`
instances = [i for i in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}, {'Name':'tag:Test1', 'Values':['sad']}])]
# make a list of filtered instances IDs `[i.id for i in instances]`
# Filter from all instances the instance that are not in the filtered list
instances_to_delete = [to_del for to_del in all_instances if to_del.id not in [i.id for i in instances]]
for instances in instances_to_delete:
    instances.stop()
