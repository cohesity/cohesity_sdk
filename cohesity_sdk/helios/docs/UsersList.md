# UsersList

Specifies a list of users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[UserParams]**](UserParams.md) | Specifies the list of users. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.users_list import UsersList

# TODO update the JSON string below
json = "{}"
# create an instance of UsersList from a JSON string
users_list_instance = UsersList.from_json(json)
# print the JSON string representation of the object
print(UsersList.to_json())

# convert the object into a dict
users_list_dict = users_list_instance.to_dict()
# create an instance of UsersList from a dict
users_list_from_dict = UsersList.from_dict(users_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


