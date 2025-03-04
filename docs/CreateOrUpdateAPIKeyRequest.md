# CreateOrUpdateAPIKeyRequest

Specified the request to create a new user API key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_time_msecs** | **int** | Specifies the time in milliseconds when the API key will expire. Set null for no expiry. | [optional] 
**is_active** | **bool** | Specifies if the API key is active. | [optional] [default to True]
**name** | **str** | Specifies the API key name. | 

## Example

```python
from cohesity_sdk.models.create_or_update_api_key_request import CreateOrUpdateAPIKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateAPIKeyRequest from a JSON string
create_or_update_api_key_request_instance = CreateOrUpdateAPIKeyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateAPIKeyRequest.to_json())

# convert the object into a dict
create_or_update_api_key_request_dict = create_or_update_api_key_request_instance.to_dict()
# create an instance of CreateOrUpdateAPIKeyRequest from a dict
create_or_update_api_key_request_from_dict = CreateOrUpdateAPIKeyRequest.from_dict(create_or_update_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


