# RecoverElastifileFilesParams

Specifies the parameters to recover Elastifile files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elastifile_target_params** | [**RecoverElastifileToElastifileFilesTargetParams**](RecoverElastifileToElastifileFilesTargetParams.md) |  | [optional] 
**files_and_folders** | [**List[CommonRecoverFileAndFolderInfo]**](CommonRecoverFileAndFolderInfo.md) | Specifies the info about the files and folders to be recovered. | 
**flashblade_target_params** | [**RecoverOtherNasToFlashbladeFilesTargetParams**](RecoverOtherNasToFlashbladeFilesTargetParams.md) |  | [optional] 
**generic_nas_target_params** | [**RecoverOtherNasToGenericNasFilesTargetParams**](RecoverOtherNasToGenericNasFilesTargetParams.md) |  | [optional] 
**gpfs_target_params** | [**RecoverOtherNasToGpfsFilesTargetParams**](RecoverOtherNasToGpfsFilesTargetParams.md) |  | [optional] 
**isilon_target_params** | [**RecoverOtherNasToIsilonFilesTargetParams**](RecoverOtherNasToIsilonFilesTargetParams.md) |  | [optional] 
**netapp_target_params** | [**RecoverOtherNasToNetappFilesTargetParams**](RecoverOtherNasToNetappFilesTargetParams.md) |  | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.models.recover_elastifile_files_params import RecoverElastifileFilesParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverElastifileFilesParams from a JSON string
recover_elastifile_files_params_instance = RecoverElastifileFilesParams.from_json(json)
# print the JSON string representation of the object
print(RecoverElastifileFilesParams.to_json())

# convert the object into a dict
recover_elastifile_files_params_dict = recover_elastifile_files_params_instance.to_dict()
# create an instance of RecoverElastifileFilesParams from a dict
recover_elastifile_files_params_from_dict = RecoverElastifileFilesParams.from_dict(recover_elastifile_files_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


