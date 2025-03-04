# RecoverNetappFilesParams

Specifies the parameters to recover Netapp files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elastifile_target_params** | [**RecoverOtherNasToElastifileFilesTargetParams**](RecoverOtherNasToElastifileFilesTargetParams.md) |  | [optional] 
**files_and_folders** | [**List[NetappRecoverFileAndFolderInfo]**](NetappRecoverFileAndFolderInfo.md) | Specifies the list of info about the netapp files and folders to be recovered. | 
**flashblade_target_params** | [**RecoverOtherNasToFlashbladeFilesTargetParams**](RecoverOtherNasToFlashbladeFilesTargetParams.md) |  | [optional] 
**generic_nas_target_params** | [**RecoverOtherNasToGenericNasFilesTargetParams**](RecoverOtherNasToGenericNasFilesTargetParams.md) |  | [optional] 
**gpfs_target_params** | [**RecoverOtherNasToGpfsFilesTargetParams**](RecoverOtherNasToGpfsFilesTargetParams.md) |  | [optional] 
**is_from_source_initiated_protection** | **bool** | Specifies if the snapshot trying to recover is from a source initiated protection. | [optional] 
**isilon_target_params** | [**RecoverOtherNasToIsilonFilesTargetParams**](RecoverOtherNasToIsilonFilesTargetParams.md) |  | [optional] 
**netapp_target_params** | [**RecoverNetappToNetappFilesTargetParams**](RecoverNetappToNetappFilesTargetParams.md) |  | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.models.recover_netapp_files_params import RecoverNetappFilesParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverNetappFilesParams from a JSON string
recover_netapp_files_params_instance = RecoverNetappFilesParams.from_json(json)
# print the JSON string representation of the object
print(RecoverNetappFilesParams.to_json())

# convert the object into a dict
recover_netapp_files_params_dict = recover_netapp_files_params_instance.to_dict()
# create an instance of RecoverNetappFilesParams from a dict
recover_netapp_files_params_from_dict = RecoverNetappFilesParams.from_dict(recover_netapp_files_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


