# HeliosTenant

Description of a Tenant and it's properties on various clusters.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at_time_msecs** | **int, none_type** | Epoch time when tenant was created. | [optional] [readonly] 
**deleted_at_time_msecs** | **int, none_type** | Epoch time when tenant was last updated. | [optional] [readonly] 
**description** | **str, none_type** | Description about the tenant. | [optional] 
**id** | **str, none_type** | The tenant id. | [optional] 
**last_updated_at_time_msecs** | **int, none_type** | Epoch time when tenant was last updated. | [optional] [readonly] 
**managed_on_helios** | **bool, none_type** | Wether managed on helios or not. | [optional] 
**name** | **str, none_type** | Name of the Tenant | [optional] 
**status** | **str, none_type** | Current Status of the Tenant. | [optional] 
**systems** | [**[HeliosClusterTenant]**](HeliosClusterTenant.md) | Details of tenant on each system that it is living. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


