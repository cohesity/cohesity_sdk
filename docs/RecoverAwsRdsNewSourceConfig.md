# RecoverAwsRdsNewSourceConfig

Specifies the new destination Source configuration where the RDS instances will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_config** | [**RecoverAwsRdsNewSourceNetworkConfig**](RecoverAwsRdsNewSourceNetworkConfig.md) |  | 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_rds_new_source_config import RecoverAwsRdsNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsRdsNewSourceConfig from a JSON string
recover_aws_rds_new_source_config_instance = RecoverAwsRdsNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsRdsNewSourceConfig.to_json())

# convert the object into a dict
recover_aws_rds_new_source_config_dict = recover_aws_rds_new_source_config_instance.to_dict()
# create an instance of RecoverAwsRdsNewSourceConfig from a dict
recover_aws_rds_new_source_config_from_dict = RecoverAwsRdsNewSourceConfig.from_dict(recover_aws_rds_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


