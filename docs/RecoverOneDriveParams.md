# RecoverOneDriveParams

Specifies the parameters to recover an Office 365 OneDrive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other OneDrive items if one of items failed to recover. Default value is false. | [optional] 
**objects** | [**List[ObjectOneDriveParam]**](ObjectOneDriveParam.md) | Specifies a list of OneDrive params associated with the objects to recover. These parameters allow overriding the request level &#39;recoverUserDefaultDrive&#39; parameter for each object specified here. | 
**recover_preservation_hold_library** | **bool** | Specifies whether to recover Preservation Hold Library associated with the OneDrives selected for restore. Default value is false. | [optional] 
**recover_user_default_drive** | **bool** | Specifies whether to recover default drives associated with the OneDrives selected for restore. Default value is true. This setting can be overridden for each object selected for recovery, by specifying &#39;recoverEntireDrive&#39; for the desired drive within &#39;oneDriveParams&#39;. Granular recovery is still allowed even if this value is set to true. | [optional] 
**target_drive** | [**TargetOneDriveParam**](TargetOneDriveParam.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.recover_one_drive_params import RecoverOneDriveParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverOneDriveParams from a JSON string
recover_one_drive_params_instance = RecoverOneDriveParams.from_json(json)
# print the JSON string representation of the object
print(RecoverOneDriveParams.to_json())

# convert the object into a dict
recover_one_drive_params_dict = recover_one_drive_params_instance.to_dict()
# create an instance of RecoverOneDriveParams from a dict
recover_one_drive_params_from_dict = RecoverOneDriveParams.from_dict(recover_one_drive_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


