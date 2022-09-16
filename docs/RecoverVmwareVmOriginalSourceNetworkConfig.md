# RecoverVmwareVmOriginalSourceNetworkConfig

Specifies the network config parameters to be applied for VMware VMs if recovering to original Source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detach_network** | **bool, none_type** | If this is set to true, then the network will be detached from the recovered VMs. All the other networking parameters set will be ignored if set to true. Default value is false. | [optional] 
**disable_network** | **bool, none_type** | Specifies whether the attached network should be left in disabled state. Default is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


