# RecoverGoogleDriveParams

Specifies the parameters to recover an Google Drive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other Google Drive items if one of items failed to recover. Default value is false. | [optional] 
**objects** | [**List[ObjectGoogleDriveParams]**](ObjectGoogleDriveParams.md) | Specifies a list of Google Drive params associated with the objects to recover. | 
**target_drive** | [**TargetGoogleDriveParams**](TargetGoogleDriveParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_google_drive_params import RecoverGoogleDriveParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGoogleDriveParams from a JSON string
recover_google_drive_params_instance = RecoverGoogleDriveParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGoogleDriveParams.to_json())

# convert the object into a dict
recover_google_drive_params_dict = recover_google_drive_params_instance.to_dict()
# create an instance of RecoverGoogleDriveParams from a dict
recover_google_drive_params_from_dict = RecoverGoogleDriveParams.from_dict(recover_google_drive_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


