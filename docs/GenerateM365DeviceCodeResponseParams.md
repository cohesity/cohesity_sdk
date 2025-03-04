# GenerateM365DeviceCodeResponseParams

Specifies the response containing the user and device codes along with the verification URI needed for Device Authorization grant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_code** | **str** | Specifies the string used to verify the session between the client and the authorization server. The client uses this parameter to request the access token from the authorization server. | [optional] 
**expires_in_secs** | **int** | The number of seconds before the deviceCode and userCode expire. | [optional] 
**interval_secs** | **int** | The number of seconds the client should wait between polling requests to check for token. | [optional] 
**user_code** | **str** | A short string shown to the user that&#39;s used to identify the session on a secondary device. | [optional] 
**verification_uri** | **str** | The URI the user should go to with the userCode in order to sign in. | [optional] 

## Example

```python
from cohesity_sdk.models.generate_m365_device_code_response_params import GenerateM365DeviceCodeResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateM365DeviceCodeResponseParams from a JSON string
generate_m365_device_code_response_params_instance = GenerateM365DeviceCodeResponseParams.from_json(json)
# print the JSON string representation of the object
print(GenerateM365DeviceCodeResponseParams.to_json())

# convert the object into a dict
generate_m365_device_code_response_params_dict = generate_m365_device_code_response_params_instance.to_dict()
# create an instance of GenerateM365DeviceCodeResponseParams from a dict
generate_m365_device_code_response_params_from_dict = GenerateM365DeviceCodeResponseParams.from_dict(generate_m365_device_code_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


