# RecoverKvmVmNewSourceNetworkConfig

Specifies the network config parameters to be applied for KVM VMs if recovering to new Source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detach_network** | **bool, none_type** | If this is set to true, then the network will be detached from the recovered VMs. All the other networking parameters set will be ignored if set to true. Default value is false. | [optional] 
**new_network_config** | [**RecoverKvmVmNewNetworkConfig**](RecoverKvmVmNewNetworkConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


