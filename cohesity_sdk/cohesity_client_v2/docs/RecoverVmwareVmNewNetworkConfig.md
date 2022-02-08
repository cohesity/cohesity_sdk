# RecoverVmwareVmNewNetworkConfig

Specifies the new network config parameters to be applied to VMware VMs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_port_group** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the network port group (i.e, either a standard switch port group or a distributed port group) that will attached to the recovered Object. This parameter is mandatory if detach network is specified as false. | [optional] 
**disable_network** | **bool, none_type** | Specifies whether the attached network should be left in disabled state. Default is false | [optional] 
**preserve_mac_address** | **bool, none_type** | If this is true and we are attaching to a new network entity, then the VM&#39;s MAC address will be preserved on the new network. Default value is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


