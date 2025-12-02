# AwsRdsMsSqlProtectionGroupParams

Specifies the parameters which are specific to AWS RDS MS SQL related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_auto_create** | **bool** | Specifies whether to auto create the Cloud Storage bucket if it does not exist. | [optional] 
**cloud_storage_bucket_name** | **str** | The Cloud Storage bucket name for MS SQL database backup. | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_rds_tag_ids** | **List[List[int]]** | Array of arrays of RDS Tag Ids that Specify db instances to Exclude. | [optional] 
**objects** | [**List[AwsRdsMsSqlProtectionGroupObjectParams]**](AwsRdsMsSqlProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**rds_tag_ids** | **List[List[int]]** | Array of arrays of RDS Tag Ids that Specify db instances to Protect. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.aws_rds_ms_sql_protection_group_params import AwsRdsMsSqlProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRdsMsSqlProtectionGroupParams from a JSON string
aws_rds_ms_sql_protection_group_params_instance = AwsRdsMsSqlProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AwsRdsMsSqlProtectionGroupParams.to_json())

# convert the object into a dict
aws_rds_ms_sql_protection_group_params_dict = aws_rds_ms_sql_protection_group_params_instance.to_dict()
# create an instance of AwsRdsMsSqlProtectionGroupParams from a dict
aws_rds_ms_sql_protection_group_params_from_dict = AwsRdsMsSqlProtectionGroupParams.from_dict(aws_rds_ms_sql_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


