# FortknoxError

Specifies the error object with error code and a message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** | Specifies the error code. | [optional] 
**error_message** | **str** | Specifies the error message. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.fortknox_error import FortknoxError

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxError from a JSON string
fortknox_error_instance = FortknoxError.from_json(json)
# print the JSON string representation of the object
print(FortknoxError.to_json())

# convert the object into a dict
fortknox_error_dict = fortknox_error_instance.to_dict()
# create an instance of FortknoxError from a dict
fortknox_error_from_dict = FortknoxError.from_dict(fortknox_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


