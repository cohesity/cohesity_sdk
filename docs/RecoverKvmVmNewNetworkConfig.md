# RecoverKvmVmNewNetworkConfig

Specifies the network config parameters to be applied for KVM VMs if recovering to a new source with a new network.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_port_group** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the network port group (i.e, either a standard switch port group or a distributed port group) that will attached to the recovered Object. This parameter is mandatory if detach network is specified as false. | [optional] 
**vnic_profile** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies VNic profile that will be attached to the restored object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


