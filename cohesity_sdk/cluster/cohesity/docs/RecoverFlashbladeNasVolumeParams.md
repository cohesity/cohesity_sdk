# RecoverFlashbladeNasVolumeParams

Specifies the parameters to recover Flashblade NAS volumes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 
**elastifile_target_params** | [**RecoverOtherNasToElastifileVolumeTargetParams**](RecoverOtherNasToElastifileVolumeTargetParams.md) |  | [optional] 
**flashblade_target_params** | [**RecoverFlashbladeToFlashbladeVolumeTargetParams**](RecoverFlashbladeToFlashbladeVolumeTargetParams.md) |  | [optional] 
**generic_nas_target_params** | [**RecoverOtherNasToGenericNasVolumeTargetParams**](RecoverOtherNasToGenericNasVolumeTargetParams.md) |  | [optional] 
**gpfs_target_params** | [**RecoverOtherNasToGpfsVolumeTargetParams**](RecoverOtherNasToGpfsVolumeTargetParams.md) |  | [optional] 
**isilon_target_params** | [**RecoverOtherNasToIsilonVolumeTargetParams**](RecoverOtherNasToIsilonVolumeTargetParams.md) |  | [optional] 
**netapp_target_params** | [**RecoverOtherNasToNetappVolumeTargetParams**](RecoverOtherNasToNetappVolumeTargetParams.md) |  | [optional] 
**view_target_params** | [**RecoverNasVolumeToViewParams**](RecoverNasVolumeToViewParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


