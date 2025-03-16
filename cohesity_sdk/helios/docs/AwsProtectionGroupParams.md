# AwsProtectionGroupParams

Specifies the parameters which are specific to AWS related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_protection_type_params** | [**AwsAgentProtectionGroupParams**](AwsAgentProtectionGroupParams.md) |  | [optional] 
**aurora_protection_type_params** | [**AwsAuroraProtectionGroupParams**](AwsAuroraProtectionGroupParams.md) |  | [optional] 
**native_protection_type_params** | [**AwsNativeProtectionGroupParams**](AwsNativeProtectionGroupParams.md) |  | [optional] 
**protection_type** | **str** | Specifies the AWS Protection Group type. | 
**rds_postgres_protection_type_params** | [**AwsRdsPostgresProtectionGroupParams**](AwsRdsPostgresProtectionGroupParams.md) |  | [optional] 
**rds_protection_type_params** | [**AwsRdsProtectionGroupParams**](AwsRdsProtectionGroupParams.md) |  | [optional] 
**s3_protection_type_params** | [**AwsS3ProtectionGroupParams**](AwsS3ProtectionGroupParams.md) |  | [optional] 
**snapshot_manager_protection_type_params** | [**AwsSnapshotManagerProtectionGroupParams**](AwsSnapshotManagerProtectionGroupParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.aws_protection_group_params import AwsProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsProtectionGroupParams from a JSON string
aws_protection_group_params_instance = AwsProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AwsProtectionGroupParams.to_json())

# convert the object into a dict
aws_protection_group_params_dict = aws_protection_group_params_instance.to_dict()
# create an instance of AwsProtectionGroupParams from a dict
aws_protection_group_params_from_dict = AwsProtectionGroupParams.from_dict(aws_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


