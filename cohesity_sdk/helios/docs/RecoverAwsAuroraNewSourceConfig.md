# RecoverAwsAuroraNewSourceConfig

Specifies the new destination Source configuration where the Aurora instances will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_config** | [**RecoverAwsAuroraNewSourceNetworkConfig**](RecoverAwsAuroraNewSourceNetworkConfig.md) | Specifies the networking configuration to be applied to the recovered VMs. | 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the AWS region in which to deploy the Aurora instance. | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the id of the parent source to recover the Aurora. | 

## Example

```python
from cohesity_sdk.helios.models.recover_aws_aurora_new_source_config import RecoverAwsAuroraNewSourceConfig

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


