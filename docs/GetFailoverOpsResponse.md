# GetFailoverOpsResponse

Specifies the response upon requesting a allowed failover operations for a view id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_failover_operations** | [**List[AllowedFailoverOperation]**](AllowedFailoverOperation.md) | Failover operations that can be performed corresponding to the view id. | [optional] 

## Example

```python
from cohesity_sdk.models.get_failover_ops_response import GetFailoverOpsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFailoverOpsResponse from a JSON string
get_failover_ops_response_instance = GetFailoverOpsResponse.from_json(json)
# print the JSON string representation of the object
print(GetFailoverOpsResponse.to_json())

# convert the object into a dict
get_failover_ops_response_dict = get_failover_ops_response_instance.to_dict()
# create an instance of GetFailoverOpsResponse from a dict
get_failover_ops_response_from_dict = GetFailoverOpsResponse.from_dict(get_failover_ops_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


