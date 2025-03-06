# RecoverAwsRdsNewSourceNetworkConfig

Specifies the network config parameters to be applied for AWS RDS if recovering to new Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zone** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**security_groups** | [**List[RecoveryObjectIdentifier]**](RecoveryObjectIdentifier.md) | Specifies the network security groups within above VPC. | [optional] 
**subnet** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**vpc** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_rds_new_source_network_config import RecoverAwsRdsNewSourceNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsRdsNewSourceNetworkConfig from a JSON string
recover_aws_rds_new_source_network_config_instance = RecoverAwsRdsNewSourceNetworkConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsRdsNewSourceNetworkConfig.to_json())

# convert the object into a dict
recover_aws_rds_new_source_network_config_dict = recover_aws_rds_new_source_network_config_instance.to_dict()
# create an instance of RecoverAwsRdsNewSourceNetworkConfig from a dict
recover_aws_rds_new_source_network_config_from_dict = RecoverAwsRdsNewSourceNetworkConfig.from_dict(recover_aws_rds_new_source_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


