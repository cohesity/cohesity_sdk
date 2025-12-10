# RecoverAwsRdsMySqlNewSourceConfig

Specifies the new destination Source configuration where the RDS MySQL instances will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_rds_my_sql_new_source_config import RecoverAwsRdsMySqlNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsRdsMySqlNewSourceConfig from a JSON string
recover_aws_rds_my_sql_new_source_config_instance = RecoverAwsRdsMySqlNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsRdsMySqlNewSourceConfig.to_json())

# convert the object into a dict
recover_aws_rds_my_sql_new_source_config_dict = recover_aws_rds_my_sql_new_source_config_instance.to_dict()
# create an instance of RecoverAwsRdsMySqlNewSourceConfig from a dict
recover_aws_rds_my_sql_new_source_config_from_dict = RecoverAwsRdsMySqlNewSourceConfig.from_dict(recover_aws_rds_my_sql_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


