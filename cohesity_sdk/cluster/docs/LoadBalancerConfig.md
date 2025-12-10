# LoadBalancerConfig

Load balancer VIP config for OneHelios cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **str** | Specifies gateway. | [optional] 
**host_name** | **str** | Specifies host name of the Helios endpoint. | [optional] 
**subnet** | [**SubnetDefinition**](SubnetDefinition.md) |  | [optional] 
**virtual_ip_vec** | **List[str]** | Specifies list of Virtual IP Addresses. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.load_balancer_config import LoadBalancerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LoadBalancerConfig from a JSON string
load_balancer_config_instance = LoadBalancerConfig.from_json(json)
# print the JSON string representation of the object
print(LoadBalancerConfig.to_json())

# convert the object into a dict
load_balancer_config_dict = load_balancer_config_instance.to_dict()
# create an instance of LoadBalancerConfig from a dict
load_balancer_config_from_dict = LoadBalancerConfig.from_dict(load_balancer_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


