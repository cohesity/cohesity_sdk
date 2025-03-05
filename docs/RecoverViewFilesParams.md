# RecoverViewFilesParams

Specifies the parameters to recover View files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files_and_folders** | [**List[ViewRecoverFileAndFolderInfo]**](ViewRecoverFileAndFolderInfo.md) | Specifies the list of info about the view files and folders to be recovered. | 
**view_target_params** | [**RecoverViewToViewFilesTargetParams**](RecoverViewToViewFilesTargetParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.recover_view_files_params import RecoverViewFilesParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverViewFilesParams from a JSON string
recover_view_files_params_instance = RecoverViewFilesParams.from_json(json)
# print the JSON string representation of the object
print(RecoverViewFilesParams.to_json())

# convert the object into a dict
recover_view_files_params_dict = recover_view_files_params_instance.to_dict()
# create an instance of RecoverViewFilesParams from a dict
recover_view_files_params_from_dict = RecoverViewFilesParams.from_dict(recover_view_files_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


