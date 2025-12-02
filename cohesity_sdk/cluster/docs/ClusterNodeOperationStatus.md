# ClusterNodeOperationStatus

Status of operation on a node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[OperationEvents]**](OperationEvents.md) | Specifies the list of events that took place during the operation.  | [optional] 
**id** | **int** | Specifies the ID of the node. | [optional] 
**ip** | **str** | Specifies the IP address of the node. | [optional] 
**percentage** | **int** | Specifies the approximate completion percentage for the operation. | [optional] 
**status** | **str** | Specifies the status of the operation. &#x60;Success&#x60; indicates the operation is successful. &#x60;Failed&#x60; indicates the operation failed due to an error. &#x60;InProgress&#x60; indicates the operation is in progress.  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_node_operation_status import ClusterNodeOperationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodeOperationStatus from a JSON string
cluster_node_operation_status_instance = ClusterNodeOperationStatus.from_json(json)
# print the JSON string representation of the object
print(ClusterNodeOperationStatus.to_json())

# convert the object into a dict
cluster_node_operation_status_dict = cluster_node_operation_status_instance.to_dict()
# create an instance of ClusterNodeOperationStatus from a dict
cluster_node_operation_status_from_dict = ClusterNodeOperationStatus.from_dict(cluster_node_operation_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


