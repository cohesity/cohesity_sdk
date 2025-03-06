# ActionObjectLevelResponse

Specifies the object level response params after performing an action on a protected object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 
**pause_status** | [**PauseActionObjectLevelResponse**](PauseActionObjectLevelResponse.md) |  | [optional] 
**resume_status** | [**ResumeActionObjectLevelResponse**](ResumeActionObjectLevelResponse.md) |  | [optional] 
**run_now_status** | [**RunNowActionObjectLevelResponse**](RunNowActionObjectLevelResponse.md) |  | [optional] 
**un_protect_status** | [**UnprotectActionObjectLevelResponse**](UnprotectActionObjectLevelResponse.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.action_object_level_response import ActionObjectLevelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActionObjectLevelResponse from a JSON string
action_object_level_response_instance = ActionObjectLevelResponse.from_json(json)
# print the JSON string representation of the object
print(ActionObjectLevelResponse.to_json())

# convert the object into a dict
action_object_level_response_dict = action_object_level_response_instance.to_dict()
# create an instance of ActionObjectLevelResponse from a dict
action_object_level_response_from_dict = ActionObjectLevelResponse.from_dict(action_object_level_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


