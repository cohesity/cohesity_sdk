# TenantAccess

Specifies the Tenant Access.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str, none_type** | Specifies the Tenant Id of the tenant access. | 
**roles** | **[str]** | Specifies a list of roles associated with this access. | 
**clusters** | [**[McmClusterIdentifier]**](McmClusterIdentifier.md) | Specifies the list of clusters accessible by this access. | 
**created_time_msecs** | **int, none_type** | Specifies the timestamp in milliseconds since the epoch when this access was created. | [optional] [readonly] 
**last_updated_time_msecs** | **int, none_type** | Specifies the timestamp in milliseconds since the epoch when this access was updated. | [optional] [readonly] 
**is_access_active** | **bool, none_type** | Specifies whether or not this access is currently active. | [optional] [readonly] 
**effective_time_msecs** | **int, none_type** | Specifies the starting timestamp in milliseconds since the epoch when this access will be able allowed. | [optional] [readonly] 
**expired_time_msecs** | **int, none_type** | Specifies the timestamp in milliseconds since the epoch when this access will no longer be allowed. | [optional] [readonly] 
**tenant_name** | **str, none_type** | Name of the Tenant. | [optional] [readonly] 
**tenant_status** | **str, none_type** | Specifies the Tenant status. | [optional] [readonly] 
**tenant_type** | **str, none_type** | Specifies the type of the tenant. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


