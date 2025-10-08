# RecoverVmwareChildSnapshotParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_migration_info** | [**RecoveryTaskInfo**](RecoveryTaskInfo.md) |  | [optional] 
**instant_recovery_info** | [**RecoveryTaskInfo**](RecoveryTaskInfo.md) |  | [optional] 
**restored_object_info** | [**Object**](Object.md) |  | [optional] 
**tear_down_message** | **str, none_type** | Specifies the error message about the tear down operation. | [optional] 
**tear_down_status** | **str, none_type** | Indicates the tear down status of the VM. &#39;DestroyScheduled&#39; indicates that the tear down is ready to schedule. &#39;Destroying&#39; indicates that the tear down is still running. &#39;Destroyed&#39; indicates that the tear down succeeded. &#39;DestroyError&#39; indicates that the tear down failed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


