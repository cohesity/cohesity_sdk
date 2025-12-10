# RecoverNutanixFSFilesParams

Specifies the parameters to recover NutanixFS files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elastifile_target_params** | [**RecoverOtherNasToElastifileFilesTargetParams**](RecoverOtherNasToElastifileFilesTargetParams.md) |  | [optional] 
**files_and_folders** | [**List[NutanixFSRecoverFileAndFolderInfo]**](NutanixFSRecoverFileAndFolderInfo.md) | Specifies the list of info about the nutanixFS files and folders to be recovered. | 
**flashblade_target_params** | [**RecoverOtherNasToFlashbladeFilesTargetParams**](RecoverOtherNasToFlashbladeFilesTargetParams.md) |  | [optional] 
**generic_nas_target_params** | [**RecoverOtherNasToGenericNasFilesTargetParams**](RecoverOtherNasToGenericNasFilesTargetParams.md) |  | [optional] 
**gpfs_target_params** | [**RecoverOtherNasToGpfsFilesTargetParams**](RecoverOtherNasToGpfsFilesTargetParams.md) |  | [optional] 
**is_from_source_initiated_protection** | **bool** | Specifies if the snapshot trying to recover is from a source initiated protection. | [optional] 
**isilon_target_params** | [**RecoverOtherNasToIsilonFilesTargetParams**](RecoverOtherNasToIsilonFilesTargetParams.md) |  | [optional] 
**netapp_target_params** | [**RecoverOtherNasToNetappFilesTargetParams**](RecoverOtherNasToNetappFilesTargetParams.md) |  | [optional] 
**nutanix_fs_target_params** | [**RecoverNutanixFSToNutanixFSFilesTargetParams**](RecoverNutanixFSToNutanixFSFilesTargetParams.md) |  | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_nutanix_fs_files_params import RecoverNutanixFSFilesParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverNutanixFSFilesParams from a JSON string
recover_nutanix_fs_files_params_instance = RecoverNutanixFSFilesParams.from_json(json)
# print the JSON string representation of the object
print(RecoverNutanixFSFilesParams.to_json())

# convert the object into a dict
recover_nutanix_fs_files_params_dict = recover_nutanix_fs_files_params_instance.to_dict()
# create an instance of RecoverNutanixFSFilesParams from a dict
recover_nutanix_fs_files_params_from_dict = RecoverNutanixFSFilesParams.from_dict(recover_nutanix_fs_files_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


