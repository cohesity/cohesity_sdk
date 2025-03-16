# RunNowActionObjectLevelResponse

Specifies the infomration about status of run now action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Error**](Error.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.run_now_action_object_level_response import RunNowActionObjectLevelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RunNowActionObjectLevelResponse from a JSON string
run_now_action_object_level_response_instance = RunNowActionObjectLevelResponse.from_json(json)
# print the JSON string representation of the object
print(RunNowActionObjectLevelResponse.to_json())

# convert the object into a dict
run_now_action_object_level_response_dict = run_now_action_object_level_response_instance.to_dict()
# create an instance of RunNowActionObjectLevelResponse from a dict
run_now_action_object_level_response_from_dict = RunNowActionObjectLevelResponse.from_dict(run_now_action_object_level_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


