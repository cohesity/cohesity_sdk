# AwsRdsPostgresDbProtectionGroupParams

Specifies the parameters which are specific to AWS RDS Postgres DB related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_rds_tag_ids** | **List[List[int]]** | Array of arrays of RDS Tag Ids that Specify db instances to Exclude. | [optional] 
**objects** | [**List[AwsPostgresDbProtectionGroupObjectParams]**](AwsPostgresDbProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**rds_tag_ids** | **List[List[int]]** | Array of arrays of RDS Tag Ids that Specify db instances to Protect. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.aws_rds_postgres_db_protection_group_params import AwsRdsPostgresDbProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRdsPostgresDbProtectionGroupParams from a JSON string
aws_rds_postgres_db_protection_group_params_instance = AwsRdsPostgresDbProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AwsRdsPostgresDbProtectionGroupParams.to_json())

# convert the object into a dict
aws_rds_postgres_db_protection_group_params_dict = aws_rds_postgres_db_protection_group_params_instance.to_dict()
# create an instance of AwsRdsPostgresDbProtectionGroupParams from a dict
aws_rds_postgres_db_protection_group_params_from_dict = AwsRdsPostgresDbProtectionGroupParams.from_dict(aws_rds_postgres_db_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


