# RecoverAcropolisVmNewSourceNetworkConfig

Specifies the network config parameters to applied for Acropolis VMs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detach_network** | **bool, none_type** | If this is set to true, then the network will be detached from the recovered VMs. All the other networking parameters set will be ignored if set to true. Default value is false. | [optional] 
**network_port_group** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the network port group (i.e, either a standard switch port group or a distributed port group) that will attached to the recovered Object. This parameter is mandatory if detach network is specified as false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


