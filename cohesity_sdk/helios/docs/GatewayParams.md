# GatewayParams

Specifies the port & direction settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | Specifies the packet direction settings. | [optional] 
**port** | **str** | Specifies the port along with the protocol settings. For example 22/tcp, 68/udp. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.gateway_params import GatewayParams

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayParams from a JSON string
gateway_params_instance = GatewayParams.from_json(json)
# print the JSON string representation of the object
print(GatewayParams.to_json())

# convert the object into a dict
gateway_params_dict = gateway_params_instance.to_dict()
# create an instance of GatewayParams from a dict
gateway_params_from_dict = GatewayParams.from_dict(gateway_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


