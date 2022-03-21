# RestoreVMwareVMParams

Specifies the parameters for a VMware recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_vm_folder_id** | **int, none_type** | Specifies the folder ID where the VMs should be created. | [optional] 
**target_data_store_id** | **int, none_type** | Specifies the folder where the restore datastore should be created. | [optional] 
**enable_copy_recovery** | **bool, none_type** | Specifies whether to perform copy recovery or not. | [optional] 
**resource_pool_id** | **int, none_type** | Specifies if the restore is to alternate location. | [optional] 
**datastore_ids** | **[int], none_type** | Specifies Datastore Ids, if the restore is to alternate location. | [optional] 
**overwrite_existing_vm** | **bool, none_type** | Specifies whether to overwrite the VM at the target location. | [optional] 
**power_off_and_rename_existing_vm** | **bool, none_type** | Specifies whether to power off and mark the VM at the target location as deprecated. | [optional] 
**attempt_differential_restore** | **bool, none_type** | Specifies whether to attempt differential restore. | [optional] 
**is_on_prem_deploy** | **bool, none_type** | Specifies whether a task in on prem deploy or not. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


