# OriginalViewFilesTargetParams

Specifies the params of the original View recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_original_path** | **bool, none_type** | Specifies whether to recover files and folders to the original path location. If false, alternatePath must be specified. | 
**alternate_path** | **str, none_type** | Specifies the alternate path location to recover files to. | [optional] 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other files if one of the files fails to recover. Default value is false. | [optional] 
**overwrite_existing_file** | **bool, none_type** | Specifies whether to overwrite existing file/folder during recovery. | [optional] 
**preserve_file_attributes** | **bool, none_type** | Specifies whether to preserve file/folder attributes during recovery. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


