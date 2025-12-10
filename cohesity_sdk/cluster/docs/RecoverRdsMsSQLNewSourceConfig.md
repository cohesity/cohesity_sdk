# RecoverRdsMsSQLNewSourceConfig

Specifies the new destination Source configuration where the MS SQL clusters will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_rds_ms_sql_new_source_config import RecoverRdsMsSQLNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverRdsMsSQLNewSourceConfig from a JSON string
recover_rds_ms_sql_new_source_config_instance = RecoverRdsMsSQLNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverRdsMsSQLNewSourceConfig.to_json())

# convert the object into a dict
recover_rds_ms_sql_new_source_config_dict = recover_rds_ms_sql_new_source_config_instance.to_dict()
# create an instance of RecoverRdsMsSQLNewSourceConfig from a dict
recover_rds_ms_sql_new_source_config_from_dict = RecoverRdsMsSQLNewSourceConfig.from_dict(recover_rds_ms_sql_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


