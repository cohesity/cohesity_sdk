# GoogleDriveItem

Specifies a Google Drive item to recover.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Specifies the item id. | [optional] 
**is_file** | **bool** | Specifies if the item is a file. | [optional] 
**item_path** | **str** | Specifies the path to the Google Drive item. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.google_drive_item import GoogleDriveItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleDriveItem from a JSON string
google_drive_item_instance = GoogleDriveItem.from_json(json)
# print the JSON string representation of the object
print(GoogleDriveItem.to_json())

# convert the object into a dict
google_drive_item_dict = google_drive_item_instance.to_dict()
# create an instance of GoogleDriveItem from a dict
google_drive_item_from_dict = GoogleDriveItem.from_dict(google_drive_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


