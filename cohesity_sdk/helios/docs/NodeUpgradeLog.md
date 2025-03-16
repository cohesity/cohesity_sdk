# NodeUpgradeLog

Specifies the upgrade logs for a node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[UpgradeLog]**](UpgradeLog.md) | Upgrade logs for the node. | [optional] 
**node_id** | **str** | Id of the node. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.node_upgrade_log import NodeUpgradeLog

# TODO update the JSON string below
json = "{}"
# create an instance of NodeUpgradeLog from a JSON string
node_upgrade_log_instance = NodeUpgradeLog.from_json(json)
# print the JSON string representation of the object
print(NodeUpgradeLog.to_json())

# convert the object into a dict
node_upgrade_log_dict = node_upgrade_log_instance.to_dict()
# create an instance of NodeUpgradeLog from a dict
node_upgrade_log_from_dict = NodeUpgradeLog.from_dict(node_upgrade_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


