# RecoverAwsAuroraNewSourceNetworkConfig

Specifies the network config parameters to be applied for AWS Aurora if recovering to new Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zone** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the entity representing the availability zone to use while restoring the DB. | [optional] 
**security_groups** | [**List[RecoveryObjectIdentifier]**](RecoveryObjectIdentifier.md) | Specifies the network security groups within above VPC. | [optional] 
**subnet** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the subnet within above VPC. | 
**vpc** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the Virtual Private Cloud to choose for the instance type. | 

## Example

```python
from cohesity_sdk.helios.models.recover_aws_aurora_new_source_network_config import RecoverAwsAuroraNewSourceNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsAuroraNewSourceNetworkConfig from a JSON string
recover_aws_aurora_new_source_network_config_instance = RecoverAwsAuroraNewSourceNetworkConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsAuroraNewSourceNetworkConfig.to_json())

# convert the object into a dict
recover_aws_aurora_new_source_network_config_dict = recover_aws_aurora_new_source_network_config_instance.to_dict()
# create an instance of RecoverAwsAuroraNewSourceNetworkConfig from a dict
recover_aws_aurora_new_source_network_config_from_dict = RecoverAwsAuroraNewSourceNetworkConfig.from_dict(recover_aws_aurora_new_source_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


