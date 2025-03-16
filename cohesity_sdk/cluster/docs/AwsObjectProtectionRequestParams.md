# AwsObjectProtectionRequestParams

Specifies the parameters which are specific to AWS related Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_type** | **str** | Specifies the AWS Protection Job type. | [optional] 
**aurora_snapshot_manager_protection_type_params** | [**AwsAuroraSnapshotManagerObjectProtectionParams**](AwsAuroraSnapshotManagerObjectProtectionParams.md) |  | [optional] 
**native_protection_type_params** | [**AwsNativeObjectProtectionParams**](AwsNativeObjectProtectionParams.md) |  | [optional] 
**rds_postgres_protection_type_params** | [**AwsRdsPostgresProtectionParams**](AwsRdsPostgresProtectionParams.md) |  | [optional] 
**rds_snapshot_manager_protection_type_params** | [**AwsRdsSnapshotManagerObjectProtectionParams**](AwsRdsSnapshotManagerObjectProtectionParams.md) |  | [optional] 
**s3_protection_type_params** | [**AwsS3ProtectionParams**](AwsS3ProtectionParams.md) |  | [optional] 
**snapshot_manager_protection_type_params** | [**AwsSnapshotManagerObjectProtectionParams**](AwsSnapshotManagerObjectProtectionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_object_protection_request_params import AwsObjectProtectionRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsObjectProtectionRequestParams from a JSON string
aws_object_protection_request_params_instance = AwsObjectProtectionRequestParams.from_json(json)
# print the JSON string representation of the object
print(AwsObjectProtectionRequestParams.to_json())

# convert the object into a dict
aws_object_protection_request_params_dict = aws_object_protection_request_params_instance.to_dict()
# create an instance of AwsObjectProtectionRequestParams from a dict
aws_object_protection_request_params_from_dict = AwsObjectProtectionRequestParams.from_dict(aws_object_protection_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


