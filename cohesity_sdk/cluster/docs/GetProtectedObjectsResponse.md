# GetProtectedObjectsResponse

Specifies the protected objects response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ProtectedObjectInfo]**](ProtectedObjectInfo.md) | Specifies the protected object backup configuration and lastRun details if it has happned. | [optional] 
**pagination_info** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.get_protected_objects_response import GetProtectedObjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProtectedObjectsResponse from a JSON string
get_protected_objects_response_instance = GetProtectedObjectsResponse.from_json(json)
# print the JSON string representation of the object
print(GetProtectedObjectsResponse.to_json())

# convert the object into a dict
get_protected_objects_response_dict = get_protected_objects_response_instance.to_dict()
# create an instance of GetProtectedObjectsResponse from a dict
get_protected_objects_response_from_dict = GetProtectedObjectsResponse.from_dict(get_protected_objects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


