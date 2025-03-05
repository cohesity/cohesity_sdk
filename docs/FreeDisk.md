# FreeDisk

Specifies the details of a free disk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | Specifies the location of disk. | [optional] 
**path** | **str** | Specifies path of disk. | [optional] 
**serial_number** | **str** | Specifies serial number of disk. | 
**size_in_bytes** | **int** | Size of disk. | [optional] 

## Example

```python
from cohesity_sdk.models.free_disk import FreeDisk

# TODO update the JSON string below
json = "{}"
# create an instance of FreeDisk from a JSON string
free_disk_instance = FreeDisk.from_json(json)
# print the JSON string representation of the object
print(FreeDisk.to_json())

# convert the object into a dict
free_disk_dict = free_disk_instance.to_dict()
# create an instance of FreeDisk from a dict
free_disk_from_dict = FreeDisk.from_dict(free_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


