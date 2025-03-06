# GetObjectRunsResponseBody

Specifies the response body of the get object run request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination_info** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 
**protection_runs** | [**List[ObjectProtectionRunSummary]**](ObjectProtectionRunSummary.md) | Specifies the protection runs of the given object. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.get_object_runs_response_body import GetObjectRunsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetObjectRunsResponseBody from a JSON string
get_object_runs_response_body_instance = GetObjectRunsResponseBody.from_json(json)
# print the JSON string representation of the object
print(GetObjectRunsResponseBody.to_json())

# convert the object into a dict
get_object_runs_response_body_dict = get_object_runs_response_body_instance.to_dict()
# create an instance of GetObjectRunsResponseBody from a dict
get_object_runs_response_body_from_dict = GetObjectRunsResponseBody.from_dict(get_object_runs_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


