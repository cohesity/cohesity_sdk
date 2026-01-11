# CreateM365SelfServiceConfigRequestParams

Specifies the request parameters to enable Self-Service for a given Microsoft365 source. The Self-Service workflow includes search & recovery of granular items within Mailbox & OneDrive workloads only.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str, none_type** | Specifies the domain name of the Microsoft365 Source. | 
**tenant_id** | **str, none_type** | Specifies the Cohesity Tenant ID for the Microsoft365 source owner. | 
**uuid** | **str, none_type** | Specifies the UUID of the Microsoft365 Source. | 
**mailbox_params** | [**M365SelfServiceWorkloadParams**](M365SelfServiceWorkloadParams.md) |  | [optional] 
**oidc_config** | [**OIDCStandardConfiguration**](OIDCStandardConfiguration.md) |  | [optional] 
**one_drive_params** | [**M365SelfServiceWorkloadParams**](M365SelfServiceWorkloadParams.md) |  | [optional] 
**preferred_authentication_mode** | **str, none_type** | Specifies the authentication mode for Self Service workflow. If unspecified this will default to Azure AD. Otherwise Self-Service will use associated IdP OIDC Configuration. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


