# GoogleDriveParams

Specifies parameters to recover a Google Drive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Specifies the Google Drive id. | [optional] 
**name** | **str** | Specifies the Google Drive name. | [optional] 
**recover_entire_drive** | **bool** | Specifies whether to recover the whole Google Drive. This is set to false when excluding recovering specific drive items. | [optional] 
**recover_items** | [**List[GoogleDriveItem]**](GoogleDriveItem.md) | Specifies a list of Google Drive items to recover. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.google_drive_params import GoogleDriveParams

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleDriveParams from a JSON string
google_drive_params_instance = GoogleDriveParams.from_json(json)
# print the JSON string representation of the object
print(GoogleDriveParams.to_json())

# convert the object into a dict
google_drive_params_dict = google_drive_params_instance.to_dict()
# create an instance of GoogleDriveParams from a dict
google_drive_params_from_dict = GoogleDriveParams.from_dict(google_drive_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


