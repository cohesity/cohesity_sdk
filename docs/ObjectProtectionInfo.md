# ObjectProtectionInfo

Specifies the object info on clsuter.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **int, none_type** | Specifies the object id. | [optional] 
**source_id** | **int, none_type** | Specifies the source id. | [optional] 
**region_id** | **str, none_type** | Specifies the region id where this object belongs to. | [optional] 
**cluster_id** | **int, none_type** | Specifies the cluster id where this object belongs to. | [optional] 
**cluster_incarnation_id** | **int, none_type** | Specifies the cluster incarnation id where this object belongs to. | [optional] 
**protection_groups** | [**[ObjectProtectionGroupSummary], none_type**](ObjectProtectionGroupSummary.md) | Specifies a list of protection groups protecting this object. | [optional] 
**object_backup_configuration** | [**[ProtectionSummary], none_type**](ProtectionSummary.md) | Specifies a list of object protections. | [optional] 
**last_run_status** | **str, none_type** | Specifies the status of the object&#39;s last protection run. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


