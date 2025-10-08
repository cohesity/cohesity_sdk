# ObjectProtectionInfo

Specifies the object info on cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int, none_type** | Specifies the cluster id where this object belongs to. | [optional] 
**cluster_incarnation_id** | **int, none_type** | Specifies the cluster incarnation id where this object belongs to. | [optional] 
**is_deleted** | **bool, none_type** | Specifies whether the object is deleted. Deleted objects can&#39;t be protected but can be recovered or unprotected. | [optional] 
**last_run_status** | **str, none_type** | Specifies the status of the object&#39;s last protection run. | [optional] 
**object_backup_configuration** | [**[ProtectionSummary], none_type**](ProtectionSummary.md) | Specifies a list of object protections. | [optional] 
**object_id** | **int, none_type** | Specifies the object id. | [optional] 
**protection_groups** | [**[ObjectProtectionGroupSummary], none_type**](ObjectProtectionGroupSummary.md) | Specifies a list of protection groups protecting this object. | [optional] 
**region_id** | **str, none_type** | Specifies the region id where this object belongs to. | [optional] 
**source_id** | **int, none_type** | Specifies the source id. | [optional] 
**tenant_ids** | **[str]** | List of Tenants the object belongs to. | [optional] 
**view_id** | **int, none_type** | Specifies the view id for the object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


