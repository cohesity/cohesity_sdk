# RecoverAwsVmNewSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption_config** | [**EncryptionConfig**](EncryptionConfig.md) | Specifies the encryption configuration. | [optional] 
**key_pair** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the pair of public and private key used to login into the VM | [optional] 
**network_config** | [**RecoverAwsVmNewSourceNetworkConfig**](RecoverAwsVmNewSourceNetworkConfig.md) | Specifies the networking configuration to be applied to the recovered VMs. | 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the AWS region in which to deploy the VM. | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the id of the parent source to recover the VMs. | 

## Example

```python
from cohesity_sdk.helios.models.recover_aws_vm_new_source_config import RecoverAwsVmNewSourceConfig

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


