# RecoverElastifileParams

Specifies the recovery options specific to Elastifile environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) | Specifies the parameters to download files and folders. | [optional] 
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | 
**recover_file_and_folder_params** | [**RecoverElastifileFilesParams**](RecoverElastifileFilesParams.md) | Specifies the parameters to recover files. | [optional] 
**recover_nas_volume_params** | [**RecoverElastifileNasVolumeParams**](RecoverElastifileNasVolumeParams.md) | Specifies the parameters to recover Nas Volumes. | [optional] 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.helios.models.recover_elastifile_params import RecoverElastifileParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverElastifileParams from a JSON string
recover_elastifile_params_instance = RecoverElastifileParams.from_json(json)
# print the JSON string representation of the object
print(RecoverElastifileParams.to_json())

# convert the object into a dict
recover_elastifile_params_dict = recover_elastifile_params_instance.to_dict()
# create an instance of RecoverElastifileParams from a dict
recover_elastifile_params_from_dict = RecoverElastifileParams.from_dict(recover_elastifile_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


