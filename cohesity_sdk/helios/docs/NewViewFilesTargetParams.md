# NewViewFilesTargetParams

Specifies the params of the View recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_path** | **str** | Specifies the path location to recover files to. | 
**continue_on_error** | **bool** | Specifies whether to continue recovering other files if one of the files fails to recover. Default value is false. | [optional] 
**overwrite_existing_file** | **bool** | Specifies whether to overwrite existing file/folder during recovery. | [optional] 
**preserve_file_attributes** | **bool** | Specifies whether to preserve file/folder attributes during recovery. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.new_view_files_target_params import NewViewFilesTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of NewViewFilesTargetParams from a JSON string
new_view_files_target_params_instance = NewViewFilesTargetParams.from_json(json)
# print the JSON string representation of the object
print(NewViewFilesTargetParams.to_json())

# convert the object into a dict
new_view_files_target_params_dict = new_view_files_target_params_instance.to_dict()
# create an instance of NewViewFilesTargetParams from a dict
new_view_files_target_params_from_dict = NewViewFilesTargetParams.from_dict(new_view_files_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


