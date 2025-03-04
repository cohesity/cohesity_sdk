# UptieringPolicy

Specifies the data uptiering policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_audit_logging** | **bool** | Specifies whether to audit log the file tiering activity. | [optional] [default to False]
**file_path** | [**FileFilteringPolicy**](FileFilteringPolicy.md) |  | [optional] 
**file_size** | [**FileSizePolicy**](FileSizePolicy.md) |  | [optional] 
**file_age** | [**UptieringFileAgePolicy**](UptieringFileAgePolicy.md) |  | [optional] 
**include_all_files** | **bool** | If set, all files in the view will be uptiered regardless of file_select_policy, num_file_access, hot_file_window, file_size constraints. | [optional] [default to False]
**target** | [**UptieringTarget**](UptieringTarget.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.uptiering_policy import UptieringPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of UptieringPolicy from a JSON string
uptiering_policy_instance = UptieringPolicy.from_json(json)
# print the JSON string representation of the object
print(UptieringPolicy.to_json())

# convert the object into a dict
uptiering_policy_dict = uptiering_policy_instance.to_dict()
# create an instance of UptieringPolicy from a dict
uptiering_policy_from_dict = UptieringPolicy.from_dict(uptiering_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


