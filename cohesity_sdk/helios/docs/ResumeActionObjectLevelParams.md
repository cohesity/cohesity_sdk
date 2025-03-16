# ResumeActionObjectLevelParams

Specifies the request parameters for Resume action on a Protected object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.resume_action_object_level_params import ResumeActionObjectLevelParams

# TODO update the JSON string below
json = "{}"
# create an instance of ResumeActionObjectLevelParams from a JSON string
resume_action_object_level_params_instance = ResumeActionObjectLevelParams.from_json(json)
# print the JSON string representation of the object
print(ResumeActionObjectLevelParams.to_json())

# convert the object into a dict
resume_action_object_level_params_dict = resume_action_object_level_params_instance.to_dict()
# create an instance of ResumeActionObjectLevelParams from a dict
resume_action_object_level_params_from_dict = ResumeActionObjectLevelParams.from_dict(resume_action_object_level_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


