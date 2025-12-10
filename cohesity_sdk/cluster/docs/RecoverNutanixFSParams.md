# RecoverNutanixFSParams

Specifies the recovery options specific to NutanixFS environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | 
**recover_file_and_folder_params** | [**RecoverNutanixFSFilesParams**](RecoverNutanixFSFilesParams.md) |  | [optional] 
**recover_nas_volume_params** | [**RecoverNutanixFSNasVolumeParams**](RecoverNutanixFSNasVolumeParams.md) |  | [optional] 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_nutanix_fs_params import RecoverNutanixFSParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverNutanixFSParams from a JSON string
recover_nutanix_fs_params_instance = RecoverNutanixFSParams.from_json(json)
# print the JSON string representation of the object
print(RecoverNutanixFSParams.to_json())

# convert the object into a dict
recover_nutanix_fs_params_dict = recover_nutanix_fs_params_instance.to_dict()
# create an instance of RecoverNutanixFSParams from a dict
recover_nutanix_fs_params_from_dict = RecoverNutanixFSParams.from_dict(recover_nutanix_fs_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


