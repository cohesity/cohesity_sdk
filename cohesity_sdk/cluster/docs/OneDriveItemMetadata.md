# OneDriveItemMetadata

Info about a onedrive item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Specifies the type of the OneDrive item | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.one_drive_item_metadata import OneDriveItemMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of OneDriveItemMetadata from a JSON string
one_drive_item_metadata_instance = OneDriveItemMetadata.from_json(json)
# print the JSON string representation of the object
print(OneDriveItemMetadata.to_json())

# convert the object into a dict
one_drive_item_metadata_dict = one_drive_item_metadata_instance.to_dict()
# create an instance of OneDriveItemMetadata from a dict
one_drive_item_metadata_from_dict = OneDriveItemMetadata.from_dict(one_drive_item_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


