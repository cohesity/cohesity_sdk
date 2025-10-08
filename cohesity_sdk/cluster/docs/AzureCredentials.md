# AzureCredentials

Specifies the object to Azure related credentials.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | Specifies the type of authentication being used in the request. | 
**username** | **str** | Specifies the username to access target entity. | 
**managed_identity_client_id** | **str, none_type** | Specifies the Managed Identity&#39;s client id associated with the Virtual Machine using which actions can be performed. It&#39;s applicable only when user selects User Managed Identity auth method. | [optional] 
**password** | **str, none_type** | Specifies the password to access target entity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


