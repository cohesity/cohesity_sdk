# RecoverAwsVmNewSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption_config** | [**EncryptionConfig**](EncryptionConfig.md) |  | [optional] 
**key_pair** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**network_config** | [**RecoverAwsVmNewSourceNetworkConfig**](RecoverAwsVmNewSourceNetworkConfig.md) |  | 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_vm_new_source_config import RecoverAwsVmNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsVmNewSourceConfig from a JSON string
recover_aws_vm_new_source_config_instance = RecoverAwsVmNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsVmNewSourceConfig.to_json())

# convert the object into a dict
recover_aws_vm_new_source_config_dict = recover_aws_vm_new_source_config_instance.to_dict()
# create an instance of RecoverAwsVmNewSourceConfig from a dict
recover_aws_vm_new_source_config_from_dict = RecoverAwsVmNewSourceConfig.from_dict(recover_aws_vm_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


