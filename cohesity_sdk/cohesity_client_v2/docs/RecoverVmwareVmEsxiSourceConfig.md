# RecoverVmwareVmEsxiSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered for ESXi sources.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the id of the parent source to recover the VMs. | 
**resource_pool** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the resource pool object where the recovered objects will be attached. | 
**datastores** | [**[RecoveryObjectIdentifier], none_type**](RecoveryObjectIdentifier.md) | Specifies the datastore objects where the object&#39;s files should be recovered to. | [optional] 
**vm_folder** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Folder where the VMs should be created. | [optional] 
**network_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the networking configuration to be applied to the recovered VMs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


