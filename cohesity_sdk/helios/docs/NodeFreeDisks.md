# NodeFreeDisks

Sepcifies the free disks of a node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_serial** | **str** | Chassis serial number. | [optional] 
**error_message** | **str** | Error message of disks assimilation request. | [optional] [readonly] 
**free_disks** | [**List[FreeDisk]**](FreeDisk.md) | Specifies list of free disks of node. | 
**node_id** | **int** | Specifies the id of a node. | 
**slot** | **int** | Slot number of node | [optional] 

## Example

```python
from cohesity_sdk.helios.models.node_free_disks import NodeFreeDisks

# TODO update the JSON string below
json = "{}"
# create an instance of NodeFreeDisks from a JSON string
node_free_disks_instance = NodeFreeDisks.from_json(json)
# print the JSON string representation of the object
print(NodeFreeDisks.to_json())

# convert the object into a dict
node_free_disks_dict = node_free_disks_instance.to_dict()
# create an instance of NodeFreeDisks from a dict
node_free_disks_from_dict = NodeFreeDisks.from_dict(node_free_disks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


