# PauseActionObjectLevelParams

Specifies the request parameters for Pause action on a Protected object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.pause_action_object_level_params import PauseActionObjectLevelParams

# TODO update the JSON string below
json = "{}"
# create an instance of PauseActionObjectLevelParams from a JSON string
pause_action_object_level_params_instance = PauseActionObjectLevelParams.from_json(json)
# print the JSON string representation of the object
print(PauseActionObjectLevelParams.to_json())

# convert the object into a dict
pause_action_object_level_params_dict = pause_action_object_level_params_instance.to_dict()
# create an instance of PauseActionObjectLevelParams from a dict
pause_action_object_level_params_from_dict = PauseActionObjectLevelParams.from_dict(pause_action_object_level_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


