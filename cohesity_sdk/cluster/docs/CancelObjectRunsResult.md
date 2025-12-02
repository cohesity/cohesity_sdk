# CancelObjectRunsResult

Result after canceling object runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Specifies the error message if any error happens. | [optional] 
**object_id** | **int** | Specifies the id of the object. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cancel_object_runs_result import CancelObjectRunsResult

# TODO update the JSON string below
json = "{}"
# create an instance of CancelObjectRunsResult from a JSON string
cancel_object_runs_result_instance = CancelObjectRunsResult.from_json(json)
# print the JSON string representation of the object
print(CancelObjectRunsResult.to_json())

# convert the object into a dict
cancel_object_runs_result_dict = cancel_object_runs_result_instance.to_dict()
# create an instance of CancelObjectRunsResult from a dict
cancel_object_runs_result_from_dict = CancelObjectRunsResult.from_dict(cancel_object_runs_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


