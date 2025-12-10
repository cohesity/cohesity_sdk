# FileStubbingParams

File stubbing params

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_orphan_data_cleanup** | **bool** | Specifies whether to remove the orphan data from the target if the symlink is removed from the source. | [optional] [default to True]
**downtiering_file_age** | [**DowntieringFileAgePolicy**](DowntieringFileAgePolicy.md) |  | [optional] 
**skip_back_symlink** | **bool** | Specifies whether to create a symlink for the migrated data from source to target. | [optional] [default to True]

## Example

```python
from cohesity_sdk.cluster.models.file_stubbing_params import FileStubbingParams

# TODO update the JSON string below
json = "{}"
# create an instance of FileStubbingParams from a JSON string
file_stubbing_params_instance = FileStubbingParams.from_json(json)
# print the JSON string representation of the object
print(FileStubbingParams.to_json())

# convert the object into a dict
file_stubbing_params_dict = file_stubbing_params_instance.to_dict()
# create an instance of FileStubbingParams from a dict
file_stubbing_params_from_dict = FileStubbingParams.from_dict(file_stubbing_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


