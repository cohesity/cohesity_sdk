# ResumeProtectionRunActionParams

Specifies the request to resume a protection run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | Specifies a unique run id of the Protection Group run. | 

## Example

```python
from cohesity_sdk.models.resume_protection_run_action_params import ResumeProtectionRunActionParams

# TODO update the JSON string below
json = "{}"
# create an instance of ResumeProtectionRunActionParams from a JSON string
resume_protection_run_action_params_instance = ResumeProtectionRunActionParams.from_json(json)
# print the JSON string representation of the object
print(ResumeProtectionRunActionParams.to_json())

# convert the object into a dict
resume_protection_run_action_params_dict = resume_protection_run_action_params_instance.to_dict()
# create an instance of ResumeProtectionRunActionParams from a dict
resume_protection_run_action_params_from_dict = ResumeProtectionRunActionParams.from_dict(resume_protection_run_action_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


