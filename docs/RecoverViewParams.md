# RecoverViewParams

Specifies the recovery options specific to View environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | [optional] 
**recover_file_and_folder_params** | [**RecoverViewFilesParams**](RecoverViewFilesParams.md) |  | [optional] 
**recovery_action** | **str** | Specifies the type of recovery action to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_view_params import RecoverViewParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverViewParams from a JSON string
recover_view_params_instance = RecoverViewParams.from_json(json)
# print the JSON string representation of the object
print(RecoverViewParams.to_json())

# convert the object into a dict
recover_view_params_dict = recover_view_params_instance.to_dict()
# create an instance of RecoverViewParams from a dict
recover_view_params_from_dict = RecoverViewParams.from_dict(recover_view_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


