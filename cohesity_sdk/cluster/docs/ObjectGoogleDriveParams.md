# ObjectGoogleDriveParams

Specifies Google Drive recovery parameters associated with a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google_drive_params** | [**List[GoogleDriveParams]**](GoogleDriveParams.md) | Specifies parameters to recover a Google Drive. | [optional] 
**owner_info** | [**CommonRecoverObjectSnapshotParams**](CommonRecoverObjectSnapshotParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.object_google_drive_params import ObjectGoogleDriveParams

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectGoogleDriveParams from a JSON string
object_google_drive_params_instance = ObjectGoogleDriveParams.from_json(json)
# print the JSON string representation of the object
print(ObjectGoogleDriveParams.to_json())

# convert the object into a dict
object_google_drive_params_dict = object_google_drive_params_instance.to_dict()
# create an instance of ObjectGoogleDriveParams from a dict
object_google_drive_params_from_dict = ObjectGoogleDriveParams.from_dict(object_google_drive_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


