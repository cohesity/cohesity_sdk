# ReverseReplicationResult

Specifies the request parameters to create a view failover task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_reason** | **str** | Specifies the reason of not enabling reverse replication. | [optional] 
**is_reverse_replication_enabled** | **bool** | Specifies whether the reverse replication was enabled or not during group creation. It can be false, if source cluster is not reachable for reverse replication. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.reverse_replication_result import ReverseReplicationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ReverseReplicationResult from a JSON string
reverse_replication_result_instance = ReverseReplicationResult.from_json(json)
# print the JSON string representation of the object
print(ReverseReplicationResult.to_json())

# convert the object into a dict
reverse_replication_result_dict = reverse_replication_result_instance.to_dict()
# create an instance of ReverseReplicationResult from a dict
reverse_replication_result_from_dict = ReverseReplicationResult.from_dict(reverse_replication_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


