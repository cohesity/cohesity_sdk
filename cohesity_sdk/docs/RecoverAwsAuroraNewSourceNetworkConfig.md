# RecoverAwsAuroraNewSourceNetworkConfig

Specifies the network config parameters to be applied for AWS Aurora if recovering to new Source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnet** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**vpc** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**availability_zone** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**security_groups** | [**[RecoveryObjectIdentifier], none_type**](RecoveryObjectIdentifier.md) | Specifies the network security groups within above VPC. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


