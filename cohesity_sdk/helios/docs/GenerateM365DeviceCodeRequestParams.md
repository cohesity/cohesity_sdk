# GenerateM365DeviceCodeRequestParams

Specifies the request parameters to generate user and device codes for Microsoft365 Device Authorization Grant for Azure PowerShell.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Specifies the Microsoft365 domain. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.generate_m365_device_code_request_params import GenerateM365DeviceCodeRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateM365DeviceCodeRequestParams from a JSON string
generate_m365_device_code_request_params_instance = GenerateM365DeviceCodeRequestParams.from_json(json)
# print the JSON string representation of the object
print(GenerateM365DeviceCodeRequestParams.to_json())

# convert the object into a dict
generate_m365_device_code_request_params_dict = generate_m365_device_code_request_params_instance.to_dict()
# create an instance of GenerateM365DeviceCodeRequestParams from a dict
generate_m365_device_code_request_params_from_dict = GenerateM365DeviceCodeRequestParams.from_dict(generate_m365_device_code_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


