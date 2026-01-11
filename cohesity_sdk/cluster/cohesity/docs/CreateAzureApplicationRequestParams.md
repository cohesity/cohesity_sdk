# CreateAzureApplicationRequestParams

Specifies the request parameters for creating Azure Applications

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str, none_type** | Specifies the access token for Azure Application access. | 
**app_count** | **int** | Specifies the count of Azure application to be created. | 
**azure_tenant_id** | **str, none_type** | Specifies the Azure Active Directory tenant ID or domain name. | [optional] 
**certificate_thumbprints** | **[str]** | Specifies a list of certificate thumbprints. The count of items in this list should be either one or equal to the appCount. If only a single thumbprint is provided, all newly created apps will share the certificate. | [optional] 
**existing_microsoft365_app_credentials_list** | [**[Office365AppCredentials]**](Office365AppCredentials.md) | Specifies a list of Microsoft365 azure application credentials already added within the Microsoft365 source. | [optional] 
**microsoft365_region** | **str, none_type** | Specifies the region where Office 365 Exchange environment is. | [optional] 
**o365_app_credentials_list_for_cert_update** | [**[Office365AppCredentials]**](Office365AppCredentials.md) | Specifies the list of exisiting Microsoft365 azure application credentials for which certificates are to be added/ updated. Each app credential in this list should contain a certificate id. | [optional] 
**update_app_key_only** | **bool, none_type** | Specifies whether only secret key for app should be updated during edit call. | [optional]  if omitted the server will use the default value of False
**use_cases** | **[str], none_type** | The usecases for which the application is to be created. | [optional] 
**username** | **str, none_type** | Specifies the username to access Microsoft365 source. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


