# GetProtectionRunsStatusResponseBody

Specifies a list of protection runs stats taken at different time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_runs_stats_list** | [**List[ProtectionRunsStatsList]**](ProtectionRunsStatsList.md) | Specifies a list of protection runs stats taken at different time. | [optional] 

## Example

```python
from cohesity_sdk.models.get_protection_runs_status_response_body import GetProtectionRunsStatusResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetProtectionRunsStatusResponseBody from a JSON string
get_protection_runs_status_response_body_instance = GetProtectionRunsStatusResponseBody.from_json(json)
# print the JSON string representation of the object
print(GetProtectionRunsStatusResponseBody.to_json())

# convert the object into a dict
get_protection_runs_status_response_body_dict = get_protection_runs_status_response_body_instance.to_dict()
# create an instance of GetProtectionRunsStatusResponseBody from a dict
get_protection_runs_status_response_body_from_dict = GetProtectionRunsStatusResponseBody.from_dict(get_protection_runs_status_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


