# RecoverVmwareVAppVCDSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered for vCloudDirector sources.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the id of the parent source to recover the VMs. | 
**vdc** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the VDC object where the recovered objects will be attached. | 
**datastores** | [**[RecoveryObjectIdentifier], none_type**](RecoveryObjectIdentifier.md) | Specifies the datastore objects where the object&#39;s files should be recovered to. | [optional] 
**network_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the networking configuration to be applied to the recovered VMs. | [optional] 
**org_vdc_network** | [**OrgVDCNetwork**](OrgVDCNetwork.md) |  | [optional] 
**storage_profile** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the storage profile to which the objects should be recovered. This should only be specified if datastores are not specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


