# RecoverPhysicalFileAndFolderParams

Specifies the parameters to recover files and folders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files_and_folders** | [**List[CommonRecoverFileAndFolderInfo]**](CommonRecoverFileAndFolderInfo.md) | Specifies the information about the files and folders to be recovered. | 
**physical_target_params** | [**PhysicalTargetParamsForRecoverFileAndFolder**](PhysicalTargetParamsForRecoverFileAndFolder.md) |  | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.models.recover_physical_file_and_folder_params import RecoverPhysicalFileAndFolderParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverPhysicalFileAndFolderParams from a JSON string
recover_physical_file_and_folder_params_instance = RecoverPhysicalFileAndFolderParams.from_json(json)
# print the JSON string representation of the object
print(RecoverPhysicalFileAndFolderParams.to_json())

# convert the object into a dict
recover_physical_file_and_folder_params_dict = recover_physical_file_and_folder_params_instance.to_dict()
# create an instance of RecoverPhysicalFileAndFolderParams from a dict
recover_physical_file_and_folder_params_from_dict = RecoverPhysicalFileAndFolderParams.from_dict(recover_physical_file_and_folder_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


