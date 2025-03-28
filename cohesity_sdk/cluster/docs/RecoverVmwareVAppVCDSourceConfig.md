# RecoverVmwareVAppVCDSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered for vCloudDirector sources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastores** | [**List[RecoveryObjectIdentifier]**](RecoveryObjectIdentifier.md) | Specifies the datastore objects where the object&#39;s files should be recovered to. | [optional] 
**network_config** | [**RecoverVmwareVmNewSourceNetworkConfig**](RecoverVmwareVmNewSourceNetworkConfig.md) |  | [optional] 
**org_vdc_network** | [**OrgVDCNetwork**](OrgVDCNetwork.md) |  | [optional] 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**storage_profile** | [**VcdStorageProfileParams**](VcdStorageProfileParams.md) |  | [optional] 
**vdc** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_vmware_v_app_vcd_source_config import RecoverVmwareVAppVCDSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareVAppVCDSourceConfig from a JSON string
recover_vmware_v_app_vcd_source_config_instance = RecoverVmwareVAppVCDSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareVAppVCDSourceConfig.to_json())

# convert the object into a dict
recover_vmware_v_app_vcd_source_config_dict = recover_vmware_v_app_vcd_source_config_instance.to_dict()
# create an instance of RecoverVmwareVAppVCDSourceConfig from a dict
recover_vmware_v_app_vcd_source_config_from_dict = RecoverVmwareVAppVCDSourceConfig.from_dict(recover_vmware_v_app_vcd_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


