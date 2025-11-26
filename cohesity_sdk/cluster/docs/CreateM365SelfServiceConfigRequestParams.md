# CreateM365SelfServiceConfigRequestParams

Specifies the request parameters to enable Self-Service for a given Microsoft365 source. The Self-Service workflow includes search & recovery of granular items within Mailbox & OneDrive workloads only.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str, none_type** | Specifies the Cohesity Tenant ID for the Microsoft365 source owner. | 
**uuid** | **str, none_type** | Specifies the UUID of the Microsoft365 Source. | 
**mailbox_params** | [**M365SelfServiceWorkloadParams**](M365SelfServiceWorkloadParams.md) |  | [optional] 
**one_drive_params** | [**M365SelfServiceWorkloadParams**](M365SelfServiceWorkloadParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


