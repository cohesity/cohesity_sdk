# UserAPIKeys

List of user owned API Keys.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_keys** | [**List[UserAPIKey]**](UserAPIKey.md) | List of user owned API Keys. | [optional] 

## Example

```python
from cohesity_sdk.models.user_api_keys import UserAPIKeys

# TODO update the JSON string below
json = "{}"
# create an instance of UserAPIKeys from a JSON string
user_api_keys_instance = UserAPIKeys.from_json(json)
# print the JSON string representation of the object
print(UserAPIKeys.to_json())

# convert the object into a dict
user_api_keys_dict = user_api_keys_instance.to_dict()
# create an instance of UserAPIKeys from a dict
user_api_keys_from_dict = UserAPIKeys.from_dict(user_api_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


