# RecoverPhysicalParams

Specifies the recovery options specific to Physical environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**mount_volume_params** | [**MountPhysicalVolumeParams**](MountPhysicalVolumeParams.md) |  | [optional] 
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of Recover Object parameters. For recovering files, specifies the object contains the file to recover. | 
**recover_file_and_folder_params** | [**RecoverPhysicalFileAndFolderParams**](RecoverPhysicalFileAndFolderParams.md) |  | [optional] 
**recover_volume_params** | [**RecoverPhysicalVolumeParams**](RecoverPhysicalVolumeParams.md) |  | [optional] 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 
**system_recovery_params** | [**SystemRecoveryParams**](SystemRecoveryParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.recover_physical_params import RecoverPhysicalParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverPhysicalParams from a JSON string
recover_physical_params_instance = RecoverPhysicalParams.from_json(json)
# print the JSON string representation of the object
print(RecoverPhysicalParams.to_json())

# convert the object into a dict
recover_physical_params_dict = recover_physical_params_instance.to_dict()
# create an instance of RecoverPhysicalParams from a dict
recover_physical_params_from_dict = RecoverPhysicalParams.from_dict(recover_physical_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


