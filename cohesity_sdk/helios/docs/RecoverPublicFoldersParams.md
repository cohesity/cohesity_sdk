# RecoverPublicFoldersParams

Specifies the parameters to recover Office 365 Public Folders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other Public Folders if one of Public Folder failed to recover. Default value is false. | [optional] 
**root_public_folders** | [**List[RootPublicFolderParam]**](RootPublicFolderParam.md) | Specifies a list of RootPublicFolder params associated with the objects to recover. | 
**target_folder_path** | **str** | Specifies the path to the target folder. | [optional] 
**target_root_public_folder** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the target RootPublicFolder to recover to. If not specified, the objects will be recovered to original location. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_public_folders_params import RecoverPublicFoldersParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverPublicFoldersParams from a JSON string
recover_public_folders_params_instance = RecoverPublicFoldersParams.from_json(json)
# print the JSON string representation of the object
print(RecoverPublicFoldersParams.to_json())

# convert the object into a dict
recover_public_folders_params_dict = recover_public_folders_params_instance.to_dict()
# create an instance of RecoverPublicFoldersParams from a dict
recover_public_folders_params_from_dict = RecoverPublicFoldersParams.from_dict(recover_public_folders_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


