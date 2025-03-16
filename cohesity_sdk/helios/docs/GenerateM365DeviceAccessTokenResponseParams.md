# GenerateM365DeviceAccessTokenResponseParams

Specifies the response parameters for Device Authorization Grant containing the access token for creating Applications through Azure PowerShell.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Specifies the access token for Microsoft365 Azure PowerShell. | [optional] 
**expires_in_secs** | **int** | Specifies the number of seconds before the included access token is valid for. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.generate_m365_device_access_token_response_params import GenerateM365DeviceAccessTokenResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateM365DeviceAccessTokenResponseParams from a JSON string
generate_m365_device_access_token_response_params_instance = GenerateM365DeviceAccessTokenResponseParams.from_json(json)
# print the JSON string representation of the object
print(GenerateM365DeviceAccessTokenResponseParams.to_json())

# convert the object into a dict
generate_m365_device_access_token_response_params_dict = generate_m365_device_access_token_response_params_instance.to_dict()
# create an instance of GenerateM365DeviceAccessTokenResponseParams from a dict
generate_m365_device_access_token_response_params_from_dict = GenerateM365DeviceAccessTokenResponseParams.from_dict(generate_m365_device_access_token_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


