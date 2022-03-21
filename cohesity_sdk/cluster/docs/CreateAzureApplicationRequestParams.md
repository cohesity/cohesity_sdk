# CreateAzureApplicationRequestParams

Specifies the request parameters for creating Azure Applications

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str, none_type** | Specifies the access token for Azure PowerShell Application access. | 
**username** | **str, none_type** | Specifies the username to access Microsoft365 source. | 
**app_count** | **int** | Specifies the count of Azure application to be created. | 
**microsoft365_region** | **str, none_type** | Specifies the region where Office 365 Exchange environment is. | [optional] 
**existing_microsoft365_app_credentials_list** | [**[Office365AppCredentials]**](Office365AppCredentials.md) | Specifies a list of Microsoft365 azure application credentials already added within the Microsoft365 source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


