# AzureSourceRegistrationParams

Specifies the paramaters to register an Azure source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_level** | **str, none_type** | Specifies whether the registration is at tenant level or subscription level. | 
**registration_workflow** | **str, none_type** | Specifies whether the type of registration is express or manual. | 
**application_credentials** | [**[AzureApplicationCredentials]**](AzureApplicationCredentials.md) | Specifies the credentials for a list of applications from azure active directory. | [optional] 
**azure_tenant_id** | **str, none_type** | Specifies Tenant Id of the active directory of Azure account. Accpets both Azure tanant Id and tenant domain name. | [optional] 
**subscription_details** | [**[AzureSubscription]**](AzureSubscription.md) | Specifies the list subscription ids to be registered. | [optional] 
**use_cases** | **[str], none_type** | The use cases for which the source is to be registered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


