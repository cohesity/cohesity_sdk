# Office365SourceRegistrationParams

Specifies the paramaters to register an office-365 source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password to access target entity. | 
**username** | **str** | Specifies the username to access target entity. | 
**endpoint** | **str** | Specifies the endpoint IPaddress, URL or hostname of the host. | 
**description** | **str, none_type** | Specifies the description of the source being registered. | [optional] 
**o365_objects_discovery_params** | [**ObjectsDiscoveryParams**](ObjectsDiscoveryParams.md) |  | [optional] 
**office365_app_credentials_list** | [**[Office365AppCredentials]**](Office365AppCredentials.md) | Specifies a list of office365 azure application credentials needed to authenticate &amp; authorize users for Office 365. | [optional] 
**office365_region** | **str, none_type** | Specifies the region where Office 365 Exchange environment is. | [optional] 
**office365_service_account_credentials_list** | [**[Credentials], none_type**](Credentials.md) | Specifies the list of Office365 service account credentials which can be used for Mailbox Backups. | [optional] 
**proxy_host_source_id_list** | **[int], none_type** | Specifies the list of the protection source id of the windows physical host which will be used during the protection and recovery of the sites that belong to a office365 domain. | [optional] 
**use_existing_credentials** | **bool, none_type** | Specifies whether to use existing Office365 credentials like password and client secret for app id&#39;s. This parameter is only valid in the case of updating the registered source. | [optional] 
**use_o_auth_for_exchange_online** | **bool, none_type** | Specifies whether OAuth should be used for authentication in case of Exchange Online. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


