# PauseProtectionRunActionParams

Specifies the request to pause a protection run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | Specifies a unique run id of the Protection Group run. | 

## Example

```python
from cohesity_sdk.helios.models.pause_protection_run_action_params import PauseProtectionRunActionParams

# TODO update the JSON string below
json = "{}"
# create an instance of PauseProtectionRunActionParams from a JSON string
pause_protection_run_action_params_instance = PauseProtectionRunActionParams.from_json(json)
# print the JSON string representation of the object
print(PauseProtectionRunActionParams.to_json())

# convert the object into a dict
pause_protection_run_action_params_dict = pause_protection_run_action_params_instance.to_dict()
# create an instance of PauseProtectionRunActionParams from a dict
pause_protection_run_action_params_from_dict = PauseProtectionRunActionParams.from_dict(pause_protection_run_action_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


