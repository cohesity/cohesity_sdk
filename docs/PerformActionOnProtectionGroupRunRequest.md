# PerformActionOnProtectionGroupRunRequest

Specifies the request to perform actions on protection runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the type of the action which will be performed on protection runs. | 
**cancel_params** | [**List[CancelProtectionGroupRunRequest]**](CancelProtectionGroupRunRequest.md) | Specifies the cancel action params for a protection run. | [optional] 
**pause_params** | [**List[PauseProtectionRunActionParams]**](PauseProtectionRunActionParams.md) | Specifies the pause action params for a protection run. | [optional] 
**resume_params** | [**List[ResumeProtectionRunActionParams]**](ResumeProtectionRunActionParams.md) | Specifies the resume action params for a protection run. | [optional] 

## Example

```python
from cohesity_sdk.models.perform_action_on_protection_group_run_request import PerformActionOnProtectionGroupRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PerformActionOnProtectionGroupRunRequest from a JSON string
perform_action_on_protection_group_run_request_instance = PerformActionOnProtectionGroupRunRequest.from_json(json)
# print the JSON string representation of the object
print(PerformActionOnProtectionGroupRunRequest.to_json())

# convert the object into a dict
perform_action_on_protection_group_run_request_dict = perform_action_on_protection_group_run_request_instance.to_dict()
# create an instance of PerformActionOnProtectionGroupRunRequest from a dict
perform_action_on_protection_group_run_request_from_dict = PerformActionOnProtectionGroupRunRequest.from_dict(perform_action_on_protection_group_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


