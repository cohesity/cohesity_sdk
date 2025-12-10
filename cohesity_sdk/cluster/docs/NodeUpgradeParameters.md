# NodeUpgradeParameters

Parameters for Node Upgrade.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_ids** | **List[int]** | Specifies a list of IDs of additional nodes to be upgraded. These must be free Nodes present on the same local network as the Node that the request was sent to. The ID of the Node the request was sent to should not be included in this list. This parameter can only be specified if upgradeAllFreeNodes is not specified.  | [optional] 
**target_sw_version** | **str** | Specifies the target software version. The node that the request is sent to will search itself for the specified software package and if that package is found, it will be used for the upgrade.  | 
**upgrade_all_free_nodes** | **bool** | Specifies whether or not to attempt to upgrade all free nodes which are currently connected to the same local network as the node that the request was sent to. This parameter can only be specified if nodeIds is not specified.  | [optional] 
**upgrade_self** | **bool** | Specifies that the node that the request is being sent to should be upgraded. By default, this is set to true.  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.node_upgrade_parameters import NodeUpgradeParameters

# TODO update the JSON string below
json = "{}"
# create an instance of NodeUpgradeParameters from a JSON string
node_upgrade_parameters_instance = NodeUpgradeParameters.from_json(json)
# print the JSON string representation of the object
print(NodeUpgradeParameters.to_json())

# convert the object into a dict
node_upgrade_parameters_dict = node_upgrade_parameters_instance.to_dict()
# create an instance of NodeUpgradeParameters from a dict
node_upgrade_parameters_from_dict = NodeUpgradeParameters.from_dict(node_upgrade_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


