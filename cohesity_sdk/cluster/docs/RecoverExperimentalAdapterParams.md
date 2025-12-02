# RecoverExperimentalAdapterParams

Specifies the parameters to recover Experimental Adapter objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overwrite** | **bool** | Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object. | [optional] 
**recover_to** | **int** | Specifies the &#39;Source Registration ID&#39; of the source where the objects are to be recovered. If this is not specified, the recovery job will recover to the original location. | [optional] 
**restore_target_entity_id** | **int** | Specifies the ID of the entity under which the objects need to be restored. This is relevant only when restoring to an alternate target. | [optional] 
**restore_type** | **str** | Specifies the type of experimental adapter restore. | [optional] 
**snapshots** | [**List[RecoverExperimentalAdapterSnapshotParams]**](RecoverExperimentalAdapterSnapshotParams.md) | Specifies the local snapshot ids and other details of the objects to be recovered. | 
**workflow_params** | **str** | Workflow parameters to be supplied to all backup workflow tasks. This specifies task configuration such as the time to wait before returning the workflow result, subtasks configuration such as number of subtasks to generate and the depth of the subtask tree, etc. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_experimental_adapter_params import RecoverExperimentalAdapterParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverExperimentalAdapterParams from a JSON string
recover_experimental_adapter_params_instance = RecoverExperimentalAdapterParams.from_json(json)
# print the JSON string representation of the object
print(RecoverExperimentalAdapterParams.to_json())

# convert the object into a dict
recover_experimental_adapter_params_dict = recover_experimental_adapter_params_instance.to_dict()
# create an instance of RecoverExperimentalAdapterParams from a dict
recover_experimental_adapter_params_from_dict = RecoverExperimentalAdapterParams.from_dict(recover_experimental_adapter_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


