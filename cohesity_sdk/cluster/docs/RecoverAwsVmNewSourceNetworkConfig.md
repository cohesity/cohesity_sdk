# RecoverAwsVmNewSourceNetworkConfig

Specifies the network config parameters to be applied for AWS VMs if recovering to new Source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**security_groups** | [**[RecoveryObjectIdentifier], none_type**](RecoveryObjectIdentifier.md) | Specifies the network security groups within above VPC. | 
**subnet** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the subnet within above VPC. | 
**vpc** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the Virtual Private Cloud to choose for the instance type. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


