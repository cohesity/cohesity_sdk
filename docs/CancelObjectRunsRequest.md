# CancelObjectRunsRequest

Request to cancel object runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_runs** | [**List[CancelObjectRunsParams]**](CancelObjectRunsParams.md) | Specifies a list of object runs to cancel. | [optional] 

## Example

```python
from cohesity_sdk.models.cancel_object_runs_request import CancelObjectRunsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelObjectRunsRequest from a JSON string
cancel_object_runs_request_instance = CancelObjectRunsRequest.from_json(json)
# print the JSON string representation of the object
print(CancelObjectRunsRequest.to_json())

# convert the object into a dict
cancel_object_runs_request_dict = cancel_object_runs_request_instance.to_dict()
# create an instance of CancelObjectRunsRequest from a dict
cancel_object_runs_request_from_dict = CancelObjectRunsRequest.from_dict(cancel_object_runs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


