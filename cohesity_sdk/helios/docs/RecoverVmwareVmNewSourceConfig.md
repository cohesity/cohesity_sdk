# RecoverVmwareVmNewSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | **str** | Specifies the type of VMware source to which the VMs are being restored. | 
**standalone_host_params** | [**RecoverVmwareVmEsxiSourceConfig**](RecoverVmwareVmEsxiSourceConfig.md) |  | [optional] 
**v_center_params** | [**RecoverVmwareVmVCenterSourceConfig**](RecoverVmwareVmVCenterSourceConfig.md) |  | [optional] 
**v_cloud_director_params** | [**RecoverVmwareVmVCDSourceConfig**](RecoverVmwareVmVCDSourceConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_vmware_vm_new_source_config import RecoverVmwareVmNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareVmNewSourceConfig from a JSON string
recover_vmware_vm_new_source_config_instance = RecoverVmwareVmNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareVmNewSourceConfig.to_json())

# convert the object into a dict
recover_vmware_vm_new_source_config_dict = recover_vmware_vm_new_source_config_instance.to_dict()
# create an instance of RecoverVmwareVmNewSourceConfig from a dict
recover_vmware_vm_new_source_config_from_dict = RecoverVmwareVmNewSourceConfig.from_dict(recover_vmware_vm_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


