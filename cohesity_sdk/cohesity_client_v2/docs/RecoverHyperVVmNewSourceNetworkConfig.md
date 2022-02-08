# RecoverHyperVVmNewSourceNetworkConfig

Specifies the network config parameters to be applied for HyperV VMs if recovering to new Source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detach_network** | **bool, none_type** | If this is set to true, then the network will be detached from the recovered VMs. All the other networking parameters set will be ignored if set to true. Default value is false. | [optional] 
**virtual_switch** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the virtual switch that will attached to all the network interfaces of the VMs being recovered. This parameter is mandatory if detach network is specified as false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


