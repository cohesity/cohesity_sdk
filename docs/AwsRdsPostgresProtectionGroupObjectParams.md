# AwsRdsPostgresProtectionGroupObjectParams

Specifies the object parameters to create an AWS RDS Postgres Ingest Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the database. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.aws_rds_postgres_protection_group_object_params import AwsRdsPostgresProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRdsPostgresProtectionGroupObjectParams from a JSON string
aws_rds_postgres_protection_group_object_params_instance = AwsRdsPostgresProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AwsRdsPostgresProtectionGroupObjectParams.to_json())

# convert the object into a dict
aws_rds_postgres_protection_group_object_params_dict = aws_rds_postgres_protection_group_object_params_instance.to_dict()
# create an instance of AwsRdsPostgresProtectionGroupObjectParams from a dict
aws_rds_postgres_protection_group_object_params_from_dict = AwsRdsPostgresProtectionGroupObjectParams.from_dict(aws_rds_postgres_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


