# GetViewFailoverResponseBody

Specifies planned failovers and unplanned failovers of a view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failovers** | [**List[Failover]**](Failover.md) | Specifies a list of failovers. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.get_view_failover_response_body import GetViewFailoverResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetViewFailoverResponseBody from a JSON string
get_view_failover_response_body_instance = GetViewFailoverResponseBody.from_json(json)
# print the JSON string representation of the object
print(GetViewFailoverResponseBody.to_json())

# convert the object into a dict
get_view_failover_response_body_dict = get_view_failover_response_body_instance.to_dict()
# create an instance of GetViewFailoverResponseBody from a dict
get_view_failover_response_body_from_dict = GetViewFailoverResponseBody.from_dict(get_view_failover_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


