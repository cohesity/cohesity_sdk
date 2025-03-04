# GenerateM365DeviceAccessTokenRequestParams

Specifies the request parameters to generate access token code for Microsoft365 Device Authorization Grant against the specified device code.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_code** | **str** | Specifies the string used to verify the session between the client and the authorization server. The client uses this parameter to request the access token from the authorization server. | [optional] 
**domain** | **str** | Specifies the Microsoft365 domain. | [optional] 

## Example

```python
from cohesity_sdk.models.generate_m365_device_access_token_request_params import GenerateM365DeviceAccessTokenRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateM365DeviceAccessTokenRequestParams from a JSON string
generate_m365_device_access_token_request_params_instance = GenerateM365DeviceAccessTokenRequestParams.from_json(json)
# print the JSON string representation of the object
print(GenerateM365DeviceAccessTokenRequestParams.to_json())

# convert the object into a dict
generate_m365_device_access_token_request_params_dict = generate_m365_device_access_token_request_params_instance.to_dict()
# create an instance of GenerateM365DeviceAccessTokenRequestParams from a dict
generate_m365_device_access_token_request_params_from_dict = GenerateM365DeviceAccessTokenRequestParams.from_dict(generate_m365_device_access_token_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


