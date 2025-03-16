# AwsRdsPostgresProtectionParams

Specifies the parameters which are specific to AWS RDS Postgres related Object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[AwsRdsPostgresObjectLevelParams]**](AwsRdsPostgresObjectLevelParams.md) | Specifies the objects to be protected. | [optional] 
**source_id** | **int** | Specifies the id of the source of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.aws_rds_postgres_protection_params import AwsRdsPostgresProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRdsPostgresProtectionParams from a JSON string
aws_rds_postgres_protection_params_instance = AwsRdsPostgresProtectionParams.from_json(json)
# print the JSON string representation of the object
print(AwsRdsPostgresProtectionParams.to_json())

# convert the object into a dict
aws_rds_postgres_protection_params_dict = aws_rds_postgres_protection_params_instance.to_dict()
# create an instance of AwsRdsPostgresProtectionParams from a dict
aws_rds_postgres_protection_params_from_dict = AwsRdsPostgresProtectionParams.from_dict(aws_rds_postgres_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


