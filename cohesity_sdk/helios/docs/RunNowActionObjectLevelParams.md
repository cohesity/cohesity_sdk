# RunNowActionObjectLevelParams

Specifies the request parameters for RunNow action on a Protected object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 
**backup_type** | **str** | Specifies the backup type should be used for RunNow action. | [optional] 
**take_local_snapshot_only** | **bool** | If sepcified as true then runNow will only take local snapshot ignoring all other targets such as replication, archivals etc. If not sepcified or specified as false then runNow will follow the policy settings. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.run_now_action_object_level_params import RunNowActionObjectLevelParams

# TODO update the JSON string below
json = "{}"
# create an instance of RunNowActionObjectLevelParams from a JSON string
run_now_action_object_level_params_instance = RunNowActionObjectLevelParams.from_json(json)
# print the JSON string representation of the object
print(RunNowActionObjectLevelParams.to_json())

# convert the object into a dict
run_now_action_object_level_params_dict = run_now_action_object_level_params_instance.to_dict()
# create an instance of RunNowActionObjectLevelParams from a dict
run_now_action_object_level_params_from_dict = RunNowActionObjectLevelParams.from_dict(run_now_action_object_level_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


