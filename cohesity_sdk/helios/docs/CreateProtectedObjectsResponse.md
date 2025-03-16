# CreateProtectedObjectsResponse

Specifies the protected objects response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protected_objects** | [**List[ObjectProtectionSummary]**](ObjectProtectionSummary.md) | Specifies the list of protected objects. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.create_protected_objects_response import CreateProtectedObjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProtectedObjectsResponse from a JSON string
create_protected_objects_response_instance = CreateProtectedObjectsResponse.from_json(json)
# print the JSON string representation of the object
print(CreateProtectedObjectsResponse.to_json())

# convert the object into a dict
create_protected_objects_response_dict = create_protected_objects_response_instance.to_dict()
# create an instance of CreateProtectedObjectsResponse from a dict
create_protected_objects_response_from_dict = CreateProtectedObjectsResponse.from_dict(create_protected_objects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


