# RecoverHyperVFileAndFolderParams

Specifies the parameters to recover files and folders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files_and_folders** | [**List[CommonRecoverFileAndFolderInfo]**](CommonRecoverFileAndFolderInfo.md) | Specifies the info about the files and folders to be recovered. | 
**hyperv_target_params** | [**HyperVTargetParamsForRecoverFileAndFolder**](HyperVTargetParamsForRecoverFileAndFolder.md) | Specifies the parameters to recover to a HyperV target. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.helios.models.recover_hyper_v_file_and_folder_params import RecoverHyperVFileAndFolderParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverHyperVFileAndFolderParams from a JSON string
recover_hyper_v_file_and_folder_params_instance = RecoverHyperVFileAndFolderParams.from_json(json)
# print the JSON string representation of the object
print(RecoverHyperVFileAndFolderParams.to_json())

# convert the object into a dict
recover_hyper_v_file_and_folder_params_dict = recover_hyper_v_file_and_folder_params_instance.to_dict()
# create an instance of RecoverHyperVFileAndFolderParams from a dict
recover_hyper_v_file_and_folder_params_from_dict = RecoverHyperVFileAndFolderParams.from_dict(recover_hyper_v_file_and_folder_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


