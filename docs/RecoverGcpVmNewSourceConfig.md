# RecoverGcpVmNewSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zone** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**network_config** | [**RecoverGcpVmNewSourceNetworkConfig**](RecoverGcpVmNewSourceNetworkConfig.md) |  | 
**project** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.models.recover_gcp_vm_new_source_config import RecoverGcpVmNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGcpVmNewSourceConfig from a JSON string
recover_gcp_vm_new_source_config_instance = RecoverGcpVmNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverGcpVmNewSourceConfig.to_json())

# convert the object into a dict
recover_gcp_vm_new_source_config_dict = recover_gcp_vm_new_source_config_instance.to_dict()
# create an instance of RecoverGcpVmNewSourceConfig from a dict
recover_gcp_vm_new_source_config_from_dict = RecoverGcpVmNewSourceConfig.from_dict(recover_gcp_vm_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


