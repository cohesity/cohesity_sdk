# RecoverVmwareVmNewNetworkConfig

Specifies the new network config parameters to be applied to VMware VMs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_network** | **bool, none_type** | Specifies whether the attached network should be left in disabled state. Default is false | [optional] 
**mappings** | [**[RecoverVmwareVmNewNetworkConfigMapping], none_type**](RecoverVmwareVmNewNetworkConfigMapping.md) | Specifies the target network mapping for each VM&#39;s network adapter. | [optional] 
**network_port_group** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**preserve_mac_address** | **bool, none_type** | If this is true and we are attaching to a new network entity, then the VM&#39;s MAC address will be preserved on the new network. Default value is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


