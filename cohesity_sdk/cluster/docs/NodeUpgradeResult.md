# NodeUpgradeResult

Result of Node Upgrade after a successful request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Result of Node Upgrade after a successful request. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.node_upgrade_result import NodeUpgradeResult

# TODO update the JSON string below
json = "{}"
# create an instance of NodeUpgradeResult from a JSON string
node_upgrade_result_instance = NodeUpgradeResult.from_json(json)
# print the JSON string representation of the object
print(NodeUpgradeResult.to_json())

# convert the object into a dict
node_upgrade_result_dict = node_upgrade_result_instance.to_dict()
# create an instance of NodeUpgradeResult from a dict
node_upgrade_result_from_dict = NodeUpgradeResult.from_dict(node_upgrade_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


