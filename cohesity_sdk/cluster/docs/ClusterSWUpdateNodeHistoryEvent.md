# ClusterSWUpdateNodeHistoryEvent

Represents an event of node upgrade/patch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_timestamp_secs** | **int** | Unix epoch timestamp (in seconds) when the upgrade/patch was done on the node.  | [optional] 
**node_id** | **int** | Node id of the node. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_sw_update_node_history_event import ClusterSWUpdateNodeHistoryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterSWUpdateNodeHistoryEvent from a JSON string
cluster_sw_update_node_history_event_instance = ClusterSWUpdateNodeHistoryEvent.from_json(json)
# print the JSON string representation of the object
print(ClusterSWUpdateNodeHistoryEvent.to_json())

# convert the object into a dict
cluster_sw_update_node_history_event_dict = cluster_sw_update_node_history_event_instance.to_dict()
# create an instance of ClusterSWUpdateNodeHistoryEvent from a dict
cluster_sw_update_node_history_event_from_dict = ClusterSWUpdateNodeHistoryEvent.from_dict(cluster_sw_update_node_history_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


