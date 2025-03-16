# RecoverGpfsFilesParams

Specifies the parameters to recover Gpfs files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elastifile_target_params** | [**RecoverOtherNasToElastifileFilesTargetParams**](RecoverOtherNasToElastifileFilesTargetParams.md) | Specifies the params for an Elastifile recovery target. | [optional] 
**files_and_folders** | [**List[CommonRecoverFileAndFolderInfo]**](CommonRecoverFileAndFolderInfo.md) | Specifies the info about the files and folders to be recovered. | 
**flashblade_target_params** | [**RecoverOtherNasToFlashbladeFilesTargetParams**](RecoverOtherNasToFlashbladeFilesTargetParams.md) | Specifies the params for a Flashblade recovery target. | [optional] 
**generic_nas_target_params** | [**RecoverOtherNasToGenericNasFilesTargetParams**](RecoverOtherNasToGenericNasFilesTargetParams.md) | Specifies the params for a generic NAS recovery target. | [optional] 
**gpfs_target_params** | [**RecoverGpfsToGpfsFilesTargetParams**](RecoverGpfsToGpfsFilesTargetParams.md) | Specifies the params for a GPFS recovery target. | [optional] 
**isilon_target_params** | [**RecoverOtherNasToIsilonFilesTargetParams**](RecoverOtherNasToIsilonFilesTargetParams.md) | Specifies the params for a Isilon recovery target. | [optional] 
**netapp_target_params** | [**RecoverOtherNasToNetappFilesTargetParams**](RecoverOtherNasToNetappFilesTargetParams.md) | Specifies the params for an Netapp recovery target. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.helios.models.recover_gpfs_files_params import RecoverGpfsFilesParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGpfsFilesParams from a JSON string
recover_gpfs_files_params_instance = RecoverGpfsFilesParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGpfsFilesParams.to_json())

# convert the object into a dict
recover_gpfs_files_params_dict = recover_gpfs_files_params_instance.to_dict()
# create an instance of RecoverGpfsFilesParams from a dict
recover_gpfs_files_params_from_dict = RecoverGpfsFilesParams.from_dict(recover_gpfs_files_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


