# HyperVDiskInfo

Specifies information about a disk to be filtered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_number** | **int** | Specifies the disk controller number. | 
**controller_type** | **str** | Specifies the disk controller type. | 
**unit_number** | **int** | Specifies the disk index number. | 

## Example

```python
from cohesity_sdk.models.hyper_v_disk_info import HyperVDiskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HyperVDiskInfo from a JSON string
hyper_v_disk_info_instance = HyperVDiskInfo.from_json(json)
# print the JSON string representation of the object
print(HyperVDiskInfo.to_json())

# convert the object into a dict
hyper_v_disk_info_dict = hyper_v_disk_info_instance.to_dict()
# create an instance of HyperVDiskInfo from a dict
hyper_v_disk_info_from_dict = HyperVDiskInfo.from_dict(hyper_v_disk_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


