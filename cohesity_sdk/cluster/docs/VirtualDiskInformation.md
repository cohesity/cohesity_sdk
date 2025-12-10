# VirtualDiskInformation

Specifies the details about a Virtual Disk within a VM, containing basic info about it and its corresponding controller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_id** | **str** | Specifies original disk id. This is sufficient to identify the disk information. | [optional] 
**disk_info** | [**DiskInfo**](DiskInfo.md) |  | [optional] 
**disk_location** | [**Object**](Object.md) |  | [optional] 
**disk_size_in_bytes** | **int** | Specifies size of the virtual disk in bytes. | [optional] 
**file_path** | **str** | Specifies the original file path if applicable. | [optional] 
**mount_points** | **List[str]** | Specifies the list of mount points. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.virtual_disk_information import VirtualDiskInformation

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskInformation from a JSON string
virtual_disk_information_instance = VirtualDiskInformation.from_json(json)
# print the JSON string representation of the object
print(VirtualDiskInformation.to_json())

# convert the object into a dict
virtual_disk_information_dict = virtual_disk_information_instance.to_dict()
# create an instance of VirtualDiskInformation from a dict
virtual_disk_information_from_dict = VirtualDiskInformation.from_dict(virtual_disk_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


