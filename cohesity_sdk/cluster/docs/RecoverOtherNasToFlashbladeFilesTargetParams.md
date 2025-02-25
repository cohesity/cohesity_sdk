# RecoverOtherNasToFlashbladeFilesTargetParams

Specifies the params of the Flashblade recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_path** | **str, none_type** | Specifies the path location to recover files to. | 
**volume** | [**RecoverTarget**](RecoverTarget.md) |  | 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other files if one of the files fails to recover. Default value is false. | [optional] 
**encryption_enabled** | **bool, none_type** | Specifies whether encryption should be enabled during recovery. | [optional] 
**filter_ip_config** | [**FilterIpConfig**](FilterIpConfig.md) |  | [optional] 
**overwrite_existing_file** | **bool, none_type** | Specifies whether to overwrite existing file/folder during recovery. | [optional] 
**parent_source** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the id of the parent source of the recovery target. | [optional] 
**preserve_file_attributes** | **bool, none_type** | Specifies whether to preserve file/folder attributes during recovery. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


