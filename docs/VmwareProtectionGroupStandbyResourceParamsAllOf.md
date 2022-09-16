# VmwareProtectionGroupStandbyResourceParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rename_restored_object_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies params to rename the standby resource. | [optional] 
**parent_object_id** | **int, none_type** | Specifies the object id for parent vCenter source where this standby resource should be created. | [optional] 
**target_folder_object_id** | **int, none_type** | Specifies the object id for target vm folder where this standby resource should be created. | [optional] 
**target_datastore_folder_object_id** | **int, none_type** | Specifies the object id for target datastore folder where disks for this standby resource should be placed. | [optional] 
**resource_pool_object_id** | **int, none_type** | Specifies the object id for resource pool where this standby resource should be created. | [optional] 
**datastore_object_ids** | **[int, none_type]** | Specifies the list of IDs of the datastore objects where this standby resource should be created. | [optional] 
**network_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the networking configuration to be applied to this standby resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


