# CloneViewDirectoryParams

Specifies the parameters to clone View directory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_directory_path** | **str** | Specifies the path of source directory. This is the full path including the Storage Domain name and View name. | 
**target_directory_name** | **str** | Specifies the name of the target directory. | 
**target_parent_directory_path** | **str** | Specifies the path of parent directory of the target directory. This is the full path including the Storage Domain name and View Name. | 

## Example

```python
from cohesity_sdk.cluster.models.clone_view_directory_params import CloneViewDirectoryParams

# TODO update the JSON string below
json = "{}"
# create an instance of CloneViewDirectoryParams from a JSON string
clone_view_directory_params_instance = CloneViewDirectoryParams.from_json(json)
# print the JSON string representation of the object
print(CloneViewDirectoryParams.to_json())

# convert the object into a dict
clone_view_directory_params_dict = clone_view_directory_params_instance.to_dict()
# create an instance of CloneViewDirectoryParams from a dict
clone_view_directory_params_from_dict = CloneViewDirectoryParams.from_dict(clone_view_directory_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


