# DeleteAzureApplicationRequestParams

Specifies the request parameters for deleting Azure Applications.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str, none_type** | Specifies the access token for Azure Application access. | 
**azure_applications_list** | [**[Office365AppCredentials]**](Office365AppCredentials.md) | Specifies a list of Microsoft365 azure application already created within the Microsoft365 source. | 
**azure_tenant_id** | **str, none_type** | Specifies the Azure Active Directory tenant ID or domain name. | 
**skip_client_id_verification** | **bool, none_type** | Specifies whether to skip client Id verification on the passed access token. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


