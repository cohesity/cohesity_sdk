# RecoverVmwareVmVCenterSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered for vCenter sources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastores** | [**List[RecoveryObjectIdentifier]**](RecoveryObjectIdentifier.md) | Specifies the datastore objects where the object&#39;s files should be recovered to. | 
**network_config** | [**RecoverVmwareVmNewSourceNetworkConfig**](RecoverVmwareVmNewSourceNetworkConfig.md) |  | [optional] 
**resource_pool** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**vm_folder** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_vmware_vm_v_center_source_config import RecoverVmwareVmVCenterSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareVmVCenterSourceConfig from a JSON string
recover_vmware_vm_v_center_source_config_instance = RecoverVmwareVmVCenterSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareVmVCenterSourceConfig.to_json())

# convert the object into a dict
recover_vmware_vm_v_center_source_config_dict = recover_vmware_vm_v_center_source_config_instance.to_dict()
# create an instance of RecoverVmwareVmVCenterSourceConfig from a dict
recover_vmware_vm_v_center_source_config_from_dict = RecoverVmwareVmVCenterSourceConfig.from_dict(recover_vmware_vm_v_center_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


