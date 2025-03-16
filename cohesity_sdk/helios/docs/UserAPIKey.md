# UserAPIKey

Specifies a user API key instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by_user_sid** | **str** | Specifies the user SID who created the API key. | [optional] [readonly] 
**created_time_msecs** | **int** | Specifies the time in milliseconds when the API key was created. | [optional] [readonly] 
**expiry_time_msecs** | **int** | Specifies the time in milliseconds when the API key will expire. null signifies no-expiry. | [optional] [readonly] 
**id** | **str** | Specifies the unique id of the API key. | [optional] [readonly] 
**is_active** | **bool** | Specifies if the API key is active. | [optional] [readonly] [default to True]
**is_expired** | **bool** | Specifies if the API key has expired. | [optional] [readonly] 
**last_rotated_time_msecs** | **int** | Specifies the time in milliseconds when the API key was last rotated. | [optional] [readonly] 
**name** | **str** | Specifies the API key name. | [optional] [readonly] 
**user_sid** | **str** | Specifies the user who owns the API key. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.user_api_key import UserAPIKey

# TODO update the JSON string below
json = "{}"
# create an instance of UserAPIKey from a JSON string
user_api_key_instance = UserAPIKey.from_json(json)
# print the JSON string representation of the object
print(UserAPIKey.to_json())

# convert the object into a dict
user_api_key_dict = user_api_key_instance.to_dict()
# create an instance of UserAPIKey from a dict
user_api_key_from_dict = UserAPIKey.from_dict(user_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


