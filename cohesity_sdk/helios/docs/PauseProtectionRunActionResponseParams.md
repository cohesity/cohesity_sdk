# PauseProtectionRunActionResponseParams

Specifies the response of a pause action on protection runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Specifies an error occured when perfroming pause of a protection run. | [optional] 
**run_id** | **str** | Specifies a unique run id of the Protection Group run. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.pause_protection_run_action_response_params import PauseProtectionRunActionResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of PauseProtectionRunActionResponseParams from a JSON string
pause_protection_run_action_response_params_instance = PauseProtectionRunActionResponseParams.from_json(json)
# print the JSON string representation of the object
print(PauseProtectionRunActionResponseParams.to_json())

# convert the object into a dict
pause_protection_run_action_response_params_dict = pause_protection_run_action_response_params_instance.to_dict()
# create an instance of PauseProtectionRunActionResponseParams from a dict
pause_protection_run_action_response_params_from_dict = PauseProtectionRunActionResponseParams.from_dict(pause_protection_run_action_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


