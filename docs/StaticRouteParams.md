# StaticRouteParams

Specifies the static route parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies a description of the Static Route. | [optional] 
**destination_network** | **str** | Specifies the destination network of the Static Route. | 
**id** | **str** | Specifies the unique identifier for the route. | [optional] [readonly] 
**interface** | **str** | Specifies the network interface name to use for communicating with the destination network. | [optional] 
**interface_group** | **str** | Specifies the network interfaces name to use for communicating with the destination network. | 
**mtu** | **int** | Specifies MTU setting per route. | [optional] 
**next_hop** | **str** | Specifies the next hop to the destination network. | 
**node_group_name** | **str** | Specifies the network node group to represent a group of nodes. | [optional] 

## Example

```python
from cohesity_sdk.models.static_route_params import StaticRouteParams

# TODO update the JSON string below
json = "{}"
# create an instance of StaticRouteParams from a JSON string
static_route_params_instance = StaticRouteParams.from_json(json)
# print the JSON string representation of the object
print(StaticRouteParams.to_json())

# convert the object into a dict
static_route_params_dict = static_route_params_instance.to_dict()
# create an instance of StaticRouteParams from a dict
static_route_params_from_dict = StaticRouteParams.from_dict(static_route_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


