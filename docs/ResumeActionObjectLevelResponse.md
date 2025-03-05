# ResumeActionObjectLevelResponse

Specifies the infomration about status of resume action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Error**](Error.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.resume_action_object_level_response import ResumeActionObjectLevelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResumeActionObjectLevelResponse from a JSON string
resume_action_object_level_response_instance = ResumeActionObjectLevelResponse.from_json(json)
# print the JSON string representation of the object
print(ResumeActionObjectLevelResponse.to_json())

# convert the object into a dict
resume_action_object_level_response_dict = resume_action_object_level_response_instance.to_dict()
# create an instance of ResumeActionObjectLevelResponse from a dict
resume_action_object_level_response_from_dict = ResumeActionObjectLevelResponse.from_dict(resume_action_object_level_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


