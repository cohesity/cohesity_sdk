# RecoverAcropolisFileAndFolderParams

Specifies the parameters to recover Acropolis files and folders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acropolis_target_params** | [**AcropolisTargetParamsForRecoverFileAndFolder**](AcropolisTargetParamsForRecoverFileAndFolder.md) |  | [optional] 
**files_and_folders** | [**List[CommonRecoverFileAndFolderInfo]**](CommonRecoverFileAndFolderInfo.md) | Specifies the info about the files and folders to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_acropolis_file_and_folder_params import RecoverAcropolisFileAndFolderParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAcropolisFileAndFolderParams from a JSON string
recover_acropolis_file_and_folder_params_instance = RecoverAcropolisFileAndFolderParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAcropolisFileAndFolderParams.to_json())

# convert the object into a dict
recover_acropolis_file_and_folder_params_dict = recover_acropolis_file_and_folder_params_instance.to_dict()
# create an instance of RecoverAcropolisFileAndFolderParams from a dict
recover_acropolis_file_and_folder_params_from_dict = RecoverAcropolisFileAndFolderParams.from_dict(recover_acropolis_file_and_folder_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


