# RecoverExperimentalAdapterParams

Specifies the parameters to recover Experimental Adapter objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**[RecoverExperimentalAdapterSnapshotParams], none_type**](RecoverExperimentalAdapterSnapshotParams.md) | Specifies the local snapshot ids and other details of the objects to be recovered. | 
**overwrite** | **bool, none_type** | Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object. | [optional] 
**recover_to** | **int, none_type** | Specifies the &#39;Source Registration ID&#39; of the source where the objects are to be recovered. If this is not specified, the recovery job will recover to the original location. | [optional] 
**restore_target_entity_id** | **int, none_type** | Specifies the ID of the entity under which the objects need to be restored. This is relevant only when restoring to an alternate target. | [optional] 
**restore_type** | **str, none_type** | Specifies the type of experimental adapter restore. | [optional]  if omitted the server will use the default value of "RecoverObjects"
**workflow_params** | **str, none_type** | Workflow parameters to be supplied to all backup workflow tasks. This specifies task configuration such as the time to wait before returning the workflow result, subtasks configuration such as number of subtasks to generate and the depth of the subtask tree, etc. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


