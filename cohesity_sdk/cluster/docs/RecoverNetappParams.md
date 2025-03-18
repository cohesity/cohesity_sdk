# RecoverNetappParams

Specifies the recovery options specific to Netapp environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | 
**recover_file_and_folder_params** | [**RecoverNetappFilesParams**](RecoverNetappFilesParams.md) |  | [optional] 
**recover_nas_volume_params** | [**RecoverNetappNasVolumeParams**](RecoverNetappNasVolumeParams.md) |  | [optional] 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_netapp_params import RecoverNetappParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverNetappParams from a JSON string
recover_netapp_params_instance = RecoverNetappParams.from_json(json)
# print the JSON string representation of the object
print(RecoverNetappParams.to_json())

# convert the object into a dict
recover_netapp_params_dict = recover_netapp_params_instance.to_dict()
# create an instance of RecoverNetappParams from a dict
recover_netapp_params_from_dict = RecoverNetappParams.from_dict(recover_netapp_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


