# AuthHeader

Specifies structure of request header

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies key for the header. | [optional] 
**value** | **str** | Specifies value for the header. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.auth_header import AuthHeader

# TODO update the JSON string below
json = "{}"
# create an instance of AuthHeader from a JSON string
auth_header_instance = AuthHeader.from_json(json)
# print the JSON string representation of the object
print(AuthHeader.to_json())

# convert the object into a dict
auth_header_dict = auth_header_instance.to_dict()
# create an instance of AuthHeader from a dict
auth_header_from_dict = AuthHeader.from_dict(auth_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


