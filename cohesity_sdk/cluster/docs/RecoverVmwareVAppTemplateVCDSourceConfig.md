# RecoverVmwareVAppTemplateVCDSourceConfig

Specifies the new destination Source configuration where the vApp Templates will be recovered for vCloudDirector sources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog** | [**VdcCatalog**](VdcCatalog.md) |  | 
**datastores** | [**List[RecoveryObjectIdentifier]**](RecoveryObjectIdentifier.md) | Specifies the datastore objects where the object&#39;s files should be recovered to. | [optional] 
**network_config** | [**RecoverVmwareVmNewSourceNetworkConfig**](RecoverVmwareVmNewSourceNetworkConfig.md) |  | [optional] 
**org_vdc_network** | [**OrgVDCNetwork**](OrgVDCNetwork.md) |  | [optional] 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**storage_profile** | [**VcdStorageProfileParams**](VcdStorageProfileParams.md) |  | [optional] 
**vdc** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_vmware_v_app_template_vcd_source_config import RecoverVmwareVAppTemplateVCDSourceConfig

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


