# PhysicalFileProtectionGroupObjectParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_vss_writers** | **List[str]** | Specifies writer names which should be excluded from physical file based backups. | [optional] 
**file_paths** | [**List[PhysicalFileBackupPathParams]**](PhysicalFileBackupPathParams.md) | Specifies a list of file paths to be protected by this Protection Group. | [optional] 
**follow_nas_symlink_target** | **bool** | Specifies whether to follow NAS target pointed by symlink for windows sources. | [optional] 
**id** | **int** | Specifies the ID of the object protected. | 
**metadata_file_path** | **str** | Specifies the path of metadatafile on source. This file contains absolute paths of files that needs to be backed up on the same source. | [optional] 
**name** | **str** | Specifies the name of the object protected. | [optional] [readonly] 
**nested_volume_types_to_skip** | **List[str]** | Specifies mount types of nested volumes to be skipped. | [optional] 
**uses_path_level_skip_nested_volume_setting** | **bool** | Specifies whether path level or object level skip nested volume setting will be used. | [optional] 

## Example

```python
from cohesity_sdk.models.physical_file_protection_group_object_params import PhysicalFileProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalFileProtectionGroupObjectParams from a JSON string
physical_file_protection_group_object_params_instance = PhysicalFileProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(PhysicalFileProtectionGroupObjectParams.to_json())

# convert the object into a dict
physical_file_protection_group_object_params_dict = physical_file_protection_group_object_params_instance.to_dict()
# create an instance of PhysicalFileProtectionGroupObjectParams from a dict
physical_file_protection_group_object_params_from_dict = PhysicalFileProtectionGroupObjectParams.from_dict(physical_file_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


