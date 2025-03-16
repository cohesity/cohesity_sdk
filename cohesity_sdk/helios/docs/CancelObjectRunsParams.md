# CancelObjectRunsParams

Request to cancel object runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **int** | Specifies object id | 
**runs_config** | [**List[CancelObjectRunParams]**](CancelObjectRunParams.md) | Specifies a list of runs to cancel. If no runs are specified, then all the outstanding runs will be canceled. | [optional] 
**snapshot_backend_types** | **List[str]** | Specifies the protections type on which action to be performed. This is used when an object is protected by multiple protection types. If not specified action will be performed on all protection types. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cancel_object_runs_params import CancelObjectRunsParams

# TODO update the JSON string below
json = "{}"
# create an instance of CancelObjectRunsParams from a JSON string
cancel_object_runs_params_instance = CancelObjectRunsParams.from_json(json)
# print the JSON string representation of the object
print(CancelObjectRunsParams.to_json())

# convert the object into a dict
cancel_object_runs_params_dict = cancel_object_runs_params_instance.to_dict()
# create an instance of CancelObjectRunsParams from a dict
cancel_object_runs_params_from_dict = CancelObjectRunsParams.from_dict(cancel_object_runs_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


