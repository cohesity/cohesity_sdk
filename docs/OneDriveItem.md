# OneDriveItem

Specifies a OneDrive item to recover.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Specifies the item id. | [optional] 
**is_file** | **bool** | Specifies if the item is a file. | [optional] 
**item_path** | **str** | Specifies the path to the OneDrive item. | [optional] 

## Example

```python
from cohesity_sdk.models.one_drive_item import OneDriveItem

# TODO update the JSON string below
json = "{}"
# create an instance of OneDriveItem from a JSON string
one_drive_item_instance = OneDriveItem.from_json(json)
# print the JSON string representation of the object
print(OneDriveItem.to_json())

# convert the object into a dict
one_drive_item_dict = one_drive_item_instance.to_dict()
# create an instance of OneDriveItem from a dict
one_drive_item_from_dict = OneDriveItem.from_dict(one_drive_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


