# PhysicalFileBackupPathParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_paths** | **List[str]** | Specifies a set of paths nested under the include path which should be excluded from the Protection Group. | [optional] 
**included_path** | **str** | Specifies a path to be included on the source. All paths under this path will be included unless they are specifically mentioned in excluded paths. | 
**skip_nested_volumes** | **bool** | Specifies whether to skip any nested volumes (both local and network) that are mounted under include path. Applicable only for windows sources. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.physical_file_backup_path_params import PhysicalFileBackupPathParams

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalFileBackupPathParams from a JSON string
physical_file_backup_path_params_instance = PhysicalFileBackupPathParams.from_json(json)
# print the JSON string representation of the object
print(PhysicalFileBackupPathParams.to_json())

# convert the object into a dict
physical_file_backup_path_params_dict = physical_file_backup_path_params_instance.to_dict()
# create an instance of PhysicalFileBackupPathParams from a dict
physical_file_backup_path_params_from_dict = PhysicalFileBackupPathParams.from_dict(physical_file_backup_path_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


