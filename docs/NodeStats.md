# NodeStats

NodeStats provides various statistics for the node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id is the Id of the Node. | [optional] 
**usage_perf_stats** | [**UsageAndPerformanceStats**](UsageAndPerformanceStats.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.node_stats import NodeStats

# TODO update the JSON string below
json = "{}"
# create an instance of NodeStats from a JSON string
node_stats_instance = NodeStats.from_json(json)
# print the JSON string representation of the object
print(NodeStats.to_json())

# convert the object into a dict
node_stats_dict = node_stats_instance.to_dict()
# create an instance of NodeStats from a dict
node_stats_from_dict = NodeStats.from_dict(node_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


