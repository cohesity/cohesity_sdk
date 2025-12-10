# CommonTieringParams

Params common to Uptiering and Downtiering params

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_all_files** | **bool** | If set, all files in the view will be uptiered regardless of file_select_policy, num_file_access, hot_file_window, file_size constraints. | [optional] [default to False]
**target** | [**DataTieringTarget**](DataTieringTarget.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_tiering_params import CommonTieringParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonTieringParams from a JSON string
common_tiering_params_instance = CommonTieringParams.from_json(json)
# print the JSON string representation of the object
print(CommonTieringParams.to_json())

# convert the object into a dict
common_tiering_params_dict = common_tiering_params_instance.to_dict()
# create an instance of CommonTieringParams from a dict
common_tiering_params_from_dict = CommonTieringParams.from_dict(common_tiering_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


