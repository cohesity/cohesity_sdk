# McmTenantObjectProtection

Specifies an object protection for a given tenant.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_protection_id** | **str, none_type** | Specifies the id assigned to the entry. | [optional] 
**tenant_ids** | **[str, none_type]** | Specifies the tenants which have access to this object. | [optional] 
**account_id** | **str, none_type** | Specifies the account ID to which this source belongs. | [optional] 
**dmaas_tenant_id** | **str, none_type** | Specifies the DMaaS tenant ID to which this source belongs. | [optional] 
**region_id** | **str, none_type** | Specifies the region ID of the cluster. | [optional] 
**cluster_id** | **int, none_type** | Specifies the ID of the cluster to which the source is registered. | [optional] 
**object_hash** | **str, none_type** | Specifies the object hash of the source. | [optional] 
**user_details** | [**User**](User.md) |  | [optional] 
**created_at_msecs** | **int, none_type** | Specifies the timestamp at which this entry was created in msecs. | [optional] 
**updated_at_msecs** | **int, none_type** | Specifies the timestamp at which this entry was updated in msecs. | [optional] 
**object_protection** | [**ProtectedObjectInfo**](ProtectedObjectInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


