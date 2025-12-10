# IpmiConfigurationParams

Specifies the parameters for configuration of IPMI.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipmi_gateway** | **str** | Specifies the default Gateway IP Address for the IPMI network | [optional] 
**ipmi_password** | **str** | Specifies the IPMI Password | [optional] 
**ipmi_subnet_mask** | **str** | Specifies the subnet mask for the IPMI network | [optional] 
**ipmi_username** | **str** | Specifies the IPMI Username | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ipmi_configuration_params import IpmiConfigurationParams

# TODO update the JSON string below
json = "{}"
# create an instance of IpmiConfigurationParams from a JSON string
ipmi_configuration_params_instance = IpmiConfigurationParams.from_json(json)
# print the JSON string representation of the object
print(IpmiConfigurationParams.to_json())

# convert the object into a dict
ipmi_configuration_params_dict = ipmi_configuration_params_instance.to_dict()
# create an instance of IpmiConfigurationParams from a dict
ipmi_configuration_params_from_dict = IpmiConfigurationParams.from_dict(ipmi_configuration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


