# RecoverKvmVmNewSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the resource (KVMH host) to which the restored VM will be attached | 
**data_center** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the datacenter where the VM&#39;s files should be restored to. | 
**source** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the id of the parent source to recover the VMs. | 
**storage_domain** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the Storage Domain where the VM&#39;s disk should be restored to. | 
**network_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the networking configuration to be applied to the recovered VMs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


