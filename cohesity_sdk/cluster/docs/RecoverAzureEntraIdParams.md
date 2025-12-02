# RecoverAzureEntraIdParams

Specifies the parameters to recover Azure Entra ID.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_attributes** | [**[RecoverAzureEntraIdObjectParams], none_type**](RecoverAzureEntraIdObjectParams.md) | Specifies the details of the azure entra id objects attributes to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kAzure"
**azure_target_params** | [**AzureTargetParamsForRecoverAzureEntraId**](AzureTargetParamsForRecoverAzureEntraId.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


