# GetProtectedObjectResponse

Specifies the protected objects response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | [**ProtectedObjectInfo**](ProtectedObjectInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.get_protected_object_response import GetProtectedObjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProtectedObjectResponse from a JSON string
get_protected_object_response_instance = GetProtectedObjectResponse.from_json(json)
# print the JSON string representation of the object
print(GetProtectedObjectResponse.to_json())

# convert the object into a dict
get_protected_object_response_dict = get_protected_object_response_instance.to_dict()
# create an instance of GetProtectedObjectResponse from a dict
get_protected_object_response_from_dict = GetProtectedObjectResponse.from_dict(get_protected_object_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


