# RecoverRDSPostgresParams

Specifies the parameters to recover RDS Postgres.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_target_params** | [**AwsTargetParamsForRecoverRDSPostgres**](AwsTargetParamsForRecoverRDSPostgres.md) | Specifies the params for recovering to an Aws target. | [optional] 
**overwrite_database** | **bool** | Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object. | [optional] 
**prefix** | **str** | Specifies the prefix to be prepended to the object name after the recovery. | [optional] 
**suffix** | **str** | Specifies the suffix to be appended to the object name after the recovery. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.helios.models.recover_rds_postgres_params import RecoverRDSPostgresParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverRDSPostgresParams from a JSON string
recover_rds_postgres_params_instance = RecoverRDSPostgresParams.from_json(json)
# print the JSON string representation of the object
print(RecoverRDSPostgresParams.to_json())

# convert the object into a dict
recover_rds_postgres_params_dict = recover_rds_postgres_params_instance.to_dict()
# create an instance of RecoverRDSPostgresParams from a dict
recover_rds_postgres_params_from_dict = RecoverRDSPostgresParams.from_dict(recover_rds_postgres_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


