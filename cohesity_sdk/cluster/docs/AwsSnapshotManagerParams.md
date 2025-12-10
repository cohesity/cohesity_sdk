# AwsSnapshotManagerParams

Specifies job parameters applicable for all 'kVMware' Environment type Protection Sources in a Protection Job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ami_creation_frequency** | **int** | Specifies the frequency of AMI creation. This should be set if the option to create AMI is set. A value of n creates an AMI from the snapshots after every n runs. eg. n &#x3D; 2 implies every alternate backup run starting from the first will create an AMI. | [optional] 
**create_ami** | **bool** | If true, creates an AMI after taking snapshots of the instance. It should be set only while backing up EC2 instances. CreateAmi creates AMI for the protection job. | [optional] 
**volume_exclusion_params** | [**EbsVolumeExclusionParams**](EbsVolumeExclusionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_snapshot_manager_params import AwsSnapshotManagerParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsSnapshotManagerParams from a JSON string
aws_snapshot_manager_params_instance = AwsSnapshotManagerParams.from_json(json)
# print the JSON string representation of the object
print(AwsSnapshotManagerParams.to_json())

# convert the object into a dict
aws_snapshot_manager_params_dict = aws_snapshot_manager_params_instance.to_dict()
# create an instance of AwsSnapshotManagerParams from a dict
aws_snapshot_manager_params_from_dict = AwsSnapshotManagerParams.from_dict(aws_snapshot_manager_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


