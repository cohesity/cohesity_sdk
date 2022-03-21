# RecoverVmwareVAppTemplateVCDSourceConfig

Specifies the new destination Source configuration where the vApp Templates will be recovered for vCloudDirector sources.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the id of the parent source to recover the vApp templates. | 
**vdc** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the VDC object where the recovered objects will be attached. | 
**catalog** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the catalog where the vApp template should reside. | 
**datastores** | [**[RecoveryObjectIdentifier], none_type**](RecoveryObjectIdentifier.md) | Specifies the datastore objects where the object&#39;s files should be recovered to. | [optional] 
**storage_profile** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the storage profile to which the objects should be recovered. This should only be specified if datastores are not specified. | [optional] 
**network_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the networking configuration to be applied to the recovered vApp templates. | [optional] 
**org_vdc_network** | [**OrgVDCNetwork**](OrgVDCNetwork.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


