# RecoverVMwareFileAndFolderParams

Specifies the parameters to recover files and folders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files_and_folders** | [**List[CommonRecoverFileAndFolderInfo]**](CommonRecoverFileAndFolderInfo.md) | Specifies the info about the files and folders to be recovered. | 
**glacier_retrieval_type** | **str** | Specifies the glacier retrieval type when restoring or downloding files or folders from a Glacier-based cloud snapshot. | [optional] 
**parent_recovery_id** | **str** | If current recovery is child task triggered through another parent recovery operation, then this field will specify the id of the parent recovery. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 
**vmware_target_params** | [**VmwareTargetParamsForRecoverFileAndFolder**](VmwareTargetParamsForRecoverFileAndFolder.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_v_mware_file_and_folder_params import RecoverVMwareFileAndFolderParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVMwareFileAndFolderParams from a JSON string
recover_v_mware_file_and_folder_params_instance = RecoverVMwareFileAndFolderParams.from_json(json)
# print the JSON string representation of the object
print(RecoverVMwareFileAndFolderParams.to_json())

# convert the object into a dict
recover_v_mware_file_and_folder_params_dict = recover_v_mware_file_and_folder_params_instance.to_dict()
# create an instance of RecoverVMwareFileAndFolderParams from a dict
recover_v_mware_file_and_folder_params_from_dict = RecoverVMwareFileAndFolderParams.from_dict(recover_v_mware_file_and_folder_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


