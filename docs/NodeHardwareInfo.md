# NodeHardwareInfo

NodeHardwareInfo provides the information regarding the hardware.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **str** | Cpu provides the information regarding the CPU. | [optional] 
**memory_size_bytes** | **int** | MemorySizeBytes provides the memory size in bytes. | [optional] 
**network** | **str** | Network provides the information regarding the network cards. | [optional] 

## Example

```python
from cohesity_sdk.models.node_hardware_info import NodeHardwareInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NodeHardwareInfo from a JSON string
node_hardware_info_instance = NodeHardwareInfo.from_json(json)
# print the JSON string representation of the object
print(NodeHardwareInfo.to_json())

# convert the object into a dict
node_hardware_info_dict = node_hardware_info_instance.to_dict()
# create an instance of NodeHardwareInfo from a dict
node_hardware_info_from_dict = NodeHardwareInfo.from_dict(node_hardware_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


