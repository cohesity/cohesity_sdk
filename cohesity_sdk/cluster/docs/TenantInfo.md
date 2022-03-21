# TenantInfo

Description of a Tenant and it's properties.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | The tenant id. | [optional] 
**name** | **str, none_type** | Name of the Tenant. | [optional] 
**description** | **str, none_type** | Description about the tenant. | [optional] 
**status** | **str, none_type** | Current Status of the Tenant. | [optional] 
**network** | [**TenantNetwork**](TenantNetwork.md) |  | [optional] 
**created_at_time_msecs** | **int, none_type** | Epoch time when tenant was created. | [optional] [readonly] 
**last_updated_at_time_msecs** | **int, none_type** | Epoch time when tenant was last updated. | [optional] [readonly] 
**deleted_at_time_msecs** | **int, none_type** | Epoch time when tenant was last updated. | [optional] [readonly] 
**is_managed_on_helios** | **bool, none_type** | Flag to indicate if tenant is managed on helios | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


