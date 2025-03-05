# OriginalViewFilesTargetParams

Specifies the params of the original View recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_path** | **str** | Specifies the alternate path location to recover files to. | [optional] 
**continue_on_error** | **bool** | Specifies whether to continue recovering other files if one of the files fails to recover. Default value is false. | [optional] 
**overwrite_existing_file** | **bool** | Specifies whether to overwrite existing file/folder during recovery. | [optional] 
**preserve_file_attributes** | **bool** | Specifies whether to preserve file/folder attributes during recovery. | [optional] 
**recover_to_original_path** | **bool** | Specifies whether to recover files and folders to the original path location. If false, alternatePath must be specified. | 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.original_view_files_target_params import OriginalViewFilesTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of OriginalViewFilesTargetParams from a JSON string
original_view_files_target_params_instance = OriginalViewFilesTargetParams.from_json(json)
# print the JSON string representation of the object
print(OriginalViewFilesTargetParams.to_json())

# convert the object into a dict
original_view_files_target_params_dict = original_view_files_target_params_instance.to_dict()
# create an instance of OriginalViewFilesTargetParams from a dict
original_view_files_target_params_from_dict = OriginalViewFilesTargetParams.from_dict(original_view_files_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


