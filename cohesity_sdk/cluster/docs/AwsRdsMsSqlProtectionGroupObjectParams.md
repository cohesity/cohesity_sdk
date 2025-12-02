# AwsRdsMsSqlProtectionGroupObjectParams

Specifies the object parameters to create an AWS RDS MS SQL Ingest Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the database instance. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.aws_rds_ms_sql_protection_group_object_params import AwsRdsMsSqlProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRdsMsSqlProtectionGroupObjectParams from a JSON string
aws_rds_ms_sql_protection_group_object_params_instance = AwsRdsMsSqlProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AwsRdsMsSqlProtectionGroupObjectParams.to_json())

# convert the object into a dict
aws_rds_ms_sql_protection_group_object_params_dict = aws_rds_ms_sql_protection_group_object_params_instance.to_dict()
# create an instance of AwsRdsMsSqlProtectionGroupObjectParams from a dict
aws_rds_ms_sql_protection_group_object_params_from_dict = AwsRdsMsSqlProtectionGroupObjectParams.from_dict(aws_rds_ms_sql_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


