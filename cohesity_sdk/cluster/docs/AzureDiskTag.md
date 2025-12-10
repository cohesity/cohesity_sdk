# AzureDiskTag

A key - value pair tag that may be specified on Azure Disks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key of the tag specified on the azure disk. | [optional] 
**value** | **str** | Value of the tag specified on the azure disk. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_disk_tag import AzureDiskTag

# TODO update the JSON string below
json = "{}"
# create an instance of AzureDiskTag from a JSON string
azure_disk_tag_instance = AzureDiskTag.from_json(json)
# print the JSON string representation of the object
print(AzureDiskTag.to_json())

# convert the object into a dict
azure_disk_tag_dict = azure_disk_tag_instance.to_dict()
# create an instance of AzureDiskTag from a dict
azure_disk_tag_from_dict = AzureDiskTag.from_dict(azure_disk_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


