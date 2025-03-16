# CancelObjectRunsResults

Results after canceling object runs. If no errors happen, this will not be returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[CancelObjectRunsResult]**](CancelObjectRunsResult.md) | Specifies results after canceling object runs. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cancel_object_runs_results import CancelObjectRunsResults

# TODO update the JSON string below
json = "{}"
# create an instance of CancelObjectRunsResults from a JSON string
cancel_object_runs_results_instance = CancelObjectRunsResults.from_json(json)
# print the JSON string representation of the object
print(CancelObjectRunsResults.to_json())

# convert the object into a dict
cancel_object_runs_results_dict = cancel_object_runs_results_instance.to_dict()
# create an instance of CancelObjectRunsResults from a dict
cancel_object_runs_results_from_dict = CancelObjectRunsResults.from_dict(cancel_object_runs_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


