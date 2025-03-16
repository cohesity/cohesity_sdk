# AwsSnapshotManagerProtectionGroupObjectParams

Specifies the object parameters to create AWS Snapshot Manager Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the virtual machine. | [optional] [readonly] 
**volume_exclusion_params** | [**EbsVolumeExclusionParams**](EbsVolumeExclusionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.aws_snapshot_manager_protection_group_object_params import AwsSnapshotManagerProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsSnapshotManagerProtectionGroupObjectParams from a JSON string
aws_snapshot_manager_protection_group_object_params_instance = AwsSnapshotManagerProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AwsSnapshotManagerProtectionGroupObjectParams.to_json())

# convert the object into a dict
aws_snapshot_manager_protection_group_object_params_dict = aws_snapshot_manager_protection_group_object_params_instance.to_dict()
# create an instance of AwsSnapshotManagerProtectionGroupObjectParams from a dict
aws_snapshot_manager_protection_group_object_params_from_dict = AwsSnapshotManagerProtectionGroupObjectParams.from_dict(aws_snapshot_manager_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


