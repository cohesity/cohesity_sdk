# NodeStatus

Specifies the status of each node in the cluster being created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Specifies an optional message relating to the node status. | [optional] 
**ipmi_ip** | **str** | Specifies the IPMI IP of the node (if physical cluster). | [optional] 
**node_id** | **int** | Specifies the ID of the node. | [optional] 
**node_ip** | **str** | Specifies the IP of the node. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.node_status import NodeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NodeStatus from a JSON string
node_status_instance = NodeStatus.from_json(json)
# print the JSON string representation of the object
print(NodeStatus.to_json())

# convert the object into a dict
node_status_dict = node_status_instance.to_dict()
# create an instance of NodeStatus from a dict
node_status_from_dict = NodeStatus.from_dict(node_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


