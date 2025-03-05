# AwsSnapshotManagerObjectProtectionParams

Specifies the parameters which are specific to AWS Object Protection using AWS native snapshot orchestration with snapshot manager. Atlease one of tags or objects must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ami_creation_frequency** | **int** | The frequency of AMI creation. This should be set if the option to create AMI is set. A value of n creates an AMI from the snapshots after every n runs. eg. n &#x3D; 2 implies every alternate backup run starting from the first will create an AMI. | [optional] 
**create_ami** | **bool** | Specifies whether AMI should be created after taking snapshots of the instance. | [optional] 
**objects** | [**List[AwsObjectLevelParams]**](AwsObjectLevelParams.md) | Specifies the objects to be protected. | [optional] 
**volume_exclusion_params** | [**EbsVolumeExclusionParams**](EbsVolumeExclusionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.aws_snapshot_manager_object_protection_params import AwsSnapshotManagerObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsSnapshotManagerObjectProtectionParams from a JSON string
aws_snapshot_manager_object_protection_params_instance = AwsSnapshotManagerObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(AwsSnapshotManagerObjectProtectionParams.to_json())

# convert the object into a dict
aws_snapshot_manager_object_protection_params_dict = aws_snapshot_manager_object_protection_params_instance.to_dict()
# create an instance of AwsSnapshotManagerObjectProtectionParams from a dict
aws_snapshot_manager_object_protection_params_from_dict = AwsSnapshotManagerObjectProtectionParams.from_dict(aws_snapshot_manager_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


