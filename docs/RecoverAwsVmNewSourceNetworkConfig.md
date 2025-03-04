# RecoverAwsVmNewSourceNetworkConfig

Specifies the network config parameters to be applied for AWS VMs if recovering to new Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**security_groups** | [**List[RecoveryObjectIdentifier]**](RecoveryObjectIdentifier.md) | Specifies the network security groups within above VPC. | 
**subnet** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**vpc** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.models.recover_aws_vm_new_source_network_config import RecoverAwsVmNewSourceNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsVmNewSourceNetworkConfig from a JSON string
recover_aws_vm_new_source_network_config_instance = RecoverAwsVmNewSourceNetworkConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsVmNewSourceNetworkConfig.to_json())

# convert the object into a dict
recover_aws_vm_new_source_network_config_dict = recover_aws_vm_new_source_network_config_instance.to_dict()
# create an instance of RecoverAwsVmNewSourceNetworkConfig from a dict
recover_aws_vm_new_source_network_config_from_dict = RecoverAwsVmNewSourceNetworkConfig.from_dict(recover_aws_vm_new_source_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


