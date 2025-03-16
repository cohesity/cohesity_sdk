# PerformRunActionResponse

Specifies the response of the performed run action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the type of the action is performed on protection runs. | [optional] 
**cancel_params** | [**List[CancelProtectionGroupRunResponseParams]**](CancelProtectionGroupRunResponseParams.md) | Specifies the cancel action response params. | [optional] 
**pause_params** | [**List[PauseProtectionRunActionResponseParams]**](PauseProtectionRunActionResponseParams.md) | Specifies the pause action response params. | [optional] 
**resume_params** | [**List[ResumeProtectionRunActionResponseParams]**](ResumeProtectionRunActionResponseParams.md) | Specifies the resume action response params. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.perform_run_action_response import PerformRunActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PerformRunActionResponse from a JSON string
perform_run_action_response_instance = PerformRunActionResponse.from_json(json)
# print the JSON string representation of the object
print(PerformRunActionResponse.to_json())

# convert the object into a dict
perform_run_action_response_dict = perform_run_action_response_instance.to_dict()
# create an instance of PerformRunActionResponse from a dict
perform_run_action_response_from_dict = PerformRunActionResponse.from_dict(perform_run_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


