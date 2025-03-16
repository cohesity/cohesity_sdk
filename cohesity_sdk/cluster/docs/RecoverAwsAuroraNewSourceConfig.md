# RecoverAwsAuroraNewSourceConfig

Specifies the new destination Source configuration where the Aurora instances will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_config** | [**RecoverAwsAuroraNewSourceNetworkConfig**](RecoverAwsAuroraNewSourceNetworkConfig.md) |  | 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_aurora_new_source_config import RecoverAwsAuroraNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsAuroraNewSourceConfig from a JSON string
recover_aws_aurora_new_source_config_instance = RecoverAwsAuroraNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsAuroraNewSourceConfig.to_json())

# convert the object into a dict
recover_aws_aurora_new_source_config_dict = recover_aws_aurora_new_source_config_instance.to_dict()
# create an instance of RecoverAwsAuroraNewSourceConfig from a dict
recover_aws_aurora_new_source_config_from_dict = RecoverAwsAuroraNewSourceConfig.from_dict(recover_aws_aurora_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


