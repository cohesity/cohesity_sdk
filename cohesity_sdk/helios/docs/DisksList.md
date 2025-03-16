# DisksList

Specifies the list of disks that belong to node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disks_list** | [**List[Disk]**](Disk.md) | Specifies the list of disks. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.disks_list import DisksList

# TODO update the JSON string below
json = "{}"
# create an instance of DisksList from a JSON string
disks_list_instance = DisksList.from_json(json)
# print the JSON string representation of the object
print(DisksList.to_json())

# convert the object into a dict
disks_list_dict = disks_list_instance.to_dict()
# create an instance of DisksList from a dict
disks_list_from_dict = DisksList.from_dict(disks_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


