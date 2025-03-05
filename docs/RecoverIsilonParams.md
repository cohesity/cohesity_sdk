# RecoverIsilonParams

Specifies the recovery options specific to Isilon environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | 
**recover_file_and_folder_params** | [**RecoverIsilonFilesParams**](RecoverIsilonFilesParams.md) |  | [optional] 
**recover_nas_volume_params** | [**RecoverIsilonNasVolumeParams**](RecoverIsilonNasVolumeParams.md) |  | [optional] 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.models.recover_isilon_params import RecoverIsilonParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverIsilonParams from a JSON string
recover_isilon_params_instance = RecoverIsilonParams.from_json(json)
# print the JSON string representation of the object
print(RecoverIsilonParams.to_json())

# convert the object into a dict
recover_isilon_params_dict = recover_isilon_params_instance.to_dict()
# create an instance of RecoverIsilonParams from a dict
recover_isilon_params_from_dict = RecoverIsilonParams.from_dict(recover_isilon_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


