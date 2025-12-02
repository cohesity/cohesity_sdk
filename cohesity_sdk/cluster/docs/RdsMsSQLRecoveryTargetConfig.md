# RdsMsSQLRecoveryTargetConfig

Specifies the target object parameters to recover AWS RDS MS SQL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_auto_create** | **bool** | Specifies whether to auto create the Cloud Storage bucket if it does not exist. | [optional] 
**cloud_storage_bucket_name** | **str** | The Cloud Storage bucket name for MS SQL database recovery. | [optional] 
**new_source_config** | [**RecoverRdsMsSQLNewSourceConfig**](RecoverRdsMsSQLNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 

## Example

```python
from cohesity_sdk.cluster.models.rds_ms_sql_recovery_target_config import RdsMsSQLRecoveryTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RdsMsSQLRecoveryTargetConfig from a JSON string
rds_ms_sql_recovery_target_config_instance = RdsMsSQLRecoveryTargetConfig.from_json(json)
# print the JSON string representation of the object
print(RdsMsSQLRecoveryTargetConfig.to_json())

# convert the object into a dict
rds_ms_sql_recovery_target_config_dict = rds_ms_sql_recovery_target_config_instance.to_dict()
# create an instance of RdsMsSQLRecoveryTargetConfig from a dict
rds_ms_sql_recovery_target_config_from_dict = RdsMsSQLRecoveryTargetConfig.from_dict(rds_ms_sql_recovery_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


