# AzureEntraIDObjectProtectionParams

Specifies the parameters which are specific to Azure Entra ID Object Protection Groups using Azure native APIs. Atlease one of objects must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_object_types** | **[str], none_type** | Specifies the list of object types to be excluded from protection. | [optional] 
**objects** | [**[AzureObjectLevelParams]**](AzureObjectLevelParams.md) | Specifies the objects to be protected. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


