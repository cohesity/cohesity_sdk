# CreatedUserAPIKey

Response instance after creating/rotating user API Keys.

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
**api_key** | **str** | Specifies the API key. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.created_user_api_key import CreatedUserAPIKey

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedUserAPIKey from a JSON string
created_user_api_key_instance = CreatedUserAPIKey.from_json(json)
# print the JSON string representation of the object
print(CreatedUserAPIKey.to_json())

# convert the object into a dict
created_user_api_key_dict = created_user_api_key_instance.to_dict()
# create an instance of CreatedUserAPIKey from a dict
created_user_api_key_from_dict = CreatedUserAPIKey.from_dict(created_user_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


