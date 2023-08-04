# RecoverHyperVVmStandaloneClusterSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the id of the parent source to recover the VMs. | 
**host** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the HyperV host where the recovered VMs will be attached. For standalone host targets, the host must be the same as the source. | 
**volume** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the datastore object where the VMs&#39; files should be recovered to. | 
**network_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the networking configuration to be applied to the recovered VMs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


