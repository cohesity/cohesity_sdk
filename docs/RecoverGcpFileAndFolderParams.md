# RecoverGcpFileAndFolderParams

Specifies the parameters to recover files and folders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files_and_folders** | [**List[CommonRecoverFileAndFolderInfo]**](CommonRecoverFileAndFolderInfo.md) | Specifies the info about the files and folders to be recovered. | 
**gcp_target_params** | [**GcpTargetParamsForRecoverFileAndFolder**](GcpTargetParamsForRecoverFileAndFolder.md) |  | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_gcp_file_and_folder_params import RecoverGcpFileAndFolderParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGcpFileAndFolderParams from a JSON string
recover_gcp_file_and_folder_params_instance = RecoverGcpFileAndFolderParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGcpFileAndFolderParams.to_json())

# convert the object into a dict
recover_gcp_file_and_folder_params_dict = recover_gcp_file_and_folder_params_instance.to_dict()
# create an instance of RecoverGcpFileAndFolderParams from a dict
recover_gcp_file_and_folder_params_from_dict = RecoverGcpFileAndFolderParams.from_dict(recover_gcp_file_and_folder_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


