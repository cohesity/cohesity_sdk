# RecoverAzureFileAndFolderParams

Specifies the parameters to recover Azure files and folders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_target_params** | [**AzureTargetParamsForRecoverFileAndFolder**](AzureTargetParamsForRecoverFileAndFolder.md) |  | [optional] 
**files_and_folders** | [**List[CommonRecoverFileAndFolderInfo]**](CommonRecoverFileAndFolderInfo.md) | Specifies the info about the files and folders to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.models.recover_azure_file_and_folder_params import RecoverAzureFileAndFolderParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureFileAndFolderParams from a JSON string
recover_azure_file_and_folder_params_instance = RecoverAzureFileAndFolderParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureFileAndFolderParams.to_json())

# convert the object into a dict
recover_azure_file_and_folder_params_dict = recover_azure_file_and_folder_params_instance.to_dict()
# create an instance of RecoverAzureFileAndFolderParams from a dict
recover_azure_file_and_folder_params_from_dict = RecoverAzureFileAndFolderParams.from_dict(recover_azure_file_and_folder_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


