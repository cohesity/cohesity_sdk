# ActiveDirectoryError

Specifies the Active Directory error object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** | Specifies the error code. | [optional] 
**error_message** | **str** | Specifies the error message corresponding to the error code. | [optional] 

## Example

```python
from cohesity_sdk.models.active_directory_error import ActiveDirectoryError

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectoryError from a JSON string
active_directory_error_instance = ActiveDirectoryError.from_json(json)
# print the JSON string representation of the object
print(ActiveDirectoryError.to_json())

# convert the object into a dict
active_directory_error_dict = active_directory_error_instance.to_dict()
# create an instance of ActiveDirectoryError from a dict
active_directory_error_from_dict = ActiveDirectoryError.from_dict(active_directory_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


