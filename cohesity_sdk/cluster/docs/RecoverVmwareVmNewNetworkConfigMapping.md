# RecoverVmwareVmNewNetworkConfigMapping

Specifies source VMs NIC to target network mapping for the VMware VMs being recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_network** | **bool, none_type** | Specifies whether the attached network should be left in disabled state for this mapping. Default is false. | [optional] 
**network_adapter_name** | **str, none_type** | Name of the VM&#39;s network adapter name. | [optional] 
**org_vdc_network** | [**OrgVDCNetwork**](OrgVDCNetwork.md) |  | [optional] 
**preserve_mac_address** | **bool, none_type** | Specifies whether to preserve the MAC address of the source network entity while attaching to the new target network. Default is false. | [optional] 
**source_network_entity** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**target_network_entity** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


