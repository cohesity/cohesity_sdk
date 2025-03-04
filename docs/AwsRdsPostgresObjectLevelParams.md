# AwsRdsPostgresObjectLevelParams

Specifies the object parameters to create an AWS RDS Postgres Ingest Object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the database. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.aws_rds_postgres_object_level_params import AwsRdsPostgresObjectLevelParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRdsPostgresObjectLevelParams from a JSON string
aws_rds_postgres_object_level_params_instance = AwsRdsPostgresObjectLevelParams.from_json(json)
# print the JSON string representation of the object
print(AwsRdsPostgresObjectLevelParams.to_json())

# convert the object into a dict
aws_rds_postgres_object_level_params_dict = aws_rds_postgres_object_level_params_instance.to_dict()
# create an instance of AwsRdsPostgresObjectLevelParams from a dict
aws_rds_postgres_object_level_params_from_dict = AwsRdsPostgresObjectLevelParams.from_dict(aws_rds_postgres_object_level_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


