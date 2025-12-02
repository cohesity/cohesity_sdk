# AppOrchestratorError

Error Object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** | The error code indicating the type of error. | [optional] 
**error_message** | **str** | A descriptive error message explaining the issue. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.app_orchestrator_error import AppOrchestratorError

# TODO update the JSON string below
json = "{}"
# create an instance of AppOrchestratorError from a JSON string
app_orchestrator_error_instance = AppOrchestratorError.from_json(json)
# print the JSON string representation of the object
print(AppOrchestratorError.to_json())

# convert the object into a dict
app_orchestrator_error_dict = app_orchestrator_error_instance.to_dict()
# create an instance of AppOrchestratorError from a dict
app_orchestrator_error_from_dict = AppOrchestratorError.from_dict(app_orchestrator_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


