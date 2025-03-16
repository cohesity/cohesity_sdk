# RecoverVmwareVAppTemplateVCDSourceConfig

Specifies the new destination Source configuration where the vApp Templates will be recovered for vCloudDirector sources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog** | [**VdcCatalog**](VdcCatalog.md) | Specifies the catalog where the vApp template should reside. | 
**datastores** | [**List[RecoveryObjectIdentifier]**](RecoveryObjectIdentifier.md) | Specifies the datastore objects where the object&#39;s files should be recovered to. | [optional] 
**network_config** | [**RecoverVmwareVmNewSourceNetworkConfig**](RecoverVmwareVmNewSourceNetworkConfig.md) | Specifies the networking configuration to be applied to the recovered vApp templates. | [optional] 
**org_vdc_network** | [**OrgVDCNetwork**](OrgVDCNetwork.md) |  | [optional] 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the id of the parent source to recover the vApp templates. | 
**storage_profile** | [**VcdStorageProfileParams**](VcdStorageProfileParams.md) | Specifies the storage profile to which the objects should be recovered. This should only be specified if datastores are not specified. | [optional] 
**vdc** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the VDC object where the recovered objects will be attached. | 

## Example

```python
from cohesity_sdk.helios.models.recover_vmware_v_app_template_vcd_source_config import RecoverVmwareVAppTemplateVCDSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareVAppTemplateVCDSourceConfig from a JSON string
recover_vmware_v_app_template_vcd_source_config_instance = RecoverVmwareVAppTemplateVCDSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareVAppTemplateVCDSourceConfig.to_json())

# convert the object into a dict
recover_vmware_v_app_template_vcd_source_config_dict = recover_vmware_v_app_template_vcd_source_config_instance.to_dict()
# create an instance of RecoverVmwareVAppTemplateVCDSourceConfig from a dict
recover_vmware_v_app_template_vcd_source_config_from_dict = RecoverVmwareVAppTemplateVCDSourceConfig.from_dict(recover_vmware_v_app_template_vcd_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


