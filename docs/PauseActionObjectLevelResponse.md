# PauseActionObjectLevelResponse

Specifies the infomration about status of pause action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Error**](Error.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.pause_action_object_level_response import PauseActionObjectLevelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PauseActionObjectLevelResponse from a JSON string
pause_action_object_level_response_instance = PauseActionObjectLevelResponse.from_json(json)
# print the JSON string representation of the object
print(PauseActionObjectLevelResponse.to_json())

# convert the object into a dict
pause_action_object_level_response_dict = pause_action_object_level_response_instance.to_dict()
# create an instance of PauseActionObjectLevelResponse from a dict
pause_action_object_level_response_from_dict = PauseActionObjectLevelResponse.from_dict(pause_action_object_level_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


