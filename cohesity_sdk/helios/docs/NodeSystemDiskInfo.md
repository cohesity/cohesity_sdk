# NodeSystemDiskInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_path** | **str** | DevicePath is the device path of the disk. | [optional] 
**id** | **int** | Id is the id of the disk. | [optional] 
**offline** | **bool** | Offline specifies whether a disk is marked offline. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.node_system_disk_info import NodeSystemDiskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NodeSystemDiskInfo from a JSON string
node_system_disk_info_instance = NodeSystemDiskInfo.from_json(json)
# print the JSON string representation of the object
print(NodeSystemDiskInfo.to_json())

# convert the object into a dict
node_system_disk_info_dict = node_system_disk_info_instance.to_dict()
# create an instance of NodeSystemDiskInfo from a dict
node_system_disk_info_from_dict = NodeSystemDiskInfo.from_dict(node_system_disk_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


