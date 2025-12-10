# FileUptieringParams

File Uptiering parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_all_files** | **bool** | If set, all files in the view will be uptiered regardless of file_select_policy, num_file_access, hot_file_window, file_size constraints. | [optional] [default to False]
**target** | [**DataTieringTarget**](DataTieringTarget.md) |  | [optional] 
**uptiering_file_age** | [**UptieringFileAgePolicy**](UptieringFileAgePolicy.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.file_uptiering_params import FileUptieringParams

# TODO update the JSON string below
json = "{}"
# create an instance of FileUptieringParams from a JSON string
file_uptiering_params_instance = FileUptieringParams.from_json(json)
# print the JSON string representation of the object
print(FileUptieringParams.to_json())

# convert the object into a dict
file_uptiering_params_dict = file_uptiering_params_instance.to_dict()
# create an instance of FileUptieringParams from a dict
file_uptiering_params_from_dict = FileUptieringParams.from_dict(file_uptiering_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


