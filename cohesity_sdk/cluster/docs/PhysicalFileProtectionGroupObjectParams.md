# PhysicalFileProtectionGroupObjectParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object protected. | 
**excluded_vss_writers** | **[str], none_type** | Specifies writer names which should be excluded from physical file based backups. | [optional] 
**file_paths** | [**[PhysicalFileBackupPathParams]**](PhysicalFileBackupPathParams.md) | Specifies a list of file paths to be protected by this Protection Group. | [optional] 
**follow_nas_symlink_target** | **bool, none_type** | Specifies whether to follow NAS target pointed by symlink for windows sources. | [optional] 
**metadata_file_path** | **str, none_type** | Specifies the path of metadatafile on source. This file contains absolute paths of files that needs to be backed up on the same source. | [optional] 
**name** | **str, none_type** | Specifies the name of the object protected. | [optional] [readonly] 
**nested_volume_types_to_skip** | **[str]** | Specifies mount types of nested volumes to be skipped. | [optional] 
**uses_path_level_skip_nested_volume_setting** | **bool, none_type** | Specifies whether path level or object level skip nested volume setting will be used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


