# DeleteUsersRequest

Specifies list of users to delete.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sids** | **List[str]** | Specifies a list of user sids to delete. | 

## Example

```python
from cohesity_sdk.cluster.models.delete_users_request import DeleteUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUsersRequest from a JSON string
delete_users_request_instance = DeleteUsersRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteUsersRequest.to_json())

# convert the object into a dict
delete_users_request_dict = delete_users_request_instance.to_dict()
# create an instance of DeleteUsersRequest from a dict
delete_users_request_from_dict = DeleteUsersRequest.from_dict(delete_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


