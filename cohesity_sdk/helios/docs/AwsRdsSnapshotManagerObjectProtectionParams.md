# AwsRdsSnapshotManagerObjectProtectionParams

Specifies the parameters which are specific to AWS Object Protection using AWS RDS snapshot orchestration with snapshot manager. Atlease one of tags or objects must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[AwsObjectLevelParams]**](AwsObjectLevelParams.md) | Specifies the objects to be protected. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.aws_rds_snapshot_manager_object_protection_params import AwsRdsSnapshotManagerObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRdsSnapshotManagerObjectProtectionParams from a JSON string
aws_rds_snapshot_manager_object_protection_params_instance = AwsRdsSnapshotManagerObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(AwsRdsSnapshotManagerObjectProtectionParams.to_json())

# convert the object into a dict
aws_rds_snapshot_manager_object_protection_params_dict = aws_rds_snapshot_manager_object_protection_params_instance.to_dict()
# create an instance of AwsRdsSnapshotManagerObjectProtectionParams from a dict
aws_rds_snapshot_manager_object_protection_params_from_dict = AwsRdsSnapshotManagerObjectProtectionParams.from_dict(aws_rds_snapshot_manager_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


