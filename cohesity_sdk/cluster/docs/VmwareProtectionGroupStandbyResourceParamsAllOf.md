# VmwareProtectionGroupStandbyResourceParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_object_ids** | **[int, none_type]** | Specifies the list of IDs of the datastore objects where this standby resource should be created. | [optional] 
**network_config** | [**RecoverVmwareVmNewSourceNetworkConfig**](RecoverVmwareVmNewSourceNetworkConfig.md) |  | [optional] 
**parent_object_id** | **int, none_type** | Specifies the object id for parent vCenter source where this standby resource should be created. | [optional] 
**rename_restored_object_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**resource_pool_object_id** | **int, none_type** | Specifies the object id for resource pool where this standby resource should be created. | [optional] 
**target_datastore_folder_object_id** | **int, none_type** | Specifies the object id for target datastore folder where disks for this standby resource should be placed. | [optional] 
**target_folder_object_id** | **int, none_type** | Specifies the object id for target vm folder where this standby resource should be created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


