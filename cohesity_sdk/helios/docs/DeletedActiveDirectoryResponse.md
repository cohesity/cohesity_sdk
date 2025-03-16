# DeletedActiveDirectoryResponse

Specifies that whether operation was successful or not.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Specifies the operation code. | [optional] 
**message** | **str** | Specifies the result message. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.deleted_active_directory_response import DeletedActiveDirectoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedActiveDirectoryResponse from a JSON string
deleted_active_directory_response_instance = DeletedActiveDirectoryResponse.from_json(json)
# print the JSON string representation of the object
print(DeletedActiveDirectoryResponse.to_json())

# convert the object into a dict
deleted_active_directory_response_dict = deleted_active_directory_response_instance.to_dict()
# create an instance of DeletedActiveDirectoryResponse from a dict
deleted_active_directory_response_from_dict = DeletedActiveDirectoryResponse.from_dict(deleted_active_directory_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


