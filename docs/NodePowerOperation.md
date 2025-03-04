# NodePowerOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **int** | Id of the node to do the specified operation. | [optional] 
**operation** | **str** | The operation clould be poweroff, reboot. | 

## Example

```python
from cohesity_sdk.models.node_power_operation import NodePowerOperation

# TODO update the JSON string below
json = "{}"
# create an instance of NodePowerOperation from a JSON string
node_power_operation_instance = NodePowerOperation.from_json(json)
# print the JSON string representation of the object
print(NodePowerOperation.to_json())

# convert the object into a dict
node_power_operation_dict = node_power_operation_instance.to_dict()
# create an instance of NodePowerOperation from a dict
node_power_operation_from_dict = NodePowerOperation.from_dict(node_power_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


