# ActiveDirectoryProtectionGroupObjectParams

Specifies the object identifier to for the active directory protection group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **int, none_type** | Specifies the id of the registered active directory source. | 
**source_name** | **str, none_type** | Specifies the name of the registered active directory source. | [optional] [readonly] 
**app_params** | [**[ActiveDirectoryAppParams], none_type**](ActiveDirectoryAppParams.md) | Specifies the specific parameters required for active directory app configuration. | [optional] 
**enable_system_backup** | **bool, none_type** | Specifies whether to take bmr backup. If this is not specified, the bmr backup won&#39;t be enabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


