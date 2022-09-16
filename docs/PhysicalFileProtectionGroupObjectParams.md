# PhysicalFileProtectionGroupObjectParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object protected. | 
**name** | **str, none_type** | Specifies the name of the object protected. | [optional] [readonly] 
**file_paths** | [**[PhysicalFileBackupPathParams]**](PhysicalFileBackupPathParams.md) | Specifies a list of file paths to be protected by this Protection Group. | [optional] 
**uses_path_level_skip_nested_volume_setting** | **bool, none_type** | Specifies whether path level or object level skip nested volume setting will be used. | [optional] 
**nested_volume_types_to_skip** | **[str]** | Specifies mount types of nested volumes to be skipped. | [optional] 
**follow_nas_symlink_target** | **bool, none_type** | Specifies whether to follow NAS target pointed by symlink for windows sources. | [optional] 
**metadata_file_path** | **str, none_type** | Specifies the path of metadatafile on source. This file contains absolute paths of files that needs to be backed up on the same source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


