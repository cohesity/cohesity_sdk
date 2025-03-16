# NodeUnitProgress

Specifies the progress of the patch operation on a node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_progress** | **bool** | Specifies whether a operation is in progress on the node. | [optional] 
**node_ip** | **str** | Specifies the IP address of the node. | [optional] 
**node_message** | **str** | Specifies a message about the patch operation on the node. | [optional] 
**patch_level_transition** | **str** | Specifies the patch level transition of the patch operation. For Apply operation, patch level goes up for each operation. For Revert operation, patch level goes down. Patch level zero is the base level where no patch was applied. | [optional] 
**percentage** | **int** | Specifies the percentage of completion of the patch operation on the node. | [optional] 
**time_taken_seconds** | **int** | Specifies the time taken so far in this patch unit operation on the node. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.node_unit_progress import NodeUnitProgress

# TODO update the JSON string below
json = "{}"
# create an instance of NodeUnitProgress from a JSON string
node_unit_progress_instance = NodeUnitProgress.from_json(json)
# print the JSON string representation of the object
print(NodeUnitProgress.to_json())

# convert the object into a dict
node_unit_progress_dict = node_unit_progress_instance.to_dict()
# create an instance of NodeUnitProgress from a dict
node_unit_progress_from_dict = NodeUnitProgress.from_dict(node_unit_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


