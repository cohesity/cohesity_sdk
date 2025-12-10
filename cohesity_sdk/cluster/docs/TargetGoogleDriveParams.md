# TargetGoogleDriveParams

Specifies the target Google Drive to recover to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the target Google Drive. | [optional] 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.target_google_drive_params import TargetGoogleDriveParams

# TODO update the JSON string below
json = "{}"
# create an instance of TargetGoogleDriveParams from a JSON string
target_google_drive_params_instance = TargetGoogleDriveParams.from_json(json)
# print the JSON string representation of the object
print(TargetGoogleDriveParams.to_json())

# convert the object into a dict
target_google_drive_params_dict = target_google_drive_params_instance.to_dict()
# create an instance of TargetGoogleDriveParams from a dict
target_google_drive_params_from_dict = TargetGoogleDriveParams.from_dict(target_google_drive_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


