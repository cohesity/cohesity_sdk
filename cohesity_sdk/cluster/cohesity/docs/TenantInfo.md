# TenantInfo

Description of a Tenant and it's properties.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_deactivation** | **str, none_type** | Specifies info about the active deactivation of this tenant, if any. | [optional] 
**created_at_time_msecs** | **int, none_type** | Epoch time when tenant was created. | [optional] [readonly] 
**deleted_at_time_msecs** | **int, none_type** | Epoch time when tenant was last updated. | [optional] [readonly] 
**description** | **str, none_type** | Description about the tenant. | [optional] 
**external_vendor_metadata** | [**ExternalVendorTenantMetadata**](ExternalVendorTenantMetadata.md) |  | [optional] 
**finished_deactivations** | **[str, none_type], none_type** | Specifies a history of deactivations for this tenant. Only the latest 5 deactivations are preserved. | [optional] 
**id** | **str, none_type** | The tenant id. | [optional] 
**is_managed_on_helios** | **bool, none_type** | Flag to indicate if tenant is managed on helios | [optional] 
**last_updated_at_time_msecs** | **int, none_type** | Epoch time when tenant was last updated. | [optional] [readonly] 
**name** | **str, none_type** | Name of the Tenant. | [optional] 
**network** | [**TenantNetwork**](TenantNetwork.md) |  | [optional] 
**status** | **str, none_type** | Current Status of the Tenant. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


