# IPConfigParams

Specifies the IP config parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** | Specifies the network interface name. IPs would be assigned to the specified interface. | [optional] 
**ip_family** | **int** | Specifies the IP family of the config. | [optional] 
**ips** | **List[str]** | Specifies a list of IP addresses to be assigned. | [optional] 
**node_ids** | **List[str]** | Specifies the cluster node ids. | [optional] 
**role** | **str** | Specifies the interface role. | [optional] 
**subnet_gateway** | **str** | Specifies the interface gateway. | [optional] 
**subnet_mask_bits** | **int** | Specifies the interface subnet mask bits. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.ip_config_params import IPConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of IPConfigParams from a JSON string
ip_config_params_instance = IPConfigParams.from_json(json)
# print the JSON string representation of the object
print(IPConfigParams.to_json())

# convert the object into a dict
ip_config_params_dict = ip_config_params_instance.to_dict()
# create an instance of IPConfigParams from a dict
ip_config_params_from_dict = IPConfigParams.from_dict(ip_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


