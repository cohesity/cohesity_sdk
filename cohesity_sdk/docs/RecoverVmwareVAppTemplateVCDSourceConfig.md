# RecoverVmwareVAppTemplateVCDSourceConfig

Specifies the new destination Source configuration where the vApp Templates will be recovered for vCloudDirector sources.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog** | [**VdcCatalog**](VdcCatalog.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**vdc** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**datastores** | [**[RecoveryObjectIdentifier], none_type**](RecoveryObjectIdentifier.md) | Specifies the datastore objects where the object&#39;s files should be recovered to. | [optional] 
**network_config** | [**RecoverVmwareVmNewSourceNetworkConfig**](RecoverVmwareVmNewSourceNetworkConfig.md) |  | [optional] 
**org_vdc_network** | [**OrgVDCNetwork**](OrgVDCNetwork.md) |  | [optional] 
**storage_profile** | [**VcdStorageProfileParams**](VcdStorageProfileParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


