# RecoverVmwareVmVCDSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered for vCloudDirector sources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastores** | [**List[RecoveryObjectIdentifier]**](RecoveryObjectIdentifier.md) | Specifies the datastore objects where the object&#39;s files should be recovered to. This should only be specified if storageProfile is not specified. | [optional] 
**network_config** | [**RecoverVmwareVmNewSourceNetworkConfig**](RecoverVmwareVmNewSourceNetworkConfig.md) | Specifies the networking configuration to be applied to the recovered VMs. | [optional] 
**org_vdc_network** | [**OrgVDCNetwork**](OrgVDCNetwork.md) |  | [optional] 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the id of the parent source to recover the VMs. | 
**storage_profile** | [**VcdStorageProfileParams**](VcdStorageProfileParams.md) | Specifies the storage profile to which the objects should be recovered. This should only be specified if datastores are not specified. | [optional] 
**v_app** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the vApp object where the recovered objects will be attached. | [optional] 
**vdc** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the VDC object where the recovered objects will be attached. | 

## Example

```python
from cohesity_sdk.helios.models.recover_vmware_vm_vcd_source_config import RecoverVmwareVmVCDSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareVmVCDSourceConfig from a JSON string
recover_vmware_vm_vcd_source_config_instance = RecoverVmwareVmVCDSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareVmVCDSourceConfig.to_json())

# convert the object into a dict
recover_vmware_vm_vcd_source_config_dict = recover_vmware_vm_vcd_source_config_instance.to_dict()
# create an instance of RecoverVmwareVmVCDSourceConfig from a dict
recover_vmware_vm_vcd_source_config_from_dict = RecoverVmwareVmVCDSourceConfig.from_dict(recover_vmware_vm_vcd_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


